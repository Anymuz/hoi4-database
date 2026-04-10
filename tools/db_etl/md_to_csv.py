#!/usr/bin/env python3
"""
Markdown-to-CSV converter for HOI4 Database ETL.

Reads markdown data-dump files from docs/data-dump/ and writes PostgreSQL-ready
CSV files to data/csv/.  Each CSV matches a target database table — column names
are mapped, subsets are filtered, and multi-source tables are merged.

Usage:
    python tools/db_etl/md_to_csv.py [--dump-dir DIR] [--csv-dir DIR] [--verbose]
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from pathlib import Path
from typing import TextIO

# ── repo root (two levels up from this file) ─────────────────────────
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DUMP_DIR = REPO_ROOT / "docs" / "data-dump"
DEFAULT_CSV_DIR = REPO_ROOT / "data" / "csv"

# ── subset files: extracted for human review only, NOT loaded ─────────
SKIP_SUBSETS = {
    "character_roles_ger",
    "characters_ger",
    "division_template_regiments_ger",
    "division_template_support_ger",
    "division_templates_ger",
    "fleets_ger",
    "task_forces_ger",
    "ships_ger",
    "air_wings_ger",
    "focuses_germany",
    "focus_links_germany",
    "technologies_infantry",
    "technology_links_infantry",
    "technology_unlocks_infantry",
    "focus_trees",  # 1-row subset; focus_trees_all is the full dataset
}

# ── simple renames: dump filename (without .md) → table name ─────────
# Files with _all suffix auto-strip to the base table name unless
# overridden here.
RENAME_MAP = {
    "equipment_all":           "equipment_definitions",
    "equipment_resources_all": "equipment_resources",
    "map_definition_provinces": "provinces",
    "resources":               "resource_types",
    "decisions_all":           "decisions",
    "technology_links_all":    "technology_prerequisites",
}

# ── column renames: (table_name, dump_col) → schema_col ──────────────
COLUMN_RENAMES = {
    # equipment_definitions
    ("equipment_definitions", "archetype"):  "archetype_key",
    ("equipment_definitions", "parent"):     "parent_key",
    ("equipment_definitions", "max_speed"):  "maximum_speed",
    # provinces
    ("provinces", "r"):         "map_r",
    ("provinces", "g"):         "map_g",
    ("provinces", "b"):         "map_b",
    ("provinces", "terrain"):   "province_kind",  # definition.csv col 5 = type (land/sea/lake)
    ("provinces", "continent"): "terrain",          # definition.csv col 7 = terrain type
    ("provinces", "extra"):     "continent_id",     # definition.csv col 8 = numeric continent
    # resource_types
    ("resource_types", "cic"):     "civilian_factory_cost_unit",
    ("resource_types", "convoys"): "convoy_cost_unit",
    # sub_ideologies
    ("sub_ideologies", "sub_ideology"): "sub_ideology_key",
    ("sub_ideologies", "ideology"):     "ideology_key",
    # country_tags  → countries (initial insert)
    ("countries", "tag"):          "tag",
    ("countries", "country_file"): "country_file_path",
    # divisions
    ("divisions", "division_template"):       "template_name",
    ("divisions", "location_province"):       "location_province_id",
    # division_templates
    ("division_templates", "template_name"):  "template_name",
    # air_wings
    ("air_wings", "equipment_type"): "equipment_type",
    # fleets
    ("fleets", "naval_base_province"): "naval_base_province_id",
    # ships
    ("ships", "hull_key"):           "hull_equipment_key",
    ("ships", "owner"):              "owner_tag",
    # task_forces — fleet_name used for FK resolution later
    ("task_forces", "location_province"): "location_province_id",
    # technology_prerequisites (from technology_links_all)
    ("technology_prerequisites", "from_technology"):       "technology_key",
    ("technology_prerequisites", "to_technology"):         "prerequisite_key",
    ("technology_prerequisites", "research_cost_coeff"):   None,  # drop
    # technologies
    ("technologies", "category"): None,  # drop (→ technology_categories_junction)
    ("technologies", "folder_x"): None,  # drop visual-only data
    ("technologies", "folder_y"): None,  # drop visual-only data
    # building_types
    ("building_types", "building_type"): "building_key",
    # states
    ("states", "name_key"): "state_name_key",
    ("states", "owner"): None,            # drop (→ state_ownership_history)
    ("states", "buildings_max_level_factor"): None,  # drop (not in schema)
    # state_victory_points
    ("state_victory_points", "points"): "victory_points",
    # state_buildings
    ("state_buildings", "building_type"): "building_key",
    ("state_buildings", "scope"): None,              # drop (filter artifact)
    ("state_buildings", "key_or_province"): None,     # drop (filter artifact)
    # continents
    ("continents", "continent_id_order"): "continent_id",
    # ideologies
    ("ideologies", "ideology"): "ideology_key",
    ("ideologies", "ai_flag"): None,  # drop (not in schema)
    # unit_types
    ("unit_types", "unit_type"): "unit_type_key",
    ("unit_types", "group"): "unit_group",
    # province_building_positions
    ("province_building_positions", "linked_province"): "linked_province_id",
    # character_roles
    ("character_roles", "ideology"): "sub_ideology_key",
    # division_template_regiments
    ("division_template_regiments", "unit_type"): "unit_type_key",
    ("division_template_regiments", "x"): "grid_x",
    ("division_template_regiments", "y"): "grid_y",
    ("division_template_regiments", "source_file"): None,  # drop
    # division_template_support
    ("division_template_support", "support_unit"): "unit_type_key",
    ("division_template_support", "x"): "grid_x",
    ("division_template_support", "y"): "grid_y",
    ("division_template_support", "source_file"): None,  # drop
    # focuses
    ("focuses", "x"): "x_pos",
    ("focuses", "y"): "y_pos",
    # occupation_laws
    ("occupation_laws", "icon"): "icon_index",
    # supply_nodes
    ("supply_nodes", "column_1"): "level",
    # country_starting_technologies
    ("country_starting_technologies", "enabled"): None,  # drop
    # strategic_regions (drop extra)
    ("strategic_regions", "province_count"): None,
    # strategic_region_provinces (drop extra)
    ("strategic_region_provinces", "source_file"): None,
    # operation_tokens (drop extra)
    ("operation_tokens", "source_file"): None,
    # bookmarks (drop extra)
    ("bookmarks", "is_default"): None,
    ("bookmarks", "source_file"): None,
    # bookmark_countries (drop extra)
    ("bookmark_countries", "source_file"): None,
    # continuous_focuses (drop extra)
    ("continuous_focuses", "source_file"): None,
    # decision_categories (drop extra)
    ("decision_categories", "source_file"): None,
    # decisions (drop extra)
    ("decisions", "source_file"): None,
    # autonomy_states (drop extra)
    ("autonomy_states", "source_file"): None,
    # country_starting_doctrines (drop extra)
    ("country_starting_doctrines", "source_file"): None,
}

# ── derived columns: computed from existing data ─────────────────────
# table_name → list of { new_col, from_col, transform }
#   "prefix"  → split on '_' and take the first part  (GER_1936.txt → GER)
#   "copy"    → copy the source value unchanged
DERIVED_COLUMNS: dict[str, list[dict[str, str]]] = {
    "division_templates": [
        {"new_col": "country_tag", "from_col": "source_file", "transform": "prefix"},
        {"new_col": "oob_file",    "from_col": "source_file", "transform": "copy"},
    ],
    "divisions": [
        {"new_col": "country_tag", "from_col": "source_file", "transform": "prefix"},
        {"new_col": "oob_file",    "from_col": "source_file", "transform": "copy"},
    ],
    "fleets": [
        {"new_col": "oob_file",    "from_col": "source_file", "transform": "copy"},
    ],
    "air_wings": [
        {"new_col": "oob_file",    "from_col": "source_file", "transform": "copy"},
    ],
}

# ── columns to drop per table (after rename mapping) ─────────────────
DROP_COLUMNS: dict[str, set[str]] = {}

# ── row filters: applied BEFORE column renames/drops ─────────────────
#    table_name → (column_name, keep_value)
#    Only rows where column_name == keep_value are kept.
ROW_FILTERS = {
    "state_buildings": ("scope", "state"),
}

# ── multi-target split rules ────────────────────────────────────────
# These dump files produce rows for MULTIPLE tables based on a column value.
#   dump_name → { split_col, targets: { value → (table, col_map) } }
SPLIT_RULES = {
    "focus_links_all": {
        "split_col": "link_type",
        "targets": {
            "prerequisite": {
                "table": "focus_prerequisites",
                "columns": {
                    "focus_id":        "focus_id",
                    "linked_focus_id": "required_focus_id",
                },
                "extra_cols": {"prerequisite_group": None},  # needs post-processing
            },
            "mutually_exclusive": {
                "table": "focus_mutually_exclusive",
                "columns": {
                    "focus_id":        "focus_a_id",
                    "linked_focus_id": "focus_b_id",
                },
            },
        },
    },
    "technology_unlocks_all": {
        "split_col": "unlock_type",
        "targets": {
            "equipment": {
                "table": "technology_enables_equipment",
                "columns": {
                    "technology_key": "technology_key",
                    "unlock_key":     "equipment_key",
                    "source_file":    "source_file",
                },
            },
            "unit": {
                "table": "technology_enables_units",
                "columns": {
                    "technology_key": "technology_key",
                    "unlock_key":     "unit_type_key",
                    "source_file":    "source_file",
                },
            },
        },
    },
}

# ── countries merge: 3 source files → 1 table ───────────────────────
COUNTRIES_SOURCES = {
    "country_tags": {
        "key_col": "tag",
        "columns": {
            "tag":          "tag",
            "country_file": "country_file_path",
        },
    },
    "countries_visuals": {
        "key_col": "country_file_key",
        # match by file path → country tag lookup
        "columns": {
            "graphical_culture":    "graphical_culture",
            "graphical_culture_2d": "graphical_culture_2d",
            "color_r":              "color_r",
            "color_g":              "color_g",
            "color_b":              "color_b",
        },
    },
    "country_history": {
        "key_col": "country_tag",
        "columns": {
            "capital_state_id":       "capital_state_id",
            "stability":              "stability",
            "war_support":            "war_support",
        },
    },
}

COUNTRIES_OUTPUT_COLS = [
    "tag", "country_file_path", "graphical_culture", "graphical_culture_2d",
    "color_r", "color_g", "color_b", "capital_state_id", "stability",
    "war_support",
]


# ─────────────────────────────────────────────────────────────────────
# Markdown parsing
# ─────────────────────────────────────────────────────────────────────

def parse_md_table(path: Path) -> tuple[list[str], list[list[str]]]:
    """Parse a data-dump .md file.  Returns (columns, rows)."""
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    # Find the header row (first line starting with |)
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "---" not in line:
            header_idx = i
            break
    if header_idx is None:
        return [], []

    columns = _split_pipe_row(lines[header_idx])

    # Pre-process: merge continuation lines (e.g. " |\n" from wrapped rows)
    merged_lines: list[str] = []
    for line in lines[header_idx + 2 :]:
        stripped = line.strip()
        if not stripped:
            continue
        # A continuation line is just whitespace + pipe(s), no real cells
        if re.match(r'^\s*\|\s*$', line):
            # Append trailing pipe to previous line (fixes wrapped rows)
            if merged_lines:
                merged_lines[-1] = merged_lines[-1].rstrip('\n') + ' |\n'
            continue
        merged_lines.append(line)

    # Rows start after the separator line
    rows: list[list[str]] = []
    for line in merged_lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = _split_pipe_row(stripped)
        # Pad or trim to match column count
        while len(cells) < len(columns):
            cells.append("")
        cells = cells[: len(columns)]
        rows.append(cells)

    return columns, rows


def _split_pipe_row(line: str) -> list[str]:
    """Split a markdown pipe-delimited row into trimmed cell values."""
    parts = line.split("|")
    # Drop the empty strings from leading/trailing pipes
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.strip() for p in parts]


# ─────────────────────────────────────────────────────────────────────
# CSV writing
# ─────────────────────────────────────────────────────────────────────

def write_csv(path: Path, columns: list[str], rows: list[list[str]]) -> int:
    """Write a CSV file.  Returns row count."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)
    return len(rows)


