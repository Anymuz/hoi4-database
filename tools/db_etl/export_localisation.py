#!/usr/bin/env python3
"""
Extract English localisation from HOI4 game files into CSV for PostgreSQL.

Reads all *_l_english.yml files from <hoi4-root>/localisation/english/
and produces a single CSV: data/csv/localisation.csv

Usage:
    python tools/db_etl/export_localisation.py --hoi4-root "C:/path/to/Hearts of Iron IV"
    python tools/db_etl/export_localisation.py   # auto-detects Steam path

The CSV has 3 columns: loc_key, loc_value, source_file
Load into PostgreSQL with:
    \copy localisation FROM 'data/csv/localisation.csv' CSV HEADER
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

# Regex for a localisation entry:  key:N "value"  or  key: "value"
# Captures the key and the quoted value.
LOC_PATTERN = re.compile(r'^\s+(\S+?):\d*\s+"(.+)"\s*$')

DEFAULT_STEAM_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV",
    r"C:\Program Files\Steam\steamapps\common\Hearts of Iron IV",
    os.path.expanduser("~/.steam/steam/steamapps/common/Hearts of Iron IV"),
    os.path.expanduser("~/Library/Application Support/Steam/steamapps/common/Hearts of Iron IV"),
]


def find_hoi4_root() -> Path | None:
    env = os.environ.get("HOI4_ROOT")
    if env and Path(env).is_dir():
        return Path(env)
    for p in DEFAULT_STEAM_PATHS:
        if Path(p).is_dir():
            return Path(p)
    return None


def parse_loc_file(filepath: Path) -> list[tuple[str, str, str]]:
    """Parse one *_l_english.yml file, return list of (key, value, filename)."""
    rows = []
    filename = filepath.name
    try:
        # HOI4 loc files are UTF-8 with BOM
        with open(filepath, encoding="utf-8-sig") as f:
            for line in f:
                m = LOC_PATTERN.match(line)
                if m:
                    key = m.group(1)
                    value = m.group(2)
                    rows.append((key, value, filename))
    except Exception as e:
        print(f"  WARNING: Could not read {filepath}: {e}", file=sys.stderr)
    return rows


def main():
    parser = argparse.ArgumentParser(description="Export HOI4 English localisation to CSV")
    parser.add_argument("--hoi4-root", type=str, help="Path to HOI4 install directory")
    args = parser.parse_args()

    if args.hoi4_root:
        hoi4_root = Path(args.hoi4_root)
    else:
        hoi4_root = find_hoi4_root()

    if not hoi4_root or not hoi4_root.is_dir():
        print("ERROR: Could not find HOI4 install. Use --hoi4-root or set HOI4_ROOT env var.", file=sys.stderr)
        sys.exit(1)

    loc_dir = hoi4_root / "localisation" / "english"
    if not loc_dir.is_dir():
        print(f"ERROR: Localisation directory not found: {loc_dir}", file=sys.stderr)
        sys.exit(1)

    # Collect all entries
    all_rows = []
    files = sorted(loc_dir.glob("*_l_english.yml"))
    print(f"Found {len(files)} localisation files in {loc_dir}")

    for f in files:
        rows = parse_loc_file(f)
        all_rows.extend(rows)

    # Deduplicate — later files override earlier ones (same key)
    seen = {}
    for key, value, source in all_rows:
        seen[key] = (key, value, source)
    deduped = sorted(seen.values(), key=lambda r: r[0])

    # Write CSV
    out_dir = Path("data/csv")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "localisation.csv"

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["loc_key", "loc_value", "source_file"])
        writer.writerows(deduped)

    print(f"Wrote {len(deduped)} localisation entries to {out_path}")


if __name__ == "__main__":
    main()