# ─────────────────────────────────────────────────────────────────────
# Column transformation
# ─────────────────────────────────────────────────────────────────────

def apply_column_renames(
    table_name: str,
    columns: list[str],
    rows: list[list[str]],
) -> tuple[list[str], list[list[str]]]:
    """Rename columns per COLUMN_RENAMES and drop columns marked as None."""
    new_cols = []
    keep_idxs = []
    for i, col in enumerate(columns):
        mapped = COLUMN_RENAMES.get((table_name, col), col)
        if mapped is None:
            continue  # drop this column
        new_cols.append(mapped)
        keep_idxs.append(i)

    # Also apply DROP_COLUMNS
    drops = DROP_COLUMNS.get(table_name, set())
    final_cols = []
    final_idxs = []
    for col, idx in zip(new_cols, keep_idxs):
        if col not in drops:
            final_cols.append(col)
            final_idxs.append(idx)

    new_rows = [[row[i] for i in final_idxs] for row in rows]
    return final_cols, new_rows


def apply_derived_columns(
    table_name: str,
    columns: list[str],
    rows: list[list[str]],
) -> tuple[list[str], list[list[str]]]:
    """Add computed columns defined in DERIVED_COLUMNS."""
    if table_name not in DERIVED_COLUMNS:
        return columns, rows

    _oob_tag_re = re.compile(r'^([A-Z]{3})_')

    for spec in DERIVED_COLUMNS[table_name]:
        new_col = spec["new_col"]
        from_col = spec["from_col"]
        transform = spec["transform"]

        if from_col not in columns:
            continue

        src_idx = columns.index(from_col)
        columns = columns + [new_col]

        for row in rows:
            val = row[src_idx]
            if transform == "prefix":
                # Extract 3-letter uppercase country tag from OOB filename
                m = _oob_tag_re.match(val) if val else None
                derived = m.group(1) if m else ""
            elif transform == "copy":
                derived = val
            else:
                derived = ""
            row.append(derived)

    return columns, rows


# ─────────────────────────────────────────────────────────────────────
# Table name resolution
# ─────────────────────────────────────────────────────────────────────

def resolve_table_name(dump_name: str) -> str | None:
    """Map a dump filename (without .md) to its target table name.
    Returns None if the file should be skipped."""
    if dump_name in SKIP_SUBSETS:
        return None
    if dump_name in RENAME_MAP:
        return RENAME_MAP[dump_name]
    if dump_name in SPLIT_RULES:
        return None  # handled separately
    if dump_name in COUNTRIES_SOURCES:
        return None  # handled by countries merge
    if dump_name == "countries_visuals":
        return None  # handled by visual definitions processor
    # Strip _all suffix
    if dump_name.endswith("_all"):
        return dump_name[:-4]
    return dump_name


# ─────────────────────────────────────────────────────────────────────
# Multi-target split processing
# ─────────────────────────────────────────────────────────────────────

def process_split_file(
    dump_name: str,
    dump_dir: Path,
    csv_dir: Path,
    verbose: bool,
) -> dict[str, int]:
    """Process a file that splits into multiple tables.  Returns {table: rows}."""
    rule = SPLIT_RULES[dump_name]
    split_col = rule["split_col"]

    columns, rows = parse_md_table(dump_dir / f"{dump_name}.md")
    if not columns:
        return {}

    split_idx = columns.index(split_col)
    results = {}

    for split_val, target in rule["targets"].items():
        table = target["table"]
        col_map = target["columns"]

        # Filter rows by split value
        filtered = [r for r in rows if r[split_idx] == split_val]

        # Map columns
        src_cols = list(col_map.keys())
        dst_cols = list(col_map.values())
        src_idxs = []
        for sc in src_cols:
            if sc in columns:
                src_idxs.append(columns.index(sc))
            else:
                src_idxs.append(None)

        out_rows = []
        for row in filtered:
            out_row = [row[i] if i is not None else "" for i in src_idxs]
            out_rows.append(out_row)

        count = write_csv(csv_dir / f"{table}.csv", dst_cols, out_rows)
        results[table] = count
        if verbose:
            print(f"  SPLIT {dump_name} → {table}.csv ({count} rows)")

    return results


# ─────────────────────────────────────────────────────────────────────
# Countries merge
# ─────────────────────────────────────────────────────────────────────

def process_countries_merge(
    dump_dir: Path,
    csv_dir: Path,
    verbose: bool,
) -> int:
    """Merge country_tags + countries_visuals + country_history → countries.csv."""
    # Step 1: Load country_tags (primary source — defines all rows)
    cols_tags, rows_tags = parse_md_table(dump_dir / "country_tags.md")
    tag_idx = cols_tags.index("tag")
    file_idx = cols_tags.index("country_file")

    # Build {tag: {col: val}} for each country
    countries: dict[str, dict[str, str]] = {}
    tag_to_file: dict[str, str] = {}
    for row in rows_tags:
        tag = row[tag_idx]
        countries[tag] = {
            "tag": tag,
            "country_file_path": row[file_idx],
        }
        # Normalise the file reference for visual matching
        file_val = row[file_idx]
        tag_to_file[tag] = file_val

    # Step 2: Merge countries_visuals (keyed by country_file_key)
    visuals_path = dump_dir / "countries_visuals.md"
    if visuals_path.exists():
        cols_vis, rows_vis = parse_md_table(visuals_path)
        vis_key_idx = cols_vis.index("country_file_key")
        vis_map = COUNTRIES_SOURCES["countries_visuals"]["columns"]

        # Build file_key → tag lookup
        file_to_tag: dict[str, str] = {}
        for tag, fpath in tag_to_file.items():
            # Normalise: "countries/Germany.txt" → "Germany" or similar
            key = Path(fpath).stem if fpath else ""
            file_to_tag[key] = tag
            file_to_tag[fpath] = tag

        for row in rows_vis:
            file_key = row[vis_key_idx]
            # Try matching by file key directly or by stem
            tag = file_to_tag.get(file_key) or file_to_tag.get(Path(file_key).stem, "")
            if tag and tag in countries:
                for src_col, dst_col in vis_map.items():
                    if src_col in cols_vis:
                        countries[tag][dst_col] = row[cols_vis.index(src_col)]

    # Step 3: Merge country_history (keyed by country_tag)
    hist_path = dump_dir / "country_history.md"
    if hist_path.exists():
        cols_hist, rows_hist = parse_md_table(hist_path)
        hist_tag_idx = cols_hist.index("country_tag")
        hist_map = COUNTRIES_SOURCES["country_history"]["columns"]

        for row in rows_hist:
            tag = row[hist_tag_idx]
            if tag in countries:
                for src_col, dst_col in hist_map.items():
                    if src_col in cols_hist:
                        countries[tag][dst_col] = row[cols_hist.index(src_col)]

    # Step 4: Write merged CSV
    out_rows = []
    for tag in sorted(countries.keys()):
        rec = countries[tag]
        out_rows.append([rec.get(c, "") for c in COUNTRIES_OUTPUT_COLS])

    count = write_csv(csv_dir / "countries.csv", COUNTRIES_OUTPUT_COLS, out_rows)
    if verbose:
        print(f"  MERGE country_tags + countries_visuals + country_history → countries.csv ({count} rows)")
    return count


# ─────────────────────────────────────────────────────────────────────
# Country visual definitions (needs tag lookup from country_tags)
# ─────────────────────────────────────────────────────────────────────

def _process_country_visual_definitions(
    dump_dir: Path,
    csv_dir: Path,
    verbose: bool,
) -> int:
    """Generate country_visual_definitions.csv by resolving file keys to tags."""
    visuals_path = dump_dir / "countries_visuals.md"
    tags_path = dump_dir / "country_tags.md"
    if not visuals_path.exists() or not tags_path.exists():
        return -1

    # Build file_path → tag lookup from country_tags
    cols_tags, rows_tags = parse_md_table(tags_path)
    tag_idx = cols_tags.index("tag")
    file_idx = cols_tags.index("country_file")
    file_to_tag: dict[str, str] = {}
    for row in rows_tags:
        file_to_tag[row[file_idx]] = row[tag_idx]
        # Also map by stem (e.g., "Germany" from "countries/Germany.txt")
        stem = Path(row[file_idx]).stem if row[file_idx] else ""
        if stem:
            file_to_tag[stem] = row[tag_idx]

    # Parse visuals dump
    cols_vis, rows_vis = parse_md_table(visuals_path)
    key_idx = cols_vis.index("country_file_key")
    gc_idx = cols_vis.index("graphical_culture")
    gc2d_idx = cols_vis.index("graphical_culture_2d")

    out_cols = ["country_tag", "graphical_culture", "graphical_culture_2d"]
    out_rows = []
    for row in rows_vis:
        file_key = row[key_idx]
        tag = file_to_tag.get(file_key) or file_to_tag.get(Path(file_key).stem, "")
        if tag:
            out_rows.append([tag, row[gc_idx], row[gc2d_idx]])

    count = write_csv(csv_dir / "country_visual_definitions.csv", out_cols, out_rows)
    if verbose:
        print(f"  RESOLVE countries_visuals → country_visual_definitions.csv ({count} rows)")
    return count


# ─────────────────────────────────────────────────────────────────────
# Main conversion loop
# ─────────────────────────────────────────────────────────────────────

def convert_all(dump_dir: Path, csv_dir: Path, verbose: bool = False) -> None:
    """Convert all markdown dumps to CSV files."""
    csv_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(f for f in dump_dir.iterdir()
                       if f.suffix == ".md" and f.name != "SUMMARY.md")

    stats: dict[str, int] = {}
    skipped: list[str] = []
    errors: list[str] = []

    # 1. Process multi-target split files
    for dump_name in SPLIT_RULES:
        md_path = dump_dir / f"{dump_name}.md"
        if md_path.exists():
            try:
                results = process_split_file(dump_name, dump_dir, csv_dir, verbose)
                stats.update(results)
            except Exception as e:
                errors.append(f"{dump_name}: {e}")

    # 2. Process countries merge
    try:
        count = process_countries_merge(dump_dir, csv_dir, verbose)
        stats["countries"] = count
    except Exception as e:
        errors.append(f"countries merge: {e}")

    # 3. Process country_visual_definitions (needs tag lookup from country_tags)
    try:
        count = _process_country_visual_definitions(dump_dir, csv_dir, verbose)
        if count >= 0:
            stats["country_visual_definitions"] = count
    except Exception as e:
        errors.append(f"country_visual_definitions: {e}")

    # 4. Process all remaining files
    for md_path in md_files:
        dump_name = md_path.stem
        table_name = resolve_table_name(dump_name)

        if table_name is None:
            skipped.append(dump_name)
            continue

        try:
            columns, rows = parse_md_table(md_path)
            if not columns:
                errors.append(f"{dump_name}: no table found in file")
                continue

            # Apply row filters before column renames
            if table_name in ROW_FILTERS:
                filter_col, keep_val = ROW_FILTERS[table_name]
                if filter_col in columns:
                    fi = columns.index(filter_col)
                    rows = [r for r in rows if r[fi] == keep_val]

            columns, rows = apply_column_renames(table_name, columns, rows)
            columns, rows = apply_derived_columns(table_name, columns, rows)
            count = write_csv(csv_dir / f"{table_name}.csv", columns, rows)
            stats[table_name] = count
            if verbose:
                print(f"  {dump_name}.md → {table_name}.csv ({count} rows)")
        except Exception as e:
            errors.append(f"{dump_name}: {e}")

    # 5. Report
    print(f"\n{'=' * 60}")
    print(f"HOI4 Markdown → CSV Conversion Complete")
    print(f"{'=' * 60}")
    print(f"  CSV output dir : {csv_dir}")
    print(f"  Tables written : {len(stats)}")
    print(f"  Total rows     : {sum(stats.values()):,}")
    print(f"  Subsets skipped: {len(skipped)}")
    if skipped and verbose:
        for s in sorted(skipped):
            print(f"    - {s}")
    if errors:
        print(f"  ERRORS         : {len(errors)}")
        for e in errors:
            print(f"    ! {e}")
    print()


# ─────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert HOI4 markdown data-dumps to PostgreSQL-ready CSV files."
    )
    parser.add_argument(
        "--dump-dir", type=Path, default=DEFAULT_DUMP_DIR,
        help=f"Markdown dump directory (default: {DEFAULT_DUMP_DIR})",
    )
    parser.add_argument(
        "--csv-dir", type=Path, default=DEFAULT_CSV_DIR,
        help=f"CSV output directory (default: {DEFAULT_CSV_DIR})",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print per-file conversion details",
    )
    args = parser.parse_args()
    convert_all(args.dump_dir, args.csv_dir, args.verbose)


if __name__ == "__main__":
    main()
