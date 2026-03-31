import argparse
import csv
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT = REPO_ROOT / "docs" / "data-dump"

# ── HOI4 install detection ──────────────────────────────────────────────
_STEAM_COMMON = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV")
_STEAM_COMMON_ALT = Path.home() / ".steam" / "steam" / "steamapps" / "common" / "Hearts of Iron IV"

def _detect_hoi4_root(cli_path: Optional[str] = None) -> Path:
    """Return the HOI4 game root, checking (in order):
    1. Explicit CLI argument
    2. HOI4_ROOT environment variable
    3. Default Steam install paths (Windows / Linux)
    """
    if cli_path:
        p = Path(cli_path)
        if p.is_dir():
            return p
        print(f"ERROR: supplied path does not exist: {p}", file=sys.stderr)
        sys.exit(1)

    env = os.environ.get("HOI4_ROOT")
    if env:
        p = Path(env)
        if p.is_dir():
            return p
        print(f"ERROR: HOI4_ROOT env var points to non-existent path: {p}", file=sys.stderr)
        sys.exit(1)

    for candidate in (_STEAM_COMMON, _STEAM_COMMON_ALT):
        if candidate.is_dir():
            return candidate

    print(
        "ERROR: Could not auto-detect Hearts of Iron IV installation.\n"
        "Provide the path via:\n"
        "  --hoi4-root <path>           (CLI argument)\n"
        "  HOI4_ROOT=<path>             (environment variable)",
        file=sys.stderr,
    )
    sys.exit(1)

# Placeholder — set by main() after CLI parsing
ROOT: Path = Path(".")


def write_md(path: Path, title: str, table_headers: List[str], rows: List[List[str]], source: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Source: `{source}`\n\n")
        f.write("| " + " | ".join(table_headers) + " |\n")
        f.write("|" + "|".join(["---"] * len(table_headers)) + "|\n")
        for row in rows:
            safe = [str(c).replace("|", "\\|") for c in row]
            f.write("| " + " | ".join(safe) + " |\n")


def write_text(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {title}\n\n")
        f.write(body)


def parse_country_tags() -> int:
    p = ROOT / "common" / "country_tags" / "00_countries.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = ln.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^([A-Z0-9_]+)\s*=\s*"([^"]+)"', line)
        if m:
            rows.append([m.group(1), m.group(2)])
    write_md(OUT / "country_tags.md", "Country Tags", ["tag", "country_file"], rows, "common/country_tags/00_countries.txt")
    return len(rows)


def parse_map_definition() -> int:
    p = ROOT / "map" / "definition.csv"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    with p.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        for raw in f:
            parts = raw.rstrip("\n").split(";")
            if len(parts) < 8:
                continue
            rows.append(parts[:8])
    write_md(
        OUT / "map_definition_provinces.md",
        "Map Definition Provinces",
        ["province_id", "r", "g", "b", "terrain", "is_coastal", "continent", "extra"],
        rows,
        "map/definition.csv",
    )
    return len(rows)


def parse_resources() -> int:
    p = ROOT / "common" / "resources" / "00_resources.txt"
    if not p.exists():
        return 0
    txt = p.read_text(encoding="utf-8", errors="ignore")
    rows: List[List[str]] = []
    for m in re.finditer(r"\n\s*([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*)\}", txt, flags=re.S):
        key = m.group(1)
        body = m.group(2)
        icon = re.search(r"icon_frame\s*=\s*([0-9.]+)", body)
        cic = re.search(r"cic\s*=\s*([0-9.]+)", body)
        conv = re.search(r"convoys\s*=\s*([0-9.]+)", body)
        if icon and cic and conv:
            rows.append([key, icon.group(1), cic.group(1), conv.group(1)])
    write_md(OUT / "resources.md", "Resources", ["resource_key", "icon_frame", "cic", "convoys"], rows, "common/resources/00_resources.txt")
    return len(rows)


def parse_states() -> Tuple[int, int, int, int, int]:
    states_dir = ROOT / "history" / "states"
    state_rows: List[List[str]] = []
    res_rows: List[List[str]] = []
    building_rows: List[List[str]] = []
    vp_rows: List[List[str]] = []
    prov_rows: List[List[str]] = []
    for fp in sorted(states_dir.glob("*.txt")):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        sid = re.search(r"\bid\s*=\s*([0-9]+)", txt)
        if not sid:
            continue
        state_id = sid.group(1)
        name = re.search(r"\bname\s*=\s*\"([^\"]+)\"", txt)
        manpower = re.search(r"\bmanpower\s*=\s*([0-9]+)", txt)
        cat = re.search(r"\bstate_category\s*=\s*([a-zA-Z0-9_]+)", txt)
        owner = re.search(r"\bowner\s*=\s*([A-Z0-9_]+)", txt)
        bmf = re.search(r"\bbuildings_max_level_factor\s*=\s*([0-9.]+)", txt)
        ls = re.search(r"\blocal_supplies\s*=\s*([0-9.]+)", txt)
        state_rows.append([
            state_id,
            name.group(1) if name else "",
            manpower.group(1) if manpower else "",
            cat.group(1) if cat else "",
            owner.group(1) if owner else "",
            bmf.group(1) if bmf else "",
            ls.group(1) if ls else "",
            fp.name,
        ])

        res_block = re.search(r"\bresources\s*=\s*\{([^{}]*)\}", txt, flags=re.S)
        if res_block:
            for rm in re.finditer(r"([a-zA-Z0-9_]+)\s*=\s*([0-9.]+)", res_block.group(1)):
                res_rows.append([state_id, rm.group(1), rm.group(2), fp.name])

        bld_block = re.search(r"\bbuildings\s*=\s*\{([\s\S]*?)\n\s*\}", txt)
        if bld_block:
            for bm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9]+)", bld_block.group(1)):
                building_rows.append([state_id, "state", "state", bm.group(1), bm.group(2), fp.name])
            for pb in re.finditer(r"\b([0-9]+)\s*=\s*\{([^{}]*)\}", bld_block.group(1), flags=re.S):
                prov_id = pb.group(1)
                for bm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9]+)", pb.group(2)):
                    building_rows.append([state_id, "province", prov_id, bm.group(1), bm.group(2), fp.name])

        for vpm in re.finditer(r"victory_points\s*=\s*\{\s*([0-9]+)\s+([0-9]+)\s*\}", txt):
            vp_rows.append([state_id, vpm.group(1), vpm.group(2), fp.name])

        pblock = re.search(r"\bprovinces\s*=\s*\{([^}]*)\}", txt, flags=re.S)
        if pblock:
            for pv in re.findall(r"\b([0-9]+)\b", pblock.group(1)):
                prov_rows.append([state_id, pv, fp.name])

    write_md(OUT / "states.md", "States", ["state_id", "name_key", "manpower", "state_category", "owner", "buildings_max_level_factor", "local_supplies", "source_file"], state_rows, "history/states/*.txt")
    write_md(OUT / "state_resources.md", "State Resources", ["state_id", "resource_key", "amount", "source_file"], res_rows, "history/states/*.txt")
    write_md(OUT / "state_buildings.md", "State Buildings", ["state_id", "scope", "key_or_province", "building_type", "level", "source_file"], building_rows, "history/states/*.txt")
    write_md(OUT / "state_victory_points.md", "State Victory Points", ["state_id", "province_id", "points", "source_file"], vp_rows, "history/states/*.txt")
    write_md(OUT / "state_provinces.md", "State Provinces", ["state_id", "province_id", "source_file"], prov_rows, "history/states/*.txt")
    return len(state_rows), len(res_rows), len(building_rows), len(vp_rows), len(prov_rows)


def parse_country_history() -> Tuple[int, int]:
    dirp = ROOT / "history" / "countries"
    rows: List[List[str]] = []
    tech_rows: List[List[str]] = []
    for fp in sorted(dirp.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        tag = re.match(r"^([A-Z0-9]+)", fp.name).group(1)
        cap = re.search(r"\bcapital\s*=\s*([0-9]+)", txt)
        tr = re.search(r"\bstarting_train_buffer\s*=\s*([0-9.]+)", txt)
        fr = re.search(r"\bset_fuel_ratio\s*=\s*([0-9.]+)", txt)
        rs = re.search(r"\bset_research_slots\s*=\s*([0-9]+)", txt)
        st = re.search(r"\bset_stability\s*=\s*([0-9.]+)", txt)
        ws = re.search(r"\bset_war_support\s*=\s*([0-9.]+)", txt)
        oob = re.search(r"\boob\s*=\s*\"([^\"]+)\"", txt)
        rows.append([
            tag,
            cap.group(1) if cap else "",
            tr.group(1) if tr else "",
            fr.group(1) if fr else "",
            rs.group(1) if rs else "",
            st.group(1) if st else "",
            ws.group(1) if ws else "",
            oob.group(1) if oob else "",
            fp.name,
        ])

        for block in re.finditer(r"set_technology\s*=\s*\{([\s\S]*?)\}", txt):
            b = block.group(1)
            for tm in re.finditer(r"\b([a-zA-Z0-9_]+)\s*=\s*([0-9]+)", b):
                tech_rows.append([tag, tm.group(1), tm.group(2), fp.name])

    write_md(OUT / "country_history.md", "Country History", ["country_tag", "capital_state_id", "starting_train_buffer", "fuel_ratio", "research_slots", "stability", "war_support", "oob_key", "source_file"], rows, "history/countries/*.txt")
    write_md(OUT / "country_starting_technologies.md", "Country Starting Technologies", ["country_tag", "technology_key", "enabled", "source_file"], tech_rows, "history/countries/*.txt")
    return len(rows), len(tech_rows)


def parse_building_positions() -> int:
    p = ROOT / "map" / "buildings.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    with p.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            parts = raw.strip().split(";")
            if len(parts) != 7:
                continue
            rows.append(parts)
    write_md(OUT / "province_building_positions.md", "Province Building Positions", ["province_id", "building_type", "pos_x", "pos_y", "pos_z", "rotation", "linked_province"], rows, "map/buildings.txt")
    return len(rows)


def parse_strategic_regions() -> Tuple[int, int]:
    d = ROOT / "map" / "strategicregions"
    reg_rows: List[List[str]] = []
    prov_rows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        rid = re.search(r"\bid\s*=\s*([0-9]+)", txt)
        name = re.search(r"\bname\s*=\s*\"([^\"]+)\"", txt)
        if not rid:
            continue
        provinces = re.search(r"\bprovinces\s*=\s*\{([^}]*)\}", txt, flags=re.S)
        plist: List[str] = []
        if provinces:
            plist = re.findall(r"\b([0-9]+)\b", provinces.group(1))
            for pv in plist:
                prov_rows.append([rid.group(1), pv, fp.name])
        reg_rows.append([rid.group(1), name.group(1) if name else "", str(len(plist)), fp.name])
    write_md(OUT / "strategic_regions.md", "Strategic Regions", ["strategic_region_id", "name_key", "province_count", "source_file"], reg_rows, "map/strategicregions/*.txt")
    write_md(OUT / "strategic_region_provinces.md", "Strategic Region Provinces", ["strategic_region_id", "province_id", "source_file"], prov_rows, "map/strategicregions/*.txt")
    return len(reg_rows), len(prov_rows)


def parse_ideologies() -> Tuple[int, int]:
    p = ROOT / "common" / "ideologies" / "00_ideologies.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    ideos: List[List[str]] = []
    sub: List[List[str]] = []
    names = ["democratic", "communism", "fascism", "neutrality"]
    positions: List[Tuple[str, int]] = []
    for n in names:
        m = re.search(rf"\n\s*{n}\s*=\s*\{{", txt)
        if m:
            positions.append((n, m.start()))
    positions.sort(key=lambda x: x[1])
    for i, (name, pos) in enumerate(positions):
        end = positions[i + 1][1] if i + 1 < len(positions) else len(txt)
        body = txt[pos:end]
        color = re.search(r"color\s*=\s*\{\s*([0-9]+)\s+([0-9]+)\s+([0-9]+)\s*\}", body)
        ai = re.search(r"\b(ai_[a-zA-Z_]+)\s*=\s*yes", body)
        ideos.append([
            name,
            color.group(1) if color else "",
            color.group(2) if color else "",
            color.group(3) if color else "",
            ai.group(1) if ai else "",
        ])
        types = re.search(r"types\s*=\s*\{([\s\S]*?)\n\s*\}\s*\n", body)
        if types:
            for sm in re.finditer(r"\b([a-zA-Z0-9_]+)\s*=\s*\{", types.group(1)):
                sub.append([name, sm.group(1)])

    write_md(OUT / "ideologies.md", "Ideologies", ["ideology", "color_r", "color_g", "color_b", "ai_flag"], ideos, "common/ideologies/00_ideologies.txt")
    write_md(OUT / "sub_ideologies.md", "Sub Ideologies", ["ideology", "sub_ideology"], sub, "common/ideologies/00_ideologies.txt")
    return len(ideos), len(sub)


def parse_characters_ger() -> Tuple[int, int]:
    p = ROOT / "common" / "characters" / "GER.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    chars: List[List[str]] = []
    roles: List[List[str]] = []
    for m in re.finditer(r"\n\s*(GER_[a-zA-Z0-9_]+)\s*=\s*\{", txt):
        cid = m.group(1)
        # grab a local window for role detection
        start = m.start()
        end = txt.find("\n\t}", start)
        if end == -1:
            end = min(len(txt), start + 2000)
        blk = txt[start:end]
        name = re.search(r"\bname\s*=\s*([A-Za-z0-9_]+)", blk)
        gender = re.search(r"\bgender\s*=\s*([a-z]+)", blk)
        chars.append([cid, name.group(1) if name else "", gender.group(1) if gender else "male"])
        if "country_leader" in blk:
            ide = re.search(r"country_leader\s*=\s*\{[\s\S]*?ideology\s*=\s*([a-zA-Z0-9_]+)", blk)
            roles.append([cid, "country_leader", ide.group(1) if ide else "", ""])
        if "field_marshal" in blk:
            roles.append([cid, "field_marshal", "", ""])
        if "advisor" in blk:
            roles.append([cid, "advisor", "", ""])

    write_md(OUT / "characters_ger.md", "Germany Characters", ["character_id", "name_key", "gender"], chars, "common/characters/GER.txt")
    write_md(OUT / "character_roles_ger.md", "Germany Character Roles", ["character_id", "role_type", "ideology", "notes"], roles, "common/characters/GER.txt")
    return len(chars), len(roles)


def parse_focus_germany() -> Tuple[int, int, int]:
    p = ROOT / "common" / "national_focus" / "germany.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    tree_rows: List[List[str]] = []
    focus_rows: List[List[str]] = []
    link_rows: List[List[str]] = []
    tree = re.search(r"focus_tree\s*=\s*\{[\s\S]*?\bid\s*=\s*([a-zA-Z0-9_-]+)", txt)
    init = re.search(r"initial_show_position\s*=\s*\{\s*x\s*=\s*([\-0-9]+)\s*y\s*=\s*([\-0-9]+)\s*\}", txt)
    if tree:
        tree_rows.append([tree.group(1), init.group(1) if init else "", init.group(2) if init else "", "germany.txt"])

    for fm in re.finditer(r"\bfocus\s*=\s*\{([\s\S]*?)\n\s*\}", txt):
        b = fm.group(1)
        fid = re.search(r"\bid\s*=\s*([a-zA-Z0-9_-]+)", b)
        if not fid:
            continue
        x = re.search(r"\bx\s*=\s*([\-0-9]+)", b)
        y = re.search(r"\by\s*=\s*([\-0-9]+)", b)
        cost = re.search(r"\bcost\s*=\s*([0-9]+)", b)
        icon = re.search(r"\bicon\s*=\s*([A-Za-z0-9_]+)", b)
        focus_rows.append([fid.group(1), x.group(1) if x else "", y.group(1) if y else "", cost.group(1) if cost else "", icon.group(1) if icon else "", "germany.txt"])
        for pr in re.finditer(r"prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_-]+)", b):
            link_rows.append([fid.group(1), "prerequisite", pr.group(1)])
        for mx in re.finditer(r"mutually_exclusive\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_-]+)", b):
            link_rows.append([fid.group(1), "mutually_exclusive", mx.group(1)])

    write_md(OUT / "focus_trees.md", "Focus Trees", ["focus_tree_id", "initial_x", "initial_y", "source_file"], tree_rows, "common/national_focus/germany.txt")
    write_md(OUT / "focuses_germany.md", "Germany Focuses", ["focus_id", "x", "y", "cost", "icon", "source_file"], focus_rows, "common/national_focus/germany.txt")
    write_md(OUT / "focus_links_germany.md", "Germany Focus Links", ["focus_id", "link_type", "linked_focus_id"], link_rows, "common/national_focus/germany.txt")
    return len(tree_rows), len(focus_rows), len(link_rows)


def parse_division_templates_ger() -> Tuple[int, int, int]:
    p = ROOT / "history" / "units" / "GER_1936.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    templates: List[List[str]] = []
    reg_rows: List[List[str]] = []
    sup_rows: List[List[str]] = []

    for tm in re.finditer(r"division_template\s*=\s*\{([\s\S]*?)\n\}", txt):
        b = tm.group(1)
        nm = re.search(r"\bname\s*=\s*\"([^\"]+)\"", b)
        grp = re.search(r"division_names_group\s*=\s*([A-Za-z0-9_]+)", b)
        tname = nm.group(1) if nm else ""
        templates.append([tname, grp.group(1) if grp else "", "GER_1936.txt"])
        reg = re.search(r"regiments\s*=\s*\{([\s\S]*?)\n\s*\}", b)
        if reg:
            for rm in re.finditer(r"([a-zA-Z0-9_]+)\s*=\s*\{\s*x\s*=\s*([0-9]+)\s*y\s*=\s*([0-9]+)\s*\}", reg.group(1)):
                reg_rows.append([tname, rm.group(1), rm.group(2), rm.group(3), "GER_1936.txt"])
        sup = re.search(r"support\s*=\s*\{([\s\S]*?)\n\s*\}", b)
        if sup:
            for sm in re.finditer(r"([a-zA-Z0-9_]+)\s*=\s*\{\s*x\s*=\s*([0-9]+)\s*y\s*=\s*([0-9]+)\s*\}", sup.group(1)):
                sup_rows.append([tname, sm.group(1), sm.group(2), sm.group(3), "GER_1936.txt"])

    write_md(OUT / "division_templates_ger.md", "Germany Division Templates", ["template_name", "division_names_group", "source_file"], templates, "history/units/GER_1936.txt")
    write_md(OUT / "division_template_regiments_ger.md", "Germany Division Template Regiments", ["template_name", "unit_type", "x", "y", "source_file"], reg_rows, "history/units/GER_1936.txt")
    write_md(OUT / "division_template_support_ger.md", "Germany Division Template Support", ["template_name", "support_unit", "x", "y", "source_file"], sup_rows, "history/units/GER_1936.txt")
    return len(templates), len(reg_rows), len(sup_rows)


def parse_naval_oob_ger() -> Tuple[int, int, int]:
    p = ROOT / "history" / "units" / "GER_1936_naval_mtg.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    fleet_rows: List[List[str]] = []
    tf_rows: List[List[str]] = []
    ship_rows: List[List[str]] = []
    current_fleet = ""
    current_tf = ""
    current_base = ""
    in_fleet = False
    in_tf = False
    brace_stack = 0
    for raw in txt.splitlines():
        line = raw.strip()
        if not line:
            continue
        brace_stack += line.count("{")
        brace_stack -= line.count("}")
        if line.startswith("fleet") and "{" in line:
            in_fleet = True
            in_tf = False
            current_fleet = ""
            current_base = ""
            continue
        if in_fleet and not in_tf and line.startswith("name") and current_fleet == "":
            m = re.search(r'"([^"]+)"', line)
            if m:
                current_fleet = m.group(1)
            continue
        if in_fleet and not in_tf and line.startswith("naval_base"):
            m = re.search(r"([0-9]+)", line)
            if m:
                current_base = m.group(1)
                fleet_rows.append(["GER", current_fleet, current_base, "GER_1936_naval_mtg.txt"])
            continue
        if in_fleet and line.startswith("task_force") and "{" in line:
            in_tf = True
            current_tf = ""
            continue
        if in_tf and line.startswith("name") and current_tf == "":
            m = re.search(r'"([^"]+)"', line)
            if m:
                current_tf = m.group(1)
            continue
        if in_tf and line.startswith("location"):
            m = re.search(r"([0-9]+)", line)
            tf_rows.append([current_fleet, current_tf, m.group(1) if m else "", "GER_1936_naval_mtg.txt"])
            continue
        if in_tf and "ship = {" in line:
            sname = re.search(r"name\s*=\s*\"([^\"]+)\"", line)
            dfn = re.search(r"definition\s*=\s*([a-zA-Z0-9_]+)", line)
            hull = re.search(r"equipment\s*=\s*\{\s*([a-zA-Z0-9_]+)\s*=", line)
            owner = re.search(r"owner\s*=\s*([A-Z0-9_]+)", line)
            ver = re.search(r"version_name\s*=\s*\"([^\"]+)\"", line)
            pride = "yes" if "pride_of_the_fleet = yes" in line else "no"
            ship_rows.append([
                current_fleet,
                current_tf,
                sname.group(1) if sname else "",
                dfn.group(1) if dfn else "",
                hull.group(1) if hull else "",
                owner.group(1) if owner else "",
                ver.group(1) if ver else "",
                pride,
                "GER_1936_naval_mtg.txt",
            ])
            continue
        # close task force/fleet when braces unwind enough
        if in_tf and line == "}":
            in_tf = False
            continue
        if in_fleet and not in_tf and line == "}" and brace_stack <= 1:
            in_fleet = False
            continue

    write_md(OUT / "fleets_ger.md", "Germany Fleets", ["country_tag", "fleet_name", "naval_base_province", "source_file"], fleet_rows, "history/units/GER_1936_naval_mtg.txt")
    write_md(OUT / "task_forces_ger.md", "Germany Task Forces", ["fleet_name", "task_force_name", "location_province", "source_file"], tf_rows, "history/units/GER_1936_naval_mtg.txt")
    write_md(OUT / "ships_ger.md", "Germany Ships", ["fleet_name", "task_force_name", "ship_name", "definition", "hull_key", "owner", "version_name", "pride_of_the_fleet", "source_file"], ship_rows, "history/units/GER_1936_naval_mtg.txt")
    return len(fleet_rows), len(tf_rows), len(ship_rows)


def parse_air_oob_ger() -> int:
    p = ROOT / "history" / "units" / "GER_1936_air_bba.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    rows: List[List[str]] = []
    current_loc = ""
    current_wing = ""
    current_eq = ""
    eq_owner = ""
    eq_amount = ""
    eq_version = ""
    in_air = False
    in_wing = False
    in_eq = False
    for raw in txt.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("air_wings") and "{" in line:
            in_air = True
            continue
        mloc = re.match(r"^([0-9]+)\s*=\s*\{", line)
        if in_air and mloc:
            in_wing = True
            current_loc = mloc.group(1)
            current_wing = ""
            continue
        if in_wing and line.startswith("name"):
            mn = re.search(r'"([^"]+)"', line)
            if mn:
                current_wing = mn.group(1)
            continue
        meq = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*\{", line)
        if in_wing and meq and meq.group(1) != "name":
            in_eq = True
            current_eq = meq.group(1)
            eq_owner = ""
            eq_amount = ""
            eq_version = ""
            continue
        if in_eq and line.startswith("owner"):
            mo = re.search(r'"?([A-Z0-9_]+)"?', line)
            if mo:
                eq_owner = mo.group(1)
            continue
        if in_eq and line.startswith("amount"):
            ma = re.search(r"([0-9]+)", line)
            if ma:
                eq_amount = ma.group(1)
            continue
        if in_eq and line.startswith("version_name"):
            mv = re.search(r'"([^"]+)"', line)
            if mv:
                eq_version = mv.group(1)
            continue
        if in_eq and line == "}":
            rows.append([current_loc, current_wing, current_eq, eq_owner, eq_amount, eq_version, "GER_1936_air_bba.txt"])
            in_eq = False
            continue
        if in_wing and not in_eq and line == "}":
            in_wing = False
            continue
    write_md(OUT / "air_wings_ger.md", "Germany Air Wings (BBA)", ["location_state_id", "wing_name", "equipment_type", "owner", "amount", "version_name", "source_file"], rows, "history/units/GER_1936_air_bba.txt")
    return len(rows)


# ── All-country naval OOB ───────────────────────────────────────────
def parse_naval_oob_all() -> Tuple[int, int, int]:
    """Parse fleet/task_force/ship data from ALL naval OOB files.

    Prefers *_naval_mtg.txt (Man the Guns DLC) when available,
    falls back to plain *_naval.txt.  Skips *_legacy.txt files.
    """
    d = ROOT / "history" / "units"
    # Collect candidate files, keyed by (TAG, year) to handle MTG priority
    candidates: Dict[Tuple[str, str], Path] = {}
    for fp in sorted(d.glob("*naval*.txt")):
        name = fp.name.lower()
        if "legacy" in name:
            continue
        tag_m = re.match(r"^([A-Z0-9]+)_(\d{4})_", fp.name)
        if not tag_m:
            continue
        key = (tag_m.group(1), tag_m.group(2))
        is_mtg = "_mtg" in name
        # Prefer MTG over plain
        if key not in candidates or is_mtg:
            candidates[key] = fp

    fleet_rows: List[List[str]] = []
    tf_rows: List[List[str]] = []
    ship_rows: List[List[str]] = []

    for (_tag, _year), fp in sorted(candidates.items()):
        tag = _tag
        src = fp.name
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        current_fleet = ""
        current_tf = ""
        current_base = ""
        in_fleet = False
        in_tf = False
        brace_stack = 0
        for raw in txt.splitlines():
            line = raw.strip()
            if not line:
                continue
            brace_stack += line.count("{")
            brace_stack -= line.count("}")
            if line.startswith("fleet") and "{" in line:
                in_fleet = True
                in_tf = False
                current_fleet = ""
                current_base = ""
                continue
            if in_fleet and not in_tf and line.startswith("name") and current_fleet == "":
                m = re.search(r'"([^"]+)"', line)
                if m:
                    current_fleet = m.group(1)
                continue
            if in_fleet and not in_tf and line.startswith("naval_base"):
                m = re.search(r"([0-9]+)", line)
                if m:
                    current_base = m.group(1)
                    fleet_rows.append([tag, current_fleet, current_base, src])
                continue
            if in_fleet and line.startswith("task_force") and "{" in line:
                in_tf = True
                current_tf = ""
                continue
            if in_tf and line.startswith("name") and current_tf == "":
                m = re.search(r'"([^"]+)"', line)
                if m:
                    current_tf = m.group(1)
                continue
            if in_tf and line.startswith("location"):
                m = re.search(r"([0-9]+)", line)
                tf_rows.append([tag, current_fleet, current_tf, m.group(1) if m else "", src])
                continue
            if in_tf and "ship = {" in line:
                sname = re.search(r"name\s*=\s*\"([^\"]+)\"", line)
                dfn = re.search(r"definition\s*=\s*([a-zA-Z0-9_]+)", line)
                hull = re.search(r"equipment\s*=\s*\{\s*([a-zA-Z0-9_]+)\s*=", line)
                owner = re.search(r"owner\s*=\s*([A-Z0-9_]+)", line)
                ver = re.search(r"version_name\s*=\s*\"([^\"]+)\"", line)
                pride = "yes" if "pride_of_the_fleet = yes" in line else "no"
                ship_rows.append([
                    tag,
                    current_fleet,
                    current_tf,
                    sname.group(1) if sname else "",
                    dfn.group(1) if dfn else "",
                    hull.group(1) if hull else "",
                    owner.group(1) if owner else "",
                    ver.group(1) if ver else "",
                    pride,
                    src,
                ])
                continue
            if in_tf and line == "}":
                in_tf = False
                continue
            if in_fleet and not in_tf and line == "}" and brace_stack <= 1:
                in_fleet = False
                continue

    write_md(OUT / "fleets_all.md", "Fleets (All Naval OOB Files)",
        ["country_tag", "fleet_name", "naval_base_province", "source_file"],
        fleet_rows, "history/units/*naval*.txt excluding legacy")
    write_md(OUT / "task_forces_all.md", "Task Forces (All Naval OOB Files)",
        ["country_tag", "fleet_name", "task_force_name", "location_province", "source_file"],
        tf_rows, "history/units/*naval*.txt excluding legacy")
    write_md(OUT / "ships_all.md", "Ships (All Naval OOB Files)",
        ["country_tag", "fleet_name", "task_force_name", "ship_name", "definition", "hull_key", "owner", "version_name", "pride_of_the_fleet", "source_file"],
        ship_rows, "history/units/*naval*.txt excluding legacy")
    return len(fleet_rows), len(tf_rows), len(ship_rows)


# ── All-country air OOB ─────────────────────────────────────────────
def parse_air_oob_all() -> int:
    """Parse air wing data from ALL *_air_bba.txt files (By Blood Alone DLC)."""
    d = ROOT / "history" / "units"
    rows: List[List[str]] = []
    for fp in sorted(d.glob("*_air_bba.txt")):
        tag_m = re.match(r"^([A-Z0-9]+)_", fp.name)
        if not tag_m:
            continue
        tag = tag_m.group(1)
        src = fp.name
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        current_loc = ""
        current_wing = ""
        current_eq = ""
        eq_amount = ""
        eq_version = ""
        in_air = False
        in_wing = False
        in_eq = False
        for raw in txt.splitlines():
            line = raw.strip()
            if not line:
                continue
            if line.startswith("air_wings") and "{" in line:
                in_air = True
                continue
            mloc = re.match(r"^([0-9]+)\s*=\s*\{", line)
            if in_air and mloc:
                in_wing = True
                current_loc = mloc.group(1)
                current_wing = ""
                continue
            if in_wing and line.startswith("name"):
                mn = re.search(r'"([^"]+)"', line)
                if mn:
                    current_wing = mn.group(1)
                continue
            meq = re.match(r"^([a-zA-Z0-9_]+)\s*=\s*\{", line)
            if in_wing and meq and meq.group(1) != "name":
                current_eq = meq.group(1)
                # Handle single-line blocks: equipment = { owner = "AFG" amount = 28 ... }
                if "}" in line:
                    ma = re.search(r"amount\s*=\s*([0-9]+)", line)
                    mv = re.search(r'version_name\s*=\s*"([^"]+)"', line)
                    rows.append([tag, current_loc, current_wing, current_eq,
                                 ma.group(1) if ma else "",
                                 mv.group(1) if mv else "",
                                 src])
                else:
                    in_eq = True
                    eq_amount = ""
                    eq_version = ""
                continue
            if in_eq and line.startswith("amount"):
                ma = re.search(r"([0-9]+)", line)
                if ma:
                    eq_amount = ma.group(1)
                continue
            if in_eq and line.startswith("version_name"):
                mv = re.search(r'"([^"]+)"', line)
                if mv:
                    eq_version = mv.group(1)
                continue
            if in_eq and line == "}":
                rows.append([tag, current_loc, current_wing, current_eq, eq_amount, eq_version, src])
                in_eq = False
                continue
            if in_wing and not in_eq and line == "}":
                in_wing = False
                continue
            if in_air and not in_wing and line == "}":
                in_air = False
                continue
    write_md(OUT / "air_wings_all.md", "Air Wings (All BBA OOB Files)",
        ["country_tag", "location_state_id", "wing_name", "equipment_type", "amount", "version_name", "source_file"],
        rows, "history/units/*_air_bba.txt")
    return len(rows)


def parse_continents() -> int:
    p = ROOT / "map" / "continent.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    rows: List[List[str]] = []
    i = 1
    for c in re.findall(r"\b([a-z_]+)\b", txt):
        if c in {"continents"}:
            continue
        rows.append([str(i), c])
        i += 1
    write_md(OUT / "continents.md", "Continents", ["continent_id_order", "continent_key"], rows, "map/continent.txt")
    return len(rows)


def parse_building_types() -> int:
    p = ROOT / "common" / "buildings" / "00_buildings.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    rows: List[List[str]] = []
    for bm in re.finditer(r"\n\s*([a-z_]+)\s*=\s*\{([\s\S]*?)\n\s*\}", txt):
        key = bm.group(1)
        body = bm.group(2)
        bc = re.search(r"base_cost\s*=\s*([0-9.]+)", body)
        som = re.search(r"show_on_map\s*=\s*([0-9.]+)", body)
        stmax = re.search(r"state_max\s*=\s*([0-9.]+)", body)
        prmax = re.search(r"province_max\s*=\s*([0-9.]+)", body)
        shares = "yes" if "shares_slots = yes" in body else "no"
        rows.append([
            key,
            bc.group(1) if bc else "",
            som.group(1) if som else "",
            stmax.group(1) if stmax else "",
            prmax.group(1) if prmax else "",
            shares,
            "00_buildings.txt",
        ])
    write_md(OUT / "building_types.md", "Building Types", ["building_type", "base_cost", "show_on_map", "state_max", "province_max", "shares_slots", "source_file"], rows, "common/buildings/00_buildings.txt")
    return len(rows)


def parse_technologies_infantry() -> Tuple[int, int, int]:
    p = ROOT / "common" / "technologies" / "infantry.txt"
    txt = p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""
    trows: List[List[str]] = []
    lrows: List[List[str]] = []
    urows: List[List[str]] = []
    for tm in re.finditer(r"\n\s*([a-zA-Z0-9_]+)\s*=\s*\{([\s\S]*?)\n\s*\}", txt):
        key = tm.group(1)
        if key.startswith("@"):
            continue
        body = tm.group(2)
        rc = re.search(r"research_cost\s*=\s*([0-9.]+)", body)
        sy = re.search(r"start_year\s*=\s*([0-9]+)", body)
        fn = re.search(r"folder\s*=\s*\{[^}]*name\s*=\s*([a-zA-Z0-9_]+)", body)
        fx = re.search(r"position\s*=\s*\{\s*x\s*=\s*([^\s}]+)", body)
        fy = re.search(r"position\s*=\s*\{[^}]*y\s*=\s*([^\s}]+)", body)
        cat = re.search(r"categories\s*=\s*\{\s*([a-zA-Z0-9_]+)", body)
        if rc or sy or fn:
            trows.append([key, rc.group(1) if rc else "", sy.group(1) if sy else "", fn.group(1) if fn else "", fx.group(1) if fx else "", fy.group(1) if fy else "", cat.group(1) if cat else ""])
        for lm in re.finditer(r"leads_to_tech\s*=\s*([a-zA-Z0-9_]+)", body):
            coeff = re.search(r"research_cost_coeff\s*=\s*([0-9.]+)", body)
            lrows.append([key, lm.group(1), coeff.group(1) if coeff else ""])
        for um in re.finditer(r"enable_equipments\s*=\s*\{([^}]*)\}", body, flags=re.S):
            for eq in re.findall(r"\b([a-zA-Z0-9_]+)\b", um.group(1)):
                urows.append([key, "equipment", eq])
        for um in re.finditer(r"enable_subunits\s*=\s*\{([^}]*)\}", body, flags=re.S):
            for su in re.findall(r"\b([a-zA-Z0-9_]+)\b", um.group(1)):
                urows.append([key, "subunit", su])

    write_md(OUT / "technologies_infantry.md", "Infantry Technologies", ["technology_key", "research_cost", "start_year", "folder_name", "folder_x", "folder_y", "category"], trows, "common/technologies/infantry.txt")
    write_md(OUT / "technology_links_infantry.md", "Infantry Technology Links", ["from_technology", "to_technology", "research_cost_coeff"], lrows, "common/technologies/infantry.txt")
    write_md(OUT / "technology_unlocks_infantry.md", "Infantry Technology Unlocks", ["technology_key", "unlock_type", "unlock_key"], urows, "common/technologies/infantry.txt")
    return len(trows), len(lrows), len(urows)


def parse_map_supply_nodes() -> int:
    p = ROOT / "map" / "supply_nodes.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = ln.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            rows.append([parts[0], parts[1]])
    write_md(OUT / "supply_nodes.md", "Supply Nodes", ["column_1", "province_id"], rows, "map/supply_nodes.txt")
    return len(rows)


def strip_comments(text: str) -> str:
    lines = []
    for ln in text.splitlines():
        # remove full-line and trailing comments
        if "#" in ln:
            idx = ln.find("#")
            ln = ln[:idx]
        lines.append(ln)
    return "\n".join(lines)


def extract_block(text: str, start: int) -> str:
    """Extract a brace-matched block starting from the first '{' at or after `start`.
    Returns the content between (and excluding) the outermost braces."""
    idx = text.find("{", start)
    if idx == -1:
        return ""
    depth = 0
    for i in range(idx, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[idx + 1 : i]
    return text[idx + 1 :]


def find_top_level_blocks(text: str, wrapper: str = "") -> list:
    """Find all top-level key = { ... } blocks inside an optional wrapper block.
    Returns list of (key, body_str, start_pos) tuples."""
    src = text
    if wrapper:
        m = re.search(rf"\b{wrapper}\s*=\s*\{{", src)
        if not m:
            return []
        src = extract_block(src, m.start())
    results = []
    pos = 0
    while pos < len(src):
        m = re.search(r"\b([a-zA-Z0-9_]+)\s*=\s*\{", src[pos:])
        if not m:
            break
        key = m.group(1)
        abs_pos = pos + m.start()
        body = extract_block(src, abs_pos)
        results.append((key, body, abs_pos))
        # advance past this block
        block_start = src.find("{", abs_pos)
        pos = block_start + len(body) + 2  # +2 for the { and }
    return results


def parse_country_visuals_all() -> int:
    d = ROOT / "common" / "countries"
    rows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        gc = re.search(r"\bgraphical_culture\s*=\s*([a-zA-Z0-9_]+)", txt)
        gc2d = re.search(r"\bgraphical_culture_2d\s*=\s*([a-zA-Z0-9_]+)", txt)
        color = re.search(r"\bcolor\s*=\s*\{\s*([0-9]+)\s+([0-9]+)\s+([0-9]+)", txt)
        rows.append([
            fp.stem,
            gc.group(1) if gc else "",
            gc2d.group(1) if gc2d else "",
            color.group(1) if color else "",
            color.group(2) if color else "",
            color.group(3) if color else "",
            fp.name,
        ])
    write_md(
        OUT / "countries_visuals.md",
        "Countries Visuals",
        ["country_file_key", "graphical_culture", "graphical_culture_2d", "color_r", "color_g", "color_b", "source_file"],
        rows,
        "common/countries/*.txt",
    )
    return len(rows)


def parse_technologies_all() -> Tuple[int, int, int]:
    d = ROOT / "common" / "technologies"
    tech_rows: List[List[str]] = []
    link_rows: List[List[str]] = []
    unlock_rows: List[List[str]] = []
    skip_keys = {"technologies", "folder", "path", "ai_will_do", "categories",
                 "on_research_complete", "on_research_complete_limit", "doctrine",
                 "sub_technologies", "OR", "AND", "NOT", "IF", "ELSE", "ELSE_IF",
                 "limit", "modifier", "available", "allow", "special_project_specialization"}
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # Find the outer technologies = { } wrapper
        wrapper_m = re.search(r"\btechnologies\s*=\s*\{", txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        # Parse each top-level block inside the wrapper
        for key, body, _ in find_top_level_blocks(wrapper_body):
            if key in skip_keys or key.startswith("@"):
                continue
            rc = re.search(r"\bresearch_cost\s*=\s*([0-9.]+)", body)
            sy = re.search(r"\bstart_year\s*=\s*([0-9]+)", body)
            fn = re.search(r"folder\s*=\s*\{[^}]*name\s*=\s*([a-zA-Z0-9_]+)", body)
            fx = re.search(r"position\s*=\s*\{\s*x\s*=\s*([^\s}]+)", body)
            fy = re.search(r"position\s*=\s*\{[^}]*y\s*=\s*([^\s}]+)", body)
            cat = re.search(r"\bcategories\s*=\s*\{([^}]*)\}", body)
            cat_first = ""
            if cat:
                cats = re.findall(r"\b([a-zA-Z0-9_]+)\b", cat.group(1))
                cat_first = cats[0] if cats else ""
            if rc or sy or fn or cat_first:
                tech_rows.append([
                    key,
                    rc.group(1) if rc else "",
                    sy.group(1) if sy else "",
                    fn.group(1) if fn else "",
                    fx.group(1) if fx else "",
                    fy.group(1) if fy else "",
                    cat_first,
                    fp.name,
                ])
            for lm in re.finditer(r"leads_to_tech\s*=\s*([a-zA-Z0-9_]+)", body):
                # find research_cost_coeff near this path block
                coeff = re.search(r"\bresearch_cost_coeff\s*=\s*([0-9.]+)", body)
                link_rows.append([key, lm.group(1), coeff.group(1) if coeff else "", fp.name])
            for um in re.finditer(r"\benable_equipments\s*=\s*\{([^}]*)\}", body, flags=re.S):
                for eq in re.findall(r"\b([a-zA-Z0-9_]+)\b", um.group(1)):
                    unlock_rows.append([key, "equipment", eq, fp.name])
            for um in re.finditer(r"\benable_subunits\s*=\s*\{([^}]*)\}", body, flags=re.S):
                for su in re.findall(r"\b([a-zA-Z0-9_]+)\b", um.group(1)):
                    unlock_rows.append([key, "subunit", su, fp.name])
            for um in re.finditer(r"\benable_equipment_modules\s*=\s*\{([^}]*)\}", body, flags=re.S):
                for eq in re.findall(r"\b([a-zA-Z0-9_]+)\b", um.group(1)):
                    unlock_rows.append([key, "module", eq, fp.name])

    write_md(OUT / "technologies_all.md", "Technologies (All Files)", ["technology_key", "research_cost", "start_year", "folder_name", "folder_x", "folder_y", "category", "source_file"], tech_rows, "common/technologies/*.txt")
    write_md(OUT / "technology_links_all.md", "Technology Links (All Files)", ["from_technology", "to_technology", "research_cost_coeff", "source_file"], link_rows, "common/technologies/*.txt")
    write_md(OUT / "technology_unlocks_all.md", "Technology Unlocks (All Files)", ["technology_key", "unlock_type", "unlock_key", "source_file"], unlock_rows, "common/technologies/*.txt")
    return len(tech_rows), len(link_rows), len(unlock_rows)


def parse_focuses_all() -> Tuple[int, int, int]:
    d = ROOT / "common" / "national_focus"
    tree_rows: List[List[str]] = []
    focus_rows: List[List[str]] = []
    link_rows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for tm in re.finditer(r"focus_tree\s*=\s*\{([\s\S]*?)\n\}", txt):
            tb = tm.group(1)
            tid = re.search(r"\bid\s*=\s*([a-zA-Z0-9_-]+)", tb)
            if not tid:
                continue
            init = re.search(r"initial_show_position\s*=\s*\{\s*x\s*=\s*([\-0-9]+)\s*y\s*=\s*([\-0-9]+)", tb)
            tree_rows.append([tid.group(1), init.group(1) if init else "", init.group(2) if init else "", fp.name])
            for fm in re.finditer(r"\bfocus\s*=\s*\{([\s\S]*?)\n\s*\}", tb):
                b = fm.group(1)
                fid = re.search(r"\bid\s*=\s*([a-zA-Z0-9_-]+)", b)
                if not fid:
                    continue
                x = re.search(r"\bx\s*=\s*([\-0-9]+)", b)
                y = re.search(r"\by\s*=\s*([\-0-9]+)", b)
                cost = re.search(r"\bcost\s*=\s*([0-9]+)", b)
                icon = re.search(r"\bicon\s*=\s*([A-Za-z0-9_]+)", b)
                focus_rows.append([fid.group(1), tid.group(1), x.group(1) if x else "", y.group(1) if y else "", cost.group(1) if cost else "", icon.group(1) if icon else "", fp.name])
                for pr in re.finditer(r"prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_-]+)", b):
                    link_rows.append([fid.group(1), "prerequisite", pr.group(1), fp.name])
                for mx in re.finditer(r"mutually_exclusive\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_-]+)", b):
                    link_rows.append([fid.group(1), "mutually_exclusive", mx.group(1), fp.name])
    write_md(OUT / "focus_trees_all.md", "Focus Trees (All Files)", ["focus_tree_id", "initial_x", "initial_y", "source_file"], tree_rows, "common/national_focus/*.txt")
    write_md(OUT / "focuses_all.md", "Focuses (All Files)", ["focus_id", "focus_tree_id", "x", "y", "cost", "icon", "source_file"], focus_rows, "common/national_focus/*.txt")
    write_md(OUT / "focus_links_all.md", "Focus Links (All Files)", ["focus_id", "link_type", "linked_focus_id", "source_file"], link_rows, "common/national_focus/*.txt")
    return len(tree_rows), len(focus_rows), len(link_rows)


def parse_characters_all() -> Tuple[int, int]:
    d = ROOT / "common" / "characters"
    crows: List[List[str]] = []
    rrows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for m in re.finditer(r"\n\s*([A-Z0-9_]+_[a-zA-Z0-9_]+)\s*=\s*\{", txt):
            cid = m.group(1)
            start = m.start()
            blk = extract_block(txt, start)
            if not blk:
                continue
            name = re.search(r"\bname\s*=\s*([A-Za-z0-9_]+)", blk)
            gender = re.search(r"\bgender\s*=\s*([a-z]+)", blk)
            crows.append([cid, name.group(1) if name else "", gender.group(1) if gender else "male", fp.name])
            if "country_leader" in blk:
                ide = re.search(r"country_leader\s*=\s*\{[\s\S]*?ideology\s*=\s*([a-zA-Z0-9_]+)", blk)
                rrows.append([cid, "country_leader", ide.group(1) if ide else "", fp.name])
            if "field_marshal" in blk:
                rrows.append([cid, "field_marshal", "", fp.name])
            if "corps_commander" in blk:
                rrows.append([cid, "corps_commander", "", fp.name])
            if "advisor" in blk:
                rrows.append([cid, "advisor", "", fp.name])
    write_md(OUT / "characters_all.md", "Characters (All Files)", ["character_id", "name_key", "gender", "source_file"], crows, "common/characters/*.txt")
    write_md(OUT / "character_roles_all.md", "Character Roles (All Files)", ["character_id", "role_type", "ideology", "source_file"], rrows, "common/characters/*.txt")
    return len(crows), len(rrows)


def parse_ideas_all() -> Tuple[int, int]:
    d = ROOT / "common" / "ideas"
    irows: List[List[str]] = []
    mrows: List[List[str]] = []
    skip_keys = {"ideas", "country", "hidden_ideas", "on_add", "on_remove",
                 "allowed", "available", "visible", "ai_will_do", "cancel_if_invalid",
                 "allowed_civil_war", "rule", "do_effect", "allowed_to_remove",
                 "traits", "OR", "AND", "NOT", "IF", "ELSE", "ELSE_IF", "limit",
                 "targeted_modifier", "research_bonus", "equipment_bonus"}
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # Find ideas = { wrapper
        wrapper_m = re.search(r"\bideas\s*=\s*\{", txt)
        if not wrapper_m:
            continue
        ideas_body = extract_block(txt, wrapper_m.start())
        # Level 1: slot categories (economy, trade_laws, mobilization_laws, country, hidden_ideas, etc.)
        for slot_key, slot_body, _ in find_top_level_blocks(ideas_body):
            if slot_key in {"country", "hidden_ideas"}:
                # These contain ideas directly
                _parse_idea_entries(slot_key, slot_body, fp.name, irows, mrows, skip_keys)
                continue
            # Check if this is a slot with law = yes or use_list_view = yes
            is_law = "law = yes" in slot_body.split("\n")[0] if slot_body else False
            # Check first few lines for slot-level flags
            first_lines = slot_body[:200] if slot_body else ""
            is_law = "law = yes" in first_lines
            _parse_idea_entries(slot_key, slot_body, fp.name, irows, mrows, skip_keys, is_law_slot=is_law)

    write_md(OUT / "ideas_all.md", "Ideas (All Files)", ["idea_key", "slot", "is_law", "cost", "removal_cost", "is_default", "source_file"], irows, "common/ideas/*.txt")
    write_md(OUT / "idea_modifiers_all.md", "Idea Modifiers (All Files)", ["idea_key", "modifier_key", "modifier_value", "source_file"], mrows, "common/ideas/*.txt")
    return len(irows), len(mrows)


def _parse_idea_entries(slot_key: str, slot_body: str, filename: str,
                        irows: list, mrows: list, skip_keys: set,
                        is_law_slot: bool = False) -> None:
    """Parse individual idea entries within a slot body."""
    for idea_key, idea_body, _ in find_top_level_blocks(slot_body):
        if idea_key in skip_keys:
            continue
        # Must look like an idea — has modifier, cost, removal_cost, or default
        has_idea_markers = any(k in idea_body for k in [
            "modifier", "removal_cost", "cost", "default = yes",
            "allowed", "available", "cancel_if_invalid", "on_add",
            "level", "research_bonus", "equipment_bonus"
        ])
        if not has_idea_markers:
            continue
        cost = re.search(r"\bcost\s*=\s*([0-9.\-]+)", idea_body)
        rem = re.search(r"\bremoval_cost\s*=\s*([0-9.\-]+)", idea_body)
        is_default = "yes" if "default = yes" in idea_body else "no"
        is_law = "yes" if is_law_slot or "law = yes" in idea_body else "no"
        irows.append([idea_key, slot_key, is_law, cost.group(1) if cost else "",
                       rem.group(1) if rem else "", is_default, filename])
        # Extract modifier block using brace matching
        mod_m = re.search(r"\bmodifier\s*=\s*\{", idea_body)
        if mod_m:
            mod_body = extract_block(idea_body, mod_m.start())
            for mm in re.finditer(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)", mod_body):
                mrows.append([idea_key, mm.group(1), mm.group(2), filename])


def parse_land_oob_all() -> Tuple[int, int, int, int]:
    d = ROOT / "history" / "units"
    trows: List[List[str]] = []
    rrows: List[List[str]] = []
    srows: List[List[str]] = []
    drows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        name = fp.name.lower()
        if "_naval_" in name or "_air_" in name:
            continue
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for tm in re.finditer(r"division_template\s*=\s*\{([\s\S]*?)\n\}", txt):
            b = tm.group(1)
            nm = re.search(r"\bname\s*=\s*\"([^\"]+)\"", b)
            grp = re.search(r"division_names_group\s*=\s*([A-Za-z0-9_]+)", b)
            tname = nm.group(1) if nm else ""
            trows.append([tname, grp.group(1) if grp else "", fp.name])
            reg = re.search(r"regiments\s*=\s*\{([\s\S]*?)\n\s*\}", b)
            if reg:
                for rm in re.finditer(r"([a-zA-Z0-9_]+)\s*=\s*\{\s*x\s*=\s*([0-9]+)\s*y\s*=\s*([0-9]+)", reg.group(1)):
                    rrows.append([tname, rm.group(1), rm.group(2), rm.group(3), fp.name])
            sup = re.search(r"support\s*=\s*\{([\s\S]*?)\n\s*\}", b)
            if sup:
                for sm in re.finditer(r"([a-zA-Z0-9_]+)\s*=\s*\{\s*x\s*=\s*([0-9]+)\s*y\s*=\s*([0-9]+)\s*\}", sup.group(1)):
                    srows.append([tname, sm.group(1), sm.group(2), sm.group(3), fp.name])
        for dm in re.finditer(r"\bdivision\s*=\s*\{([\s\S]*?)\n\s*\}", txt):
            b = dm.group(1)
            loc = re.search(r"\blocation\s*=\s*([0-9]+)", b)
            tmp = re.search(r"division_template\s*=\s*\"([^\"]+)\"", b)
            exp = re.search(r"start_experience_factor\s*=\s*([0-9.]+)", b)
            drows.append([tmp.group(1) if tmp else "", loc.group(1) if loc else "", exp.group(1) if exp else "", fp.name])
    write_md(OUT / "division_templates_all.md", "Division Templates (All Land OOB Files)", ["template_name", "division_names_group", "source_file"], trows, "history/units/*.txt excluding _naval_/_air_")
    write_md(OUT / "division_template_regiments_all.md", "Division Template Regiments (All Land OOB Files)", ["template_name", "unit_type", "x", "y", "source_file"], rrows, "history/units/*.txt excluding _naval_/_air_")
    write_md(OUT / "division_template_support_all.md", "Division Template Support (All Land OOB Files)", ["template_name", "support_unit", "x", "y", "source_file"], srows, "history/units/*.txt excluding _naval_/_air_")
    write_md(OUT / "divisions_all.md", "Divisions (All Land OOB Files)", ["division_template", "location_province", "start_experience_factor", "source_file"], drows, "history/units/*.txt excluding _naval_/_air_")
    return len(trows), len(rrows), len(srows), len(drows)


def parse_unit_types_all() -> int:
    """Parse all sub_units definitions from common/units/*.txt."""
    d = ROOT / "common" / "units"
    rows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        wrapper_m = re.search(r"\bsub_units\s*=\s*\{", txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        for key, body, _ in find_top_level_blocks(wrapper_body):
            if key in {"type", "categories", "need", "forest", "mountain", "jungle",
                        "marsh", "urban", "river", "amphibious", "hills", "desert",
                        "plains", "fort", "ai_will_do", "snow", "OR", "AND", "NOT"}:
                continue
            group = re.search(r"\bgroup\s*=\s*([a-zA-Z0-9_]+)", body)
            cw = re.search(r"\bcombat_width\s*=\s*([0-9.]+)", body)
            ms = re.search(r"\bmax_strength\s*=\s*([0-9.]+)", body)
            mo = re.search(r"\bmax_organisation\s*=\s*([0-9.]+)", body)
            dm = re.search(r"\bdefault_morale\s*=\s*([0-9.]+)", body)
            mp = re.search(r"\bmanpower\s*=\s*([0-9]+)", body)
            tt = re.search(r"\btraining_time\s*=\s*([0-9]+)", body)
            supp = re.search(r"\bsuppression\s*=\s*([0-9.]+)", body)
            wt = re.search(r"\bweight\s*=\s*([0-9.]+)", body)
            sc = re.search(r"\bsupply_consumption\s*=\s*([0-9.]+)", body)
            abbr = re.search(r'\babbreviation\s*=\s*"([^"]+)"', body)
            rows.append([
                key,
                abbr.group(1) if abbr else "",
                group.group(1) if group else "",
                cw.group(1) if cw else "",
                ms.group(1) if ms else "",
                mo.group(1) if mo else "",
                dm.group(1) if dm else "",
                mp.group(1) if mp else "",
                tt.group(1) if tt else "",
                supp.group(1) if supp else "",
                wt.group(1) if wt else "",
                sc.group(1) if sc else "",
                fp.name,
            ])
    write_md(
        OUT / "unit_types_all.md", "Unit Types (All Files)",
        ["unit_type", "abbreviation", "group", "combat_width", "max_strength",
         "max_organisation", "default_morale", "manpower", "training_time",
         "suppression", "weight", "supply_consumption", "source_file"],
        rows, "common/units/*.txt",
    )
    return len(rows)


def parse_equipment_all() -> Tuple[int, int]:
    """Parse equipment archetypes and variants from common/units/equipment/*.txt."""
    d = ROOT / "common" / "units" / "equipment"
    equip_rows: List[List[str]] = []
    res_rows: List[List[str]] = []
    skip_keys = {"equipments", "modules", "upgrades", "resources", "type",
                 "interface_category", "group_by", "OR", "AND", "NOT", "IF",
                 "ELSE", "add_equipment_to_stockpile", "limit", "ai_will_do",
                 "module_slots", "default_modules", "module_count_limit",
                 "can_convert_from", "allowed_module_categories"}
    for fp in sorted(d.glob("*.txt")):
        if fp.name.startswith("_") or "filter" in fp.name.lower():
            continue
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        wrapper_m = re.search(r"\bequipments\s*=\s*\{", txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        for key, body, _ in find_top_level_blocks(wrapper_body):
            if key in skip_keys or key.startswith("@"):
                continue
            is_archetype = "is_archetype = yes" in body
            year = re.search(r"\byear\s*=\s*([0-9]+)", body)
            archetype = re.search(r"\barchetype\s*=\s*([a-zA-Z0-9_]+)", body)
            parent = re.search(r"\bparent\s*=\s*([a-zA-Z0-9_]+)", body)
            build_cost = re.search(r"\bbuild_cost_ic\s*=\s*([0-9.]+)", body)
            reliability = re.search(r"\breliability\s*=\s*([0-9.]+)", body)
            max_speed = re.search(r"\bmaximum_speed\s*=\s*([0-9.]+)", body)
            defense = re.search(r"\bdefense\s*=\s*([0-9.]+)", body)
            breakthrough = re.search(r"\bbreakthrough\s*=\s*([0-9.]+)", body)
            soft_attack = re.search(r"\bsoft_attack\s*=\s*([0-9.]+)", body)
            hard_attack = re.search(r"\bhard_attack\s*=\s*([0-9.]+)", body)
            ap_attack = re.search(r"\bap_attack\s*=\s*([0-9.]+)", body)
            air_attack = re.search(r"\bair_attack\s*=\s*([0-9.]+)", body)
            armor_value = re.search(r"\barmor_value\s*=\s*([0-9.]+)", body)
            hardness = re.search(r"\bhardness\s*=\s*([0-9.]+)", body)
            is_buildable = re.search(r"\bis_buildable\s*=\s*([a-z]+)", body)
            equip_rows.append([
                key,
                "yes" if is_archetype else "no",
                archetype.group(1) if archetype else "",
                parent.group(1) if parent else "",
                year.group(1) if year else "",
                build_cost.group(1) if build_cost else "",
                reliability.group(1) if reliability else "",
                max_speed.group(1) if max_speed else "",
                defense.group(1) if defense else "",
                breakthrough.group(1) if breakthrough else "",
                soft_attack.group(1) if soft_attack else "",
                hard_attack.group(1) if hard_attack else "",
                ap_attack.group(1) if ap_attack else "",
                air_attack.group(1) if air_attack else "",
                armor_value.group(1) if armor_value else "",
                hardness.group(1) if hardness else "",
                is_buildable.group(1) if is_buildable else "",
                fp.name,
            ])
            # Equipment resource costs
            res_m = re.search(r"\bresources\s*=\s*\{", body)
            if res_m:
                res_body = extract_block(body, res_m.start())
                for rm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9]+)", res_body):
                    res_rows.append([key, rm.group(1), rm.group(2), fp.name])

    write_md(
        OUT / "equipment_all.md", "Equipment Definitions (All Files)",
        ["equipment_key", "is_archetype", "archetype", "parent", "year", "build_cost_ic",
         "reliability", "max_speed", "defense", "breakthrough", "soft_attack",
         "hard_attack", "ap_attack", "air_attack", "armor_value", "hardness",
         "is_buildable", "source_file"],
        equip_rows, "common/units/equipment/*.txt",
    )
    write_md(
        OUT / "equipment_resources_all.md", "Equipment Resources (All Files)",
        ["equipment_key", "resource_key", "amount", "source_file"],
        res_rows, "common/units/equipment/*.txt",
    )
    return len(equip_rows), len(res_rows)


def parse_state_categories() -> int:
    """Extract distinct state_category values from all state files."""
    d = ROOT / "history" / "states"
    cats: set = set()
    for fp in sorted(d.glob("*.txt")):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"\bstate_category\s*=\s*([a-zA-Z0-9_]+)", txt):
            cats.add(m.group(1))
    rows = [[c] for c in sorted(cats)]
    write_md(OUT / "state_categories.md", "State Categories (distinct)", ["state_category"], rows, "history/states/*.txt")
    return len(rows)


def parse_terrain_types() -> int:
    """Extract distinct terrain values from map/definition.csv column 5."""
    p = ROOT / "map" / "definition.csv"
    terrains: set = set()
    if not p.exists():
        return 0
    with p.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            parts = raw.strip().split(";")
            if len(parts) >= 5 and parts[4]:
                terrains.add(parts[4])
    rows = [[t] for t in sorted(terrains)]
    write_md(OUT / "terrain_types.md", "Terrain Types (distinct)", ["terrain_type"], rows, "map/definition.csv")
    return len(rows)


# ═══════════════════════════════════════════════════════════════════════
# GAP FILLERS — tables that had no data dumps
# ═══════════════════════════════════════════════════════════════════════


def parse_state_history_extended() -> Tuple[int, int, int, int]:
    """Extract state_cores, state_ownership_history, province_buildings,
    and province_controller_history from history/states/*.txt."""
    states_dir = ROOT / "history" / "states"
    core_rows: List[List[str]] = []
    own_rows: List[List[str]] = []
    prov_bld_rows: List[List[str]] = []
    ctrl_rows: List[List[str]] = []

    for fp in sorted(states_dir.glob("*.txt")):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        sid_m = re.search(r"\bid\s*=\s*([0-9]+)", txt)
        if not sid_m:
            continue
        state_id = sid_m.group(1)
        base_date = "1936-01-01"

        # --- Top-level history block ---
        hist_m = re.search(r"\bhistory\s*=\s*\{", txt)
        if not hist_m:
            continue
        hist_body = extract_block(txt, hist_m.start())

        # owner at top level
        owner_m = re.search(r"\bowner\s*=\s*([A-Z0-9_]+)", hist_body)
        if owner_m:
            own_rows.append([state_id, base_date, owner_m.group(1), "", fp.name, ""])

        # add_core_of at top level
        for cm in re.finditer(r"\badd_core_of\s*=\s*([A-Z0-9_]+)", hist_body):
            core_rows.append([state_id, cm.group(1), base_date, fp.name, ""])

        # province-level buildings at top level
        bld_m = re.search(r"\bbuildings\s*=\s*\{", hist_body)
        if bld_m:
            bld_body = extract_block(hist_body, bld_m.start())
            for pb in re.finditer(r"\b([0-9]+)\s*=\s*\{([^{}]*)\}", bld_body, flags=re.S):
                prov_id = pb.group(1)
                for bm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9]+)", pb.group(2)):
                    prov_bld_rows.append([prov_id, state_id, bm.group(1), base_date,
                                          bm.group(2), fp.name, ""])

        # --- Dated history blocks ---
        for date_m in re.finditer(r"\b(\d{4}\.\d{1,2}\.\d{1,2})\s*=\s*\{", hist_body):
            ds = date_m.group(1)
            parts = ds.split(".")
            iso_date = f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
            date_body = extract_block(hist_body, date_m.start())

            # DLC guard
            dlc_m = re.search(r'has_dlc\s*=\s*"([^"]+)"', date_body)
            dlc = dlc_m.group(1) if dlc_m else ""

            # owner in dated block
            ow = re.search(r"\bowner\s*=\s*([A-Z0-9_]+)", date_body)
            ct = re.search(r"\bcontroller\s*=\s*([A-Z0-9_]+)", date_body)
            if ow:
                own_rows.append([state_id, iso_date, ow.group(1),
                                 ct.group(1) if ct else "", fp.name, dlc])
            elif ct:
                # controller change without ownership change → province_controller_history
                ctrl_rows.append(["", state_id, iso_date, ct.group(1), fp.name, dlc])

            # add_core_of in dated block
            for cm in re.finditer(r"\badd_core_of\s*=\s*([A-Z0-9_]+)", date_body):
                core_rows.append([state_id, cm.group(1), iso_date, fp.name, dlc])

            # province-level buildings in dated block
            dbld_m = re.search(r"\bbuildings\s*=\s*\{", date_body)
            if dbld_m:
                dbld_body = extract_block(date_body, dbld_m.start())
                for pb in re.finditer(r"\b([0-9]+)\s*=\s*\{([^{}]*)\}", dbld_body, flags=re.S):
                    prov_id = pb.group(1)
                    for bm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9]+)", pb.group(2)):
                        prov_bld_rows.append([prov_id, state_id, bm.group(1), iso_date,
                                              bm.group(2), fp.name, dlc])

    write_md(OUT / "state_cores.md", "State Cores",
        ["state_id", "country_tag", "effective_date", "source_file", "dlc_source"],
        core_rows, "history/states/*.txt")
    write_md(OUT / "state_ownership_history.md", "State Ownership History",
        ["state_id", "effective_date", "owner_tag", "controller_tag", "source_file", "dlc_source"],
        own_rows, "history/states/*.txt")
    write_md(OUT / "province_buildings.md", "Province Buildings",
        ["province_id", "state_id", "building_key", "effective_date", "level", "source_file", "dlc_source"],
        prov_bld_rows, "history/states/*.txt")
    write_md(OUT / "province_controller_history.md", "Province Controller History",
        ["province_id", "state_id", "effective_date", "controller_tag", "source_file", "dlc_source"],
        ctrl_rows, "history/states/*.txt")
    return len(core_rows), len(own_rows), len(prov_bld_rows), len(ctrl_rows)


def parse_technology_categories_all() -> Tuple[int, int]:
    """Extract technology_categories and technology_categories_junction from
    common/technologies/*.txt."""
    d = ROOT / "common" / "technologies"
    all_cats: set = set()
    junc_rows: List[List[str]] = []
    skip_keys = {"technologies", "folder", "path", "ai_will_do", "categories",
                 "on_research_complete", "on_research_complete_limit", "doctrine",
                 "sub_technologies", "OR", "AND", "NOT", "IF", "ELSE", "ELSE_IF",
                 "limit", "modifier", "available", "allow", "special_project_specialization"}
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        wrapper_m = re.search(r"\btechnologies\s*=\s*\{", txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        for key, body, _ in find_top_level_blocks(wrapper_body):
            if key in skip_keys or key.startswith("@"):
                continue
            cat_m = re.search(r"\bcategories\s*=\s*\{([^}]*)\}", body)
            if cat_m:
                cats = re.findall(r"\b([a-zA-Z0-9_]+)\b", cat_m.group(1))
                for c in cats:
                    all_cats.add(c)
                    junc_rows.append([key, c])

    cat_rows = [[c] for c in sorted(all_cats)]
    write_md(OUT / "technology_categories.md", "Technology Categories",
        ["category_key"], cat_rows, "common/technologies/*.txt")
    write_md(OUT / "technology_categories_junction.md", "Technology Categories Junction",
        ["technology_key", "category_key"], junc_rows, "common/technologies/*.txt")
    return len(cat_rows), len(junc_rows)


def parse_character_traits_all() -> Tuple[int, int]:
    """Extract character_traits and character_role_traits from
    common/characters/*.txt.

    character_role_traits uses (character_id, role_type, trait_key) as key
    because the schema uses character_role_id (SERIAL) which can't be
    resolved before DB load. We'll output character_id + role_type so
    the CSV load can resolve it.
    """
    d = ROOT / "common" / "characters"
    all_traits: set = set()
    role_trait_rows: List[List[str]] = []

    role_names = {"country_leader", "field_marshal", "corps_commander", "navy_leader", "advisor"}
    # trait_type hints from role context
    role_to_type = {
        "country_leader": "country_leader",
        "field_marshal": "field_marshal",
        "corps_commander": "corps_commander",
        "navy_leader": "navy_leader",
        "advisor": "advisor",
    }

    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for m in re.finditer(r"\n\s*([A-Z0-9_]+_[a-zA-Z0-9_]+)\s*=\s*\{", txt):
            cid = m.group(1)
            start = m.start()
            blk = extract_block(txt, start)
            if not blk:
                continue
            # Find each role sub-block and its traits
            for role_name in role_names:
                role_pos = 0
                while True:
                    rm = re.search(rf"\b{role_name}\s*=\s*\{{", blk[role_pos:])
                    if not rm:
                        break
                    role_body = extract_block(blk, role_pos + rm.start())
                    # Extract traits block within this role
                    traits_m = re.search(r"\btraits\s*=\s*\{([^}]*)\}", role_body)
                    if traits_m:
                        trait_keys = re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]+)\b", traits_m.group(1))
                        for tk in trait_keys:
                            all_traits.add((tk, role_to_type[role_name]))
                            role_trait_rows.append([cid, role_name, tk, fp.name])
                    role_pos = role_pos + rm.start() + len(role_body) + 2

    trait_rows = [[tk, tt] for tk, tt in sorted(all_traits)]
    write_md(OUT / "character_traits.md", "Character Traits",
        ["trait_key", "trait_type"], trait_rows, "common/characters/*.txt")
    write_md(OUT / "character_role_traits.md", "Character Role Traits",
        ["character_id", "role_type", "trait_key", "source_file"],
        role_trait_rows, "common/characters/*.txt")
    return len(trait_rows), len(role_trait_rows)


def parse_country_starting_ideas_all() -> int:
    """Extract country_starting_ideas from add_ideas blocks in
    history/countries/*.txt."""
    dirp = ROOT / "history" / "countries"
    rows: List[List[str]] = []
    for fp in sorted(dirp.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        tag_m = re.match(r"^([A-Z0-9]+)", fp.name)
        if not tag_m:
            continue
        tag = tag_m.group(1)

        # Process the whole file tracking date context
        current_date = "1936-01-01"
        depth = 0
        date_stack: List[str] = []
        current_dlc = ""
        dlc_stack: List[str] = []

        for line in txt.splitlines():
            stripped = line.strip()
            if not stripped:
                continue

            # Track date blocks
            date_bm = re.match(r'(\d{4}\.\d{1,2}\.\d{1,2})\s*=\s*\{', stripped)
            if date_bm:
                ds = date_bm.group(1)
                parts = ds.split(".")
                date_stack.append(current_date)
                current_date = f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
                depth += 1
                continue

            # DLC guard
            dlc_m = re.search(r'has_dlc\s*=\s*"([^"]+)"', stripped)
            if dlc_m:
                current_dlc = dlc_m.group(1)

            # Track brace depth
            opens = stripped.count("{")
            closes = stripped.count("}")
            if date_stack:
                depth += opens - closes
                if depth <= 0:
                    current_date = date_stack.pop()
                    depth = 0

            # Look for add_ideas blocks (both inline and multi-line)
        # Re-parse using regex for add_ideas blocks
        for aim in re.finditer(r"add_ideas\s*=\s*\{([^}]*)\}", txt, flags=re.S):
            ideas_body = aim.group(1)
            # Determine date context by looking at what date block this is in
            block_start = aim.start()
            # Find the enclosing date block
            eff_date = "1936-01-01"
            for dm in re.finditer(r"(\d{4}\.\d{1,2}\.\d{1,2})\s*=\s*\{", txt):
                if dm.start() < block_start:
                    d_body = extract_block(txt, dm.start())
                    if dm.start() + len(d_body) + 2 > block_start:
                        ds = dm.group(1).split(".")
                        eff_date = f"{ds[0]}-{ds[1].zfill(2)}-{ds[2].zfill(2)}"
                        break

            # DLC context
            dlc_ctx = ""
            # Look backwards from the add_ideas block for has_dlc
            preceding = txt[max(0, block_start - 500):block_start]
            dlc_near = re.findall(r'has_dlc\s*=\s*"([^"]+)"', preceding)
            if dlc_near:
                dlc_ctx = dlc_near[-1]

            for idea in re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]+)\b", ideas_body):
                rows.append([tag, idea, eff_date, fp.name, dlc_ctx])

    write_md(OUT / "country_starting_ideas.md", "Country Starting Ideas",
        ["country_tag", "idea_key", "effective_date", "source_file", "dlc_source"],
        rows, "history/countries/*.txt")
    return len(rows)


def parse_equipment_variants_all() -> int:
    """Extract equipment_variants from create_equipment_variant blocks in
    history/countries/*.txt."""
    dirp = ROOT / "history" / "countries"
    rows: List[List[str]] = []
    for fp in sorted(dirp.glob("*.txt")):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        tag_m = re.match(r"^([A-Z0-9]+)", fp.name)
        if not tag_m:
            continue
        tag = tag_m.group(1)

        pos = 0
        while True:
            m = re.search(r"\bcreate_equipment_variant\s*=\s*\{", txt[pos:])
            if not m:
                break
            body = extract_block(txt, pos + m.start())
            name = re.search(r'\bname\s*=\s*"([^"]+)"', body)
            eq_type = re.search(r"\btype\s*=\s*([a-zA-Z0-9_]+)", body)
            rows.append([
                tag,
                eq_type.group(1) if eq_type else "",
                name.group(1) if name else "",
                fp.name,
            ])
            pos = pos + m.start() + len(body) + 2

    write_md(OUT / "equipment_variants.md", "Equipment Variants",
        ["owner_tag", "base_equipment_key", "version_name", "source_file"],
        rows, "history/countries/*.txt")
    return len(rows)


def parse_mio_traits_all() -> Tuple[int, int, int, int]:
    """Extract mio_traits, mio_trait_bonuses, mio_trait_prerequisites,
    and mio_trait_exclusions from MIO organization/template files."""
    d = ROOT / "common" / "military_industrial_organization" / "organizations"
    trait_rows: List[List[str]] = []
    bonus_rows: List[List[str]] = []
    prereq_rows: List[List[str]] = []
    excl_set: set = set()
    if not d.exists():
        return 0, 0, 0, 0

    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for owner_key, owner_body, _ in find_top_level_blocks(txt):
            # Determine owner_type
            include = re.search(r"\binclude\s*=\s*([a-zA-Z0-9_]+)", owner_body)
            owner_type = "organization" if include else "template"

            # Process trait blocks: trait = { }, add_trait = { }, override_trait = { }
            for trait_type_label in ("trait", "add_trait", "override_trait"):
                t_pos = 0
                while True:
                    tm = re.search(rf"\b{trait_type_label}\s*=\s*\{{", owner_body[t_pos:])
                    if not tm:
                        break
                    t_body = extract_block(owner_body, t_pos + tm.start())

                    token = re.search(r"\btoken\s*=\s*([a-zA-Z0-9_]+)", t_body)
                    name = re.search(r"\bname\s*=\s*([a-zA-Z0-9_]+)", t_body)
                    icon = re.search(r"\bicon\s*=\s*(\S+)", t_body)
                    special = "yes" if "special_trait_background = yes" in t_body else ""
                    pos_m = re.search(r"\bposition\s*=\s*\{\s*x\s*=\s*([0-9]+)\s*y\s*=\s*([0-9]+)", t_body)
                    rel_pos = re.search(r"\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)", t_body)
                    token_val = token.group(1) if token else ""

                    if not token_val:
                        t_pos = t_pos + tm.start() + len(t_body) + 2
                        continue

                    trait_rows.append([
                        token_val,
                        owner_key,
                        owner_type,
                        trait_type_label,
                        name.group(1) if name else "",
                        icon.group(1) if icon else "",
                        special,
                        pos_m.group(1) if pos_m else "",
                        pos_m.group(2) if pos_m else "",
                        rel_pos.group(1) if rel_pos else "",
                    ])

                    # Bonuses: equipment_bonus, production_bonus, organization_modifier
                    for cat in ("equipment_bonus", "production_bonus", "organization_modifier"):
                        bm = re.search(rf"\b{cat}\s*=\s*\{{", t_body)
                        if bm:
                            bb = extract_block(t_body, bm.start())
                            for mm in re.finditer(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)", bb):
                                bonus_rows.append([token_val, cat, mm.group(1), mm.group(2)])

                    # Prerequisites: all_parents, any_parent
                    for req_type in ("all_parents", "any_parent"):
                        pm = re.search(rf"\b{req_type}\s*=\s*\{{([^}}]*)\}}", t_body)
                        if pm:
                            parents = re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]+)\b", pm.group(1))
                            for p in parents:
                                prereq_rows.append([token_val, p, req_type.rstrip("s")])

                    # Mutual exclusions
                    me_m = re.search(r"\bmutually_exclusive\s*=\s*\{([^}]*)\}", t_body)
                    if me_m:
                        excls = re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]+)\b", me_m.group(1))
                        for e in excls:
                            pair = tuple(sorted([token_val, e]))
                            excl_set.add(pair)

                    t_pos = t_pos + tm.start() + len(t_body) + 2

    excl_rows = [[a, b] for a, b in sorted(excl_set)]

    write_md(OUT / "mio_traits.md", "MIO Traits",
        ["trait_token", "owner_key", "owner_type", "trait_type", "name", "icon",
         "special_trait_background", "position_x", "position_y", "relative_position_id"],
        trait_rows, "common/military_industrial_organization/organizations/*.txt")
    write_md(OUT / "mio_trait_bonuses.md", "MIO Trait Bonuses",
        ["trait_token", "bonus_category", "bonus_key", "bonus_value"],
        bonus_rows, "common/military_industrial_organization/organizations/*.txt")
    write_md(OUT / "mio_trait_prerequisites.md", "MIO Trait Prerequisites",
        ["trait_token", "parent_token", "requirement_type"],
        prereq_rows, "common/military_industrial_organization/organizations/*.txt")
    write_md(OUT / "mio_trait_exclusions.md", "MIO Trait Exclusions",
        ["trait_token_a", "trait_token_b"],
        excl_rows, "common/military_industrial_organization/organizations/*.txt")
    return len(trait_rows), len(bonus_rows), len(prereq_rows), len(excl_rows)


def parse_terrain_extended() -> Tuple[int, int]:
    """Extract terrain_building_limits and terrain_combat_modifiers from
    common/terrain/00_terrain.txt."""
    p = ROOT / "common" / "terrain" / "00_terrain.txt"
    bld_rows: List[List[str]] = []
    mod_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0

    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    # Parse the categories = { } wrapper
    cat_m = re.search(r"\bcategories\s*=\s*\{", txt)
    if not cat_m:
        return 0, 0
    cat_body = extract_block(txt, cat_m.start())

    for terrain_key, terrain_body, _ in find_top_level_blocks(cat_body):
        # buildings_max_level block → terrain_building_limits
        blm = re.search(r"\bbuildings_max_level\s*=\s*\{", terrain_body)
        if blm:
            bl_body = extract_block(terrain_body, blm.start())
            for bm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9]+)", bl_body):
                bld_rows.append([terrain_key, bm.group(1), bm.group(2)])

        # units block → terrain_combat_modifiers
        um = re.search(r"\bunits\s*=\s*\{", terrain_body)
        if um:
            u_body = extract_block(terrain_body, um.start())
            # Top-level key=value pairs are generic (no unit_class)
            for mm in re.finditer(r"\b([a-zA-Z_]+)\s*=\s*([0-9.\-]+)", u_body):
                mod_rows.append([terrain_key, "", mm.group(1), mm.group(2)])

    write_md(OUT / "terrain_building_limits.md", "Terrain Building Limits",
        ["terrain_type", "building_key", "max_level"],
        bld_rows, "common/terrain/00_terrain.txt")
    write_md(OUT / "terrain_combat_modifiers.md", "Terrain Combat Modifiers",
        ["terrain_type", "unit_class", "modifier_key", "modifier_value"],
        mod_rows, "common/terrain/00_terrain.txt")
    return len(bld_rows), len(mod_rows)


# ═══════════════════════════════════════════════════════════════════════
# DLC PARSERS — Phases 11–22
# ═══════════════════════════════════════════════════════════════════════


def _resolve_at_vars(text: str) -> str:
    """Replace @var references with their defined values."""
    defs: Dict[str, str] = {}
    for m in re.finditer(r"^@(\w+)\s*=\s*(\S+)", text, flags=re.M):
        defs[m.group(1)] = m.group(2)
    if not defs:
        return text
    def _sub(m: re.Match) -> str:
        return defs.get(m.group(1), m.group(0))
    return re.sub(r"@(\w+)", _sub, text)


# ── Phase 11: Map Connectivity ──────────────────────────────────────────

def parse_province_adjacencies() -> int:
    p = ROOT / "map" / "adjacencies.csv"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    with p.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or line.startswith("From"):
                continue
            parts = line.split(";")
            if len(parts) < 10:
                continue
            if parts[0] == "-1":
                continue
            rows.append(parts[:10])
    write_md(
        OUT / "province_adjacencies.md", "Province Adjacencies",
        ["from_province_id", "to_province_id", "adjacency_type", "through_province_id",
         "start_x", "start_y", "stop_x", "stop_y", "adjacency_rule_name", "comment"],
        rows, "map/adjacencies.csv",
    )
    return len(rows)


def parse_province_railways() -> int:
    p = ROOT / "map" / "railways.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = ln.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        level = parts[0]
        # parts[1] = count, rest are province chain
        provs = parts[2:]
        for i in range(len(provs) - 1):
            rows.append([provs[i], provs[i + 1], level])
    write_md(
        OUT / "province_railways.md", "Province Railways",
        ["from_province_id", "to_province_id", "railway_level"],
        rows, "map/railways.txt",
    )
    return len(rows)


# ── Phase 12: Governance ────────────────────────────────────────────────

def parse_autonomy_states_all() -> Tuple[int, int]:
    d = ROOT / "common" / "autonomous_states"
    state_rows: List[List[str]] = []
    mod_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        m = re.search(r"\bautonomy_state\s*=\s*\{", txt)
        if not m:
            continue
        body = extract_block(txt, m.start())
        aid = re.search(r"\bid\s*=\s*([a-zA-Z0-9_]+)", body)
        if not aid:
            continue
        key = aid.group(1)
        is_puppet = re.search(r"\bis_puppet\s*=\s*(yes|no)", body)
        is_default = re.search(r"\bdefault\s*=\s*(yes|no)", body)
        min_free = re.search(r"\bmin_freedom_level\s*=\s*([0-9.]+)", body)
        mp_inf = re.search(r"\bmanpower_influence\s*=\s*([0-9.]+)", body)
        # DLC source from allowed block
        dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
        state_rows.append([
            key,
            is_puppet.group(1) if is_puppet else "",
            is_default.group(1) if is_default else "",
            min_free.group(1) if min_free else "",
            mp_inf.group(1) if mp_inf else "",
            dlc.group(1) if dlc else "",
            fp.name,
        ])
        # modifier block
        mod_m = re.search(r"\bmodifier\s*=\s*\{", body)
        if mod_m:
            mod_body = extract_block(body, mod_m.start())
            for mm in re.finditer(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)", mod_body):
                mod_rows.append([key, mm.group(1), mm.group(2)])
    write_md(
        OUT / "autonomy_states.md", "Autonomy States",
        ["autonomy_key", "is_puppet", "is_default", "min_freedom_level", "manpower_influence", "dlc_source", "source_file"],
        state_rows, "common/autonomous_states/*.txt",
    )
    write_md(
        OUT / "autonomy_state_modifiers.md", "Autonomy State Modifiers",
        ["autonomy_key", "modifier_key", "modifier_value"],
        mod_rows, "common/autonomous_states/*.txt",
    )
    return len(state_rows), len(mod_rows)


def parse_occupation_laws_all() -> Tuple[int, int]:
    p = ROOT / "common" / "occupation_laws" / "occupation_laws.txt"
    law_rows: List[List[str]] = []
    mod_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    for key, body, _ in find_top_level_blocks(txt):
        if key in {"tooltip", "visible", "available", "ai_will_do"}:
            continue
        icon = re.search(r"\bicon\s*=\s*(\S+)", body)
        sound = re.search(r"\bsound_effect\s*=\s*(\S+)", body)
        gui = re.search(r"\bgui_order\s*=\s*([0-9]+)", body)
        fallback_main = "yes" if "main_fallback_law = yes" in body else "no"
        fallback = re.search(r"\bfallback_law\s*=\s*([a-zA-Z0-9_]+)", body)
        law_rows.append([
            key,
            icon.group(1) if icon else "",
            sound.group(1) if sound else "",
            gui.group(1) if gui else "",
            fallback_main,
            fallback.group(1) if fallback else "",
        ])
        # state_modifier and suppressed_state_modifier
        for is_suppressed, block_name in [("no", "state_modifier"), ("yes", "suppressed_state_modifier")]:
            bm = re.search(rf"\b{block_name}\s*=\s*\{{", body)
            if bm:
                mb = extract_block(body, bm.start())
                for mm in re.finditer(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)", mb):
                    mod_rows.append([key, mm.group(1), mm.group(2), is_suppressed])
    write_md(
        OUT / "occupation_laws.md", "Occupation Laws",
        ["occupation_law_key", "icon", "sound_effect", "gui_order", "main_fallback_law", "fallback_law_key"],
        law_rows, "common/occupation_laws/occupation_laws.txt",
    )
    write_md(
        OUT / "occupation_law_modifiers.md", "Occupation Law Modifiers",
        ["occupation_law_key", "modifier_key", "modifier_value", "is_suppressed"],
        mod_rows, "common/occupation_laws/occupation_laws.txt",
    )
    return len(law_rows), len(mod_rows)


# ── Phase 14: Bookmarks ─────────────────────────────────────────────────

def parse_bookmarks_all() -> Tuple[int, int]:
    d = ROOT / "common" / "bookmarks"
    bm_rows: List[List[str]] = []
    bc_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # bookmarks = { bookmark = { ... } }
        outer_m = re.search(r"\bbookmarks\s*=\s*\{", txt)
        if not outer_m:
            continue
        outer_body = extract_block(txt, outer_m.start())
        # find bookmark = { ... } blocks inside
        bm_m = re.search(r"\bbookmark\s*=\s*\{", outer_body)
        if not bm_m:
            continue
        bm_body = extract_block(outer_body, bm_m.start())
        name = re.search(r'\bname\s*=\s*"([^"]+)"', bm_body)
        desc = re.search(r'\bdesc\s*=\s*"([^"]+)"', bm_body)
        date = re.search(r'\bdate\s*=\s*"?([0-9.]+)"?', bm_body)
        pic = re.search(r'\bpicture\s*=\s*"?([^"\s]+)"?', bm_body)
        default_c = re.search(r'\bdefault_country\s*=\s*"?([A-Z0-9_]+)"?', bm_body)
        is_default = "yes" if re.search(r'\bdefault\s*=\s*yes', bm_body) else "no"
        bm_rows.append([
            name.group(1) if name else "",
            date.group(1) if date else "",
            pic.group(1) if pic else "",
            default_c.group(1) if default_c else "",
            is_default,
            fp.name,
        ])
        # country entries: "TAG" = { ... } — quoted tags
        for cm in re.finditer(r'"([A-Z0-9_]+)"\s*=\s*\{', bm_body):
            tag = cm.group(1)
            c_body = extract_block(bm_body, cm.start())
            ide = re.search(r'\bideology\s*=\s*([a-zA-Z0-9_]+)', c_body)
            bc_rows.append([
                name.group(1) if name else "",
                tag,
                ide.group(1) if ide else "",
                fp.name,
            ])
    write_md(
        OUT / "bookmarks.md", "Bookmarks",
        ["bookmark_name", "bookmark_date", "picture_gfx", "default_country_tag", "is_default", "source_file"],
        bm_rows, "common/bookmarks/*.txt",
    )
    write_md(
        OUT / "bookmark_countries.md", "Bookmark Countries",
        ["bookmark_name", "country_tag", "ideology_key", "source_file"],
        bc_rows, "common/bookmarks/*.txt",
    )
    return len(bm_rows), len(bc_rows)


# ── Phase 15: Decisions ──────────────────────────────────────────────────

def parse_decision_categories_all() -> int:
    d = ROOT / "common" / "decisions" / "categories"
    rows: List[List[str]] = []
    if not d.exists():
        return 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            pic = re.search(r'\bpicture\s*=\s*(\S+)', body)
            pri = re.search(r'\bpriority\s*=\s*([0-9]+)', body)
            rows.append([key, icon.group(1) if icon else "", pic.group(1) if pic else "", pri.group(1) if pri else "", fp.name])
    write_md(
        OUT / "decision_categories.md", "Decision Categories",
        ["category_key", "icon", "picture_gfx", "priority", "source_file"],
        rows, "common/decisions/categories/*.txt",
    )
    return len(rows)


def parse_decisions_all() -> int:
    d = ROOT / "common" / "decisions"
    rows: List[List[str]] = []
    if not d.exists():
        return 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # top-level blocks are category wrappers
        for cat_key, cat_body, _ in find_top_level_blocks(txt):
            # inside each category, find decision entries
            for dec_key, dec_body, _ in find_top_level_blocks(cat_body):
                if dec_key in {"icon", "picture", "visible", "allowed", "available",
                               "priority", "ai_will_do", "highlight_states", "on_map_mode"}:
                    continue
                icon = re.search(r'\bicon\s*=\s*(\S+)', dec_body)
                cost = re.search(r'\bcost\s*=\s*([0-9]+)', dec_body)
                fire = "yes" if "fire_only_once = yes" in dec_body else ""
                dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', dec_body)
                rows.append([dec_key, cat_key, icon.group(1) if icon else "", cost.group(1) if cost else "", fire, dlc.group(1) if dlc else "", fp.name])
    write_md(
        OUT / "decisions_all.md", "Decisions (All Files)",
        ["decision_key", "category_key", "icon", "cost", "fire_only_once", "dlc_source", "source_file"],
        rows, "common/decisions/*.txt",
    )
    return len(rows)


# ── Phase 16: Espionage (La Résistance) ─────────────────────────────────

def parse_operation_tokens_all() -> int:
    d = ROOT / "common" / "operation_tokens"
    rows: List[List[str]] = []
    if not d.exists():
        return 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            name = re.search(r'\bname\s*=\s*(\S+)', body)
            desc = re.search(r'\bdesc\s*=\s*(\S+)', body)
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            text_icon = re.search(r'\btext_icon\s*=\s*(\S+)', body)
            intel_src = re.search(r'\bintel_source\s*=\s*(\S+)', body)
            intel_gain = re.search(r'\bintel_gain\s*=\s*([0-9]+)', body)
            rows.append([key, name.group(1) if name else "", desc.group(1) if desc else "", icon.group(1) if icon else "", text_icon.group(1) if text_icon else "", intel_src.group(1) if intel_src else "", intel_gain.group(1) if intel_gain else "", fp.name])
    write_md(
        OUT / "operation_tokens.md", "Operation Tokens",
        ["token_key", "name", "desc", "icon", "text_icon", "intel_source", "intel_gain", "source_file"],
        rows, "common/operation_tokens/*.txt",
    )
    return len(rows)


def parse_operation_phase_definitions_all() -> Tuple[int, int]:
    d = ROOT / "common" / "operation_phases"
    phase_rows: List[List[str]] = []
    equip_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            name = re.search(r'\bname\s*=\s*(\S+)', body)
            desc = re.search(r'\bdesc\s*=\s*(\S+)', body)
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            pic = re.search(r'\bpicture\s*=\s*(\S+)', body)
            ret = "yes" if "return_on_complete = yes" in body else ""
            phase_rows.append([key, name.group(1) if name else "", desc.group(1) if desc else "", icon.group(1) if icon else "", pic.group(1) if pic else "", ret, fp.name])
            # equipment block
            eq_m = re.search(r'\bequipment\s*=\s*\{', body)
            if eq_m:
                eq_body = extract_block(body, eq_m.start())
                for em in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9]+)', eq_body):
                    equip_rows.append([key, em.group(1), em.group(2)])
    write_md(
        OUT / "operation_phase_definitions.md", "Operation Phase Definitions",
        ["phase_key", "name", "desc", "icon", "picture", "return_on_complete", "source_file"],
        phase_rows, "common/operation_phases/*.txt",
    )
    write_md(
        OUT / "operation_phase_equipment.md", "Operation Phase Equipment",
        ["phase_key", "equipment_key", "amount"],
        equip_rows, "common/operation_phases/*.txt",
    )
    return len(phase_rows), len(equip_rows)


def parse_operations_all() -> Tuple[int, int, int, int, int]:
    d = ROOT / "common" / "operations"
    op_rows: List[List[str]] = []
    token_rows: List[List[str]] = []
    equip_rows: List[List[str]] = []
    pg_rows: List[List[str]] = []
    po_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0, 0, 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            if key in {"tooltip", "visible", "available", "ai_will_do", "OR", "AND", "NOT"}:
                continue
            name = re.search(r'\bname\s*=\s*(\S+)', body)
            desc = re.search(r'\bdesc\s*=\s*(\S+)', body)
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            priority = re.search(r'\bpriority\s*=\s*([0-9]+)', body)
            days = re.search(r'\bdays\s*=\s*([0-9]+)', body)
            net = re.search(r'\bnetwork_strength\s*=\s*([0-9]+)', body)
            ops = re.search(r'\boperatives\s*=\s*([0-9]+)', body)
            risk = re.search(r'\brisk_chance\s*=\s*([0-9.]+)', body)
            exp = re.search(r'\bexperience\s*=\s*([0-9.]+)', body)
            cost_m = re.search(r'\bcost_multiplier\s*=\s*([0-9.]+)', body)
            out_extra = re.search(r'\boutcome_extra_chance\s*=\s*([0-9.]+)', body)
            prevent = "yes" if "prevent_captured_operative_to_die = yes" in body else ""
            scale = "yes" if "scale_cost_independent_of_target = yes" in body else ""
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            op_rows.append([
                key,
                name.group(1) if name else "",
                desc.group(1) if desc else "",
                icon.group(1) if icon else "",
                priority.group(1) if priority else "",
                days.group(1) if days else "",
                net.group(1) if net else "",
                ops.group(1) if ops else "",
                risk.group(1) if risk else "",
                exp.group(1) if exp else "",
                cost_m.group(1) if cost_m else "",
                out_extra.group(1) if out_extra else "",
                prevent,
                scale,
                dlc.group(1) if dlc else "",
                fp.name,
            ])
            # awarded_tokens
            at_m = re.search(r'\bawarded_tokens\s*=\s*\{', body)
            if at_m:
                at_body = extract_block(body, at_m.start())
                for tk in re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]+)\b', at_body):
                    token_rows.append([key, tk])
            # equipment
            eq_m = re.search(r'\bequipment\s*=\s*\{', body)
            if eq_m:
                eq_body = extract_block(body, eq_m.start())
                for em in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9]+)', eq_body):
                    equip_rows.append([key, em.group(1), em.group(2)])
            # phases blocks (multiple)
            seq = 0
            pos = 0
            while True:
                pm = re.search(r'\bphases\s*=\s*\{', body[pos:])
                if not pm:
                    break
                seq += 1
                p_body = extract_block(body, pos + pm.start())
                pg_rows.append([key, str(seq)])
                # phase options inside
                for ph_key, ph_body, _ in find_top_level_blocks(p_body):
                    base_w = re.search(r'\bbase\s*=\s*([0-9]+)', ph_body)
                    po_rows.append([key, str(seq), ph_key, base_w.group(1) if base_w else ""])
                pos = pos + pm.start() + len(p_body) + 2
    write_md(OUT / "operations.md", "Operations",
        ["operation_key", "name", "desc", "icon", "priority", "days", "network_strength", "operatives", "risk_chance", "experience", "cost_multiplier", "outcome_extra_chance", "prevent_captured_operative_to_die", "scale_cost_independent_of_target", "dlc_source", "source_file"],
        op_rows, "common/operations/*.txt")
    write_md(OUT / "operation_awarded_tokens.md", "Operation Awarded Tokens",
        ["operation_key", "token_key"], token_rows, "common/operations/*.txt")
    write_md(OUT / "operation_equipment_requirements.md", "Operation Equipment Requirements",
        ["operation_key", "equipment_key", "amount"], equip_rows, "common/operations/*.txt")
    write_md(OUT / "operation_phase_groups.md", "Operation Phase Groups",
        ["operation_key", "sequence_index"], pg_rows, "common/operations/*.txt")
    write_md(OUT / "operation_phase_options.md", "Operation Phase Options",
        ["operation_key", "sequence_index", "phase_key", "base_weight"], po_rows, "common/operations/*.txt")
    return len(op_rows), len(token_rows), len(equip_rows), len(pg_rows), len(po_rows)


def parse_intelligence_agencies_all() -> Tuple[int, int]:
    d = ROOT / "common" / "intelligence_agencies"
    ag_rows: List[List[str]] = []
    name_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # repeated intelligence_agency = { } blocks
        pos = 0
        while True:
            m = re.search(r'\bintelligence_agency\s*=\s*\{', txt[pos:])
            if not m:
                break
            body = extract_block(txt, pos + m.start())
            pic = re.search(r'\bpicture\s*=\s*(\S+)', body)
            # default block may contain tag
            def_m = re.search(r'\bdefault\s*=\s*\{', body)
            def_tag = ""
            if def_m:
                def_body = extract_block(body, def_m.start())
                tag_m = re.search(r'\btag\s*=\s*([A-Z0-9_]+)', def_body)
                if tag_m:
                    def_tag = tag_m.group(1)
            # available block may contain original_tag
            avail_m = re.search(r'\bavailable\s*=\s*\{', body)
            avail_tag = ""
            if avail_m:
                avail_body = extract_block(body, avail_m.start())
                otag_m = re.search(r'\boriginal_tag\s*=\s*([A-Z0-9_]+)', avail_body)
                if otag_m:
                    avail_tag = otag_m.group(1)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            ag_idx = len(ag_rows) + 1
            ag_rows.append([str(ag_idx), pic.group(1) if pic else "", def_tag, avail_tag, dlc.group(1) if dlc else "", fp.name])
            # names
            names_m = re.search(r'\bnames\s*=\s*\{', body)
            if names_m:
                names_body = extract_block(body, names_m.start())
                for nm in re.findall(r'"([^"]+)"', names_body):
                    name_rows.append([str(ag_idx), nm])
            pos = pos + m.start() + len(body) + 2
    write_md(OUT / "intelligence_agencies.md", "Intelligence Agencies",
        ["agency_id", "picture_gfx", "default_tag", "available_tag", "dlc_source", "source_file"],
        ag_rows, "common/intelligence_agencies/*.txt")
    write_md(OUT / "intelligence_agency_names.md", "Intelligence Agency Names",
        ["agency_id", "name"], name_rows, "common/intelligence_agencies/*.txt")
    return len(ag_rows), len(name_rows)


def parse_intel_agency_upgrades_all() -> Tuple[int, int, int, int]:
    d = ROOT / "common" / "intelligence_agency_upgrades"
    branch_rows: List[List[str]] = []
    upgrade_rows: List[List[str]] = []
    level_rows: List[List[str]] = []
    prog_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0, 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for branch_key, branch_body, _ in find_top_level_blocks(txt):
            if not branch_key.startswith("branch_"):
                continue
            branch_rows.append([branch_key])
            for up_key, up_body, _ in find_top_level_blocks(branch_body):
                if up_key in {"ai_will_do"}:
                    continue
                pic = re.search(r'\bpicture\s*=\s*(\S+)', up_body)
                frame = re.search(r'\bframe\s*=\s*(\S+)', up_body)
                sound = re.search(r'\bsound\s*=\s*(\S+)', up_body)
                upgrade_rows.append([up_key, branch_key, pic.group(1) if pic else "", frame.group(1) if frame else "", sound.group(1) if sound else ""])
                # modifiers_during_progress
                prog_m = re.search(r'\bmodifiers_during_progress\s*=\s*\{', up_body)
                if prog_m:
                    prog_body = extract_block(up_body, prog_m.start())
                    for pm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', prog_body):
                        prog_rows.append([up_key, pm.group(1), pm.group(2)])
                # levels
                lev_idx = 0
                lev_pos = 0
                while True:
                    lm = re.search(r'\blevel\s*=\s*\{', up_body[lev_pos:])
                    if not lm:
                        break
                    lev_idx += 1
                    lev_body = extract_block(up_body, lev_pos + lm.start())
                    mod_m = re.search(r'\bmodifier\s*=\s*\{', lev_body)
                    if mod_m:
                        mod_body = extract_block(lev_body, mod_m.start())
                        for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', mod_body):
                            level_rows.append([up_key, str(lev_idx), mm.group(1), mm.group(2)])
                    lev_pos = lev_pos + lm.start() + len(lev_body) + 2
    write_md(OUT / "intel_agency_upgrade_branches.md", "Intel Agency Upgrade Branches",
        ["branch_key"], branch_rows, "common/intelligence_agency_upgrades/*.txt")
    write_md(OUT / "intel_agency_upgrades.md", "Intel Agency Upgrades",
        ["upgrade_key", "branch_key", "picture", "frame", "sound"],
        upgrade_rows, "common/intelligence_agency_upgrades/*.txt")
    write_md(OUT / "intel_agency_upgrade_levels.md", "Intel Agency Upgrade Levels",
        ["upgrade_key", "level_index", "modifier_key", "modifier_value"],
        level_rows, "common/intelligence_agency_upgrades/*.txt")
    write_md(OUT / "intel_agency_upgrade_progress_modifiers.md", "Intel Agency Upgrade Progress Modifiers",
        ["upgrade_key", "modifier_key", "modifier_value"],
        prog_rows, "common/intelligence_agency_upgrades/*.txt")
    return len(branch_rows), len(upgrade_rows), len(level_rows), len(prog_rows)


# ── Phase 17: Occupation & Resistance ────────────────────────────────────

def parse_compliance_modifiers_all() -> Tuple[int, int]:
    p = ROOT / "common" / "resistance_compliance_modifiers" / "compliance_modifiers.txt"
    mod_rows: List[List[str]] = []
    eff_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    for key, body, _ in find_top_level_blocks(txt):
        typ = re.search(r'\btype\s*=\s*(\S+)', body)
        icon = re.search(r'\bicon\s*=\s*(\S+)', body)
        small = re.search(r'\bsmall_icon\s*=\s*(\S+)', body)
        thresh = re.search(r'\bthreshold\s*=\s*([0-9]+)', body)
        margin = re.search(r'\bmargin\s*=\s*([0-9]+)', body)
        dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
        mod_rows.append([key, typ.group(1) if typ else "", icon.group(1) if icon else "", small.group(1) if small else "", thresh.group(1) if thresh else "", margin.group(1) if margin else "", dlc.group(1) if dlc else ""])
        sm = re.search(r'\bstate_modifier\s*=\s*\{', body)
        if sm:
            sb = extract_block(body, sm.start())
            for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', sb):
                eff_rows.append([key, mm.group(1), mm.group(2)])
    write_md(OUT / "compliance_modifiers.md", "Compliance Modifiers",
        ["modifier_key", "type", "icon", "small_icon", "threshold", "margin", "dlc_source"],
        mod_rows, "common/resistance_compliance_modifiers/compliance_modifiers.txt")
    write_md(OUT / "compliance_modifier_effects.md", "Compliance Modifier Effects",
        ["modifier_key", "effect_key", "effect_value"],
        eff_rows, "common/resistance_compliance_modifiers/compliance_modifiers.txt")
    return len(mod_rows), len(eff_rows)


def parse_resistance_modifiers_all() -> Tuple[int, int]:
    p = ROOT / "common" / "resistance_compliance_modifiers" / "resistance_modifiers.txt"
    mod_rows: List[List[str]] = []
    eff_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    for key, body, _ in find_top_level_blocks(txt):
        typ = re.search(r'\btype\s*=\s*(\S+)', body)
        icon = re.search(r'\bicon\s*=\s*(\S+)', body)
        small = re.search(r'\bsmall_icon\s*=\s*(\S+)', body)
        thresh = re.search(r'\bthreshold\s*=\s*([0-9]+)', body)
        margin = re.search(r'\bmargin\s*=\s*([0-9]+)', body)
        mod_rows.append([key, typ.group(1) if typ else "", icon.group(1) if icon else "", small.group(1) if small else "", thresh.group(1) if thresh else "", margin.group(1) if margin else ""])
        sm = re.search(r'\bstate_modifier\s*=\s*\{', body)
        if sm:
            sb = extract_block(body, sm.start())
            for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', sb):
                eff_rows.append([key, mm.group(1), mm.group(2)])
    write_md(OUT / "resistance_modifiers.md", "Resistance Modifiers",
        ["modifier_key", "type", "icon", "small_icon", "threshold", "margin"],
        mod_rows, "common/resistance_compliance_modifiers/resistance_modifiers.txt")
    write_md(OUT / "resistance_modifier_effects.md", "Resistance Modifier Effects",
        ["modifier_key", "effect_key", "effect_value"],
        eff_rows, "common/resistance_compliance_modifiers/resistance_modifiers.txt")
    return len(mod_rows), len(eff_rows)


def parse_resistance_activities_all() -> int:
    p = ROOT / "common" / "resistance_activity" / "resistance_activity.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    for key, body, _ in find_top_level_blocks(txt):
        if key in {"available", "weight", "effect", "ai_will_do", "state_modifier"}:
            continue
        alert = re.search(r'\balert_text\s*=\s*(\S+)', body)
        max_amt = re.search(r'\bmax_amount\s*=\s*([0-9]+)', body)
        dur = re.search(r'\bduration\s*=\s*([0-9]+)', body)
        rows.append([key, alert.group(1) if alert else "", max_amt.group(1) if max_amt else "", dur.group(1) if dur else ""])
    write_md(OUT / "resistance_activities.md", "Resistance Activities",
        ["activity_key", "alert_text", "max_amount", "duration"],
        rows, "common/resistance_activity/resistance_activity.txt")
    return len(rows)


# ── Phase 18: MIO (Arms Against Tyranny) ────────────────────────────────

def parse_mio_equipment_groups_all() -> Tuple[int, int]:
    p = ROOT / "common" / "equipment_groups" / "mio_equipment_groups.txt"
    grp_rows: List[List[str]] = []
    mem_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    for key, body, _ in find_top_level_blocks(txt):
        grp_rows.append([key])
        eq_m = re.search(r'\bequipment_type\s*=\s*\{', body)
        if eq_m:
            eq_body = extract_block(body, eq_m.start())
            for et in re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]+)\b', eq_body):
                mem_rows.append([key, et])
    write_md(OUT / "mio_equipment_groups.md", "MIO Equipment Groups",
        ["group_key"], grp_rows, "common/equipment_groups/mio_equipment_groups.txt")
    write_md(OUT / "mio_equipment_group_members.md", "MIO Equipment Group Members",
        ["group_key", "equipment_type"], mem_rows, "common/equipment_groups/mio_equipment_groups.txt")
    return len(grp_rows), len(mem_rows)


def parse_mio_organizations_all() -> Tuple[int, int, int, int]:
    """Parse MIO templates (generic) and country-specific organizations.
    Returns (template_count, org_count, equipment_type_count, initial_trait_count)."""
    d = ROOT / "common" / "military_industrial_organization" / "organizations"
    tmpl_rows: List[List[str]] = []
    org_rows: List[List[str]] = []
    eq_rows: List[List[str]] = []
    it_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0, 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            include = re.search(r'\binclude\s*=\s*([a-zA-Z0-9_]+)', body)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            owner_type = "organization" if include else "template"
            # equipment_type list
            eq_m = re.search(r'\bequipment_type\s*=\s*\{', body)
            if eq_m:
                eq_body = extract_block(body, eq_m.start())
                for et in re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]+)\b', eq_body):
                    eq_rows.append([key, et])
            # initial_trait blocks
            it_pos = 0
            while True:
                itm = re.search(r'\binitial_trait\s*=\s*\{', body[it_pos:])
                if not itm:
                    break
                it_body = extract_block(body, it_pos + itm.start())
                nm = re.search(r'\bname\s*=\s*([a-zA-Z0-9_]+)', it_body)
                if nm:
                    it_rows.append([key, owner_type, nm.group(1)])
                it_pos = it_pos + itm.start() + len(it_body) + 2
            # Generic templates don't have `include`
            if include:
                org_rows.append([key, include.group(1), icon.group(1) if icon else "", dlc.group(1) if dlc else "", fp.name])
            else:
                tmpl_rows.append([key, icon.group(1) if icon else "", dlc.group(1) if dlc else "", fp.name])
    write_md(OUT / "mio_templates.md", "MIO Templates (Generic)",
        ["template_key", "icon", "dlc_source", "source_file"],
        tmpl_rows, "common/military_industrial_organization/organizations/*.txt")
    write_md(OUT / "mio_organizations.md", "MIO Organizations (Country-Specific)",
        ["organization_key", "template_key", "icon", "dlc_source", "source_file"],
        org_rows, "common/military_industrial_organization/organizations/*.txt")
    write_md(OUT / "mio_organization_equipment_types.md", "MIO Organization Equipment Types",
        ["owner_key", "equipment_type"],
        eq_rows, "common/military_industrial_organization/organizations/*.txt")
    write_md(OUT / "mio_initial_traits.md", "MIO Initial Traits",
        ["owner_key", "owner_type", "name"],
        it_rows, "common/military_industrial_organization/organizations/*.txt")
    return len(tmpl_rows), len(org_rows), len(eq_rows), len(it_rows)


def parse_mio_policies_all() -> Tuple[int, int]:
    d = ROOT / "common" / "military_industrial_organization" / "policies"
    pol_rows: List[List[str]] = []
    bonus_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            pol_rows.append([key, icon.group(1) if icon else "", dlc.group(1) if dlc else "", fp.name])
            # bonus blocks: organization_modifier, production_bonus, equipment_bonus
            for cat in ("organization_modifier", "production_bonus", "equipment_bonus"):
                bm = re.search(rf'\b{cat}\s*=\s*\{{', body)
                if bm:
                    bb = extract_block(body, bm.start())
                    # may have same_as_mio wrapper
                    inner_m = re.search(r'\bsame_as_mio\s*=\s*\{', bb)
                    target = extract_block(bb, inner_m.start()) if inner_m else bb
                    for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', target):
                        bonus_rows.append([key, cat, mm.group(1), mm.group(2)])
    write_md(OUT / "mio_policies.md", "MIO Policies",
        ["policy_key", "icon", "dlc_source", "source_file"],
        pol_rows, "common/military_industrial_organization/policies/*.txt")
    write_md(OUT / "mio_policy_bonuses.md", "MIO Policy Bonuses",
        ["policy_key", "bonus_category", "bonus_key", "bonus_value"],
        bonus_rows, "common/military_industrial_organization/policies/*.txt")
    return len(pol_rows), len(bonus_rows)


# ── Phase 19: Raids ─────────────────────────────────────────────────────

def parse_raid_categories_all() -> int:
    p = ROOT / "common" / "raids" / "categories" / "raid_categories.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    # wrapped in categories = { ... }
    wrapper_m = re.search(r'\bcategories\s*=\s*\{', txt)
    if not wrapper_m:
        return 0
    wrapper_body = extract_block(txt, wrapper_m.start())
    for key, body, _ in find_top_level_blocks(wrapper_body):
        intel = re.search(r'\bintel_source\s*=\s*(\S+)', body)
        faction = re.search(r'\bfaction_influence_score_on_success\s*=\s*([0-9.\-]+)', body)
        free = "yes" if "free_targeting = yes" in body else ""
        dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
        rows.append([key, intel.group(1) if intel else "", faction.group(1) if faction else "", free, dlc.group(1) if dlc else ""])
    write_md(OUT / "raid_categories.md", "Raid Categories",
        ["category_key", "intel_source", "faction_influence_score_on_success", "free_targeting", "dlc_source"],
        rows, "common/raids/categories/raid_categories.txt")
    return len(rows)


def parse_raids_all() -> Tuple[int, int]:
    d = ROOT / "common" / "raids"
    raid_rows: List[List[str]] = []
    equip_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # wrapped in types = { ... }
        wrapper_m = re.search(r'\btypes\s*=\s*\{', txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        for key, body, _ in find_top_level_blocks(wrapper_body):
            if key in {"visible", "available", "allowed", "ai_will_do", "show_target", "launchable"}:
                continue
            cat = re.search(r'\bcategory\s*=\s*(\S+)', body)
            days = re.search(r'\bdays_to_prepare\s*=\s*([0-9]+)', body)
            cp = re.search(r'\bcommand_power\s*=\s*([0-9]+)', body)
            target_icon = re.search(r'\btarget_icon\s*=\s*(\S+)', body)
            launch_sound = re.search(r'\blaunch_sound\s*=\s*(\S+)', body)
            custom_map = re.search(r'\bcustom_map_icon\s*=\s*(\S+)', body)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            raid_rows.append([key, cat.group(1) if cat else "", days.group(1) if days else "", cp.group(1) if cp else "", target_icon.group(1) if target_icon else "", launch_sound.group(1) if launch_sound else "", custom_map.group(1) if custom_map else "", dlc.group(1) if dlc else "", fp.name])
            # unit_requirements blocks (multiple possible)
            req_idx = 0
            req_pos = 0
            while True:
                rm = re.search(r'\bunit_requirements\s*=\s*\{', body[req_pos:])
                if not rm:
                    break
                req_idx += 1
                req_body = extract_block(body, req_pos + rm.start())
                # equipment = { type = { X } amount = { min = N max = N } }
                eq_m = re.search(r'\bequipment\s*=\s*\{', req_body)
                if eq_m:
                    eq_body = extract_block(req_body, eq_m.start())
                    type_m = re.search(r'\btype\s*=\s*\{([^}]*)\}', eq_body)
                    if type_m:
                        eq_type = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]+)\b', type_m.group(1))
                    else:
                        eq_type = []
                    amount_m = re.search(r'\bamount\s*=\s*\{', eq_body)
                    amt_min = ""
                    amt_max = ""
                    if amount_m:
                        amt_body = extract_block(eq_body, amount_m.start())
                        min_m = re.search(r'\bmin\s*=\s*([0-9]+)', amt_body)
                        max_m = re.search(r'\bmax\s*=\s*([0-9]+)', amt_body)
                        amt_min = min_m.group(1) if min_m else ""
                        amt_max = max_m.group(1) if max_m else ""
                    for et in eq_type:
                        equip_rows.append([key, str(req_idx), et, amt_min, amt_max])
                req_pos = req_pos + rm.start() + len(req_body) + 2
    write_md(OUT / "raids.md", "Raids",
        ["raid_key", "category_key", "days_to_prepare", "command_power", "target_icon", "launch_sound", "custom_map_icon", "dlc_source", "source_file"],
        raid_rows, "common/raids/*.txt")
    write_md(OUT / "raid_equipment_requirements.md", "Raid Equipment Requirements",
        ["raid_key", "requirement_group", "equipment_type", "amount_min", "amount_max"],
        equip_rows, "common/raids/*.txt")
    return len(raid_rows), len(equip_rows)


# ── Phase 20: Career Profile ────────────────────────────────────────────

def parse_medals_all() -> Tuple[int, int]:
    p = ROOT / "common" / "medals" / "00_medals.txt"
    medal_rows: List[List[str]] = []
    tier_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    wrapper_m = re.search(r'\bmedals\s*=\s*\{', txt)
    if not wrapper_m:
        return 0, 0
    wrapper_body = extract_block(txt, wrapper_m.start())
    for key, body, _ in find_top_level_blocks(wrapper_body):
        name = re.search(r'\bname\s*=\s*(\S+)', body)
        desc = re.search(r'\bdescription\s*=\s*(\S+)', body)
        frames = re.search(r'\bframes\s*=\s*\{([^}]*)\}', body)
        frame_list = re.findall(r'[0-9]+', frames.group(1)) if frames else []
        debug_m = re.search(r'\bdebug\s*=\s*\{([^}]*)\}', body)
        tracked = ""
        if debug_m:
            vars_list = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]+)\b', debug_m.group(1))
            tracked = vars_list[0] if vars_list else ""
        medal_rows.append([
            key,
            name.group(1) if name else "",
            desc.group(1) if desc else "",
            frame_list[0] if len(frame_list) > 0 else "",
            frame_list[1] if len(frame_list) > 1 else "",
            frame_list[2] if len(frame_list) > 2 else "",
            tracked,
        ])
        # tiers
        for tier_name in ("bronze", "silver", "gold"):
            tm = re.search(rf'\b{tier_name}\s*=\s*\{{', body)
            if tm:
                t_body = extract_block(body, tm.start())
                var = re.search(r'\bvar\s*=\s*(\S+)', t_body)
                val = re.search(r'\bvalue\s*=\s*([0-9]+)', t_body)
                comp = re.search(r'\bcompare\s*=\s*(\S+)', t_body)
                tier_rows.append([key, tier_name, var.group(1) if var else "", val.group(1) if val else "", comp.group(1) if comp else ""])
    write_md(OUT / "medals.md", "Medals",
        ["medal_key", "name", "description", "frame_1", "frame_2", "frame_3", "tracked_variable"],
        medal_rows, "common/medals/00_medals.txt")
    write_md(OUT / "medal_tiers.md", "Medal Tiers",
        ["medal_key", "tier", "variable", "threshold_value", "compare"],
        tier_rows, "common/medals/00_medals.txt")
    return len(medal_rows), len(tier_rows)


def parse_ribbons_all() -> int:
    p = ROOT / "common" / "ribbons" / "00_ribbons.txt"
    rows: List[List[str]] = []
    if not p.exists():
        return 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    wrapper_m = re.search(r'\bribbons\s*=\s*\{', txt)
    if not wrapper_m:
        return 0
    wrapper_body = extract_block(txt, wrapper_m.start())
    for key, body, _ in find_top_level_blocks(wrapper_body):
        name = re.search(r'\bname\s*=\s*(\S+)', body)
        desc = re.search(r'\bdescription\s*=\s*(\S+)', body)
        quote = re.search(r'\bquote_text\s*=\s*(\S+)', body)
        rows.append([key, name.group(1) if name else "", desc.group(1) if desc else "", quote.group(1) if quote else ""])
    write_md(OUT / "ribbons.md", "Ribbons",
        ["ribbon_key", "name", "description", "quote_text"],
        rows, "common/ribbons/00_ribbons.txt")
    return len(rows)


def parse_aces_all() -> Tuple[int, int, int]:
    p = ROOT / "common" / "aces" / "00_aces.txt"
    mod_rows: List[List[str]] = []
    eff_rows: List[List[str]] = []
    eq_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0, 0
    txt = strip_comments(p.read_text(encoding="utf-8", errors="ignore"))
    wrapper_m = re.search(r'\bmodifiers\s*=\s*\{', txt)
    if not wrapper_m:
        return 0, 0, 0
    wrapper_body = extract_block(txt, wrapper_m.start())
    for key, body, _ in find_top_level_blocks(wrapper_body):
        chance = re.search(r'\bchance\s*=\s*([0-9.]+)', body)
        mod_rows.append([key, chance.group(1) if chance else ""])
        # effect block
        eff_m = re.search(r'\beffect\s*=\s*\{', body)
        if eff_m:
            eff_body = extract_block(body, eff_m.start())
            for em in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', eff_body):
                eff_rows.append([key, em.group(1), em.group(2)])
        # type (can be list or single)
        type_m = re.search(r'\btype\s*=\s*\{([^}]*)\}', body)
        if type_m:
            for et in re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]+)\b', type_m.group(1)):
                eq_rows.append([key, et])
        else:
            type_s = re.search(r'\btype\s*=\s*([a-zA-Z_][a-zA-Z0-9_]+)', body)
            if type_s:
                eq_rows.append([key, type_s.group(1)])
    write_md(OUT / "ace_modifiers.md", "Ace Modifiers",
        ["modifier_key", "chance"], mod_rows, "common/aces/00_aces.txt")
    write_md(OUT / "ace_modifier_effects.md", "Ace Modifier Effects",
        ["modifier_key", "effect_key", "effect_value"], eff_rows, "common/aces/00_aces.txt")
    write_md(OUT / "ace_modifier_equipment_types.md", "Ace Modifier Equipment Types",
        ["modifier_key", "equipment_type"], eq_rows, "common/aces/00_aces.txt")
    return len(mod_rows), len(eff_rows), len(eq_rows)


def parse_unit_medals_all() -> Tuple[int, int]:
    p = ROOT / "common" / "unit_medals" / "00_default.txt"
    medal_rows: List[List[str]] = []
    mod_rows: List[List[str]] = []
    if not p.exists():
        return 0, 0
    raw = p.read_text(encoding="utf-8", errors="ignore")
    txt = _resolve_at_vars(strip_comments(raw))
    wrapper_m = re.search(r'\bunit_medals\s*=\s*\{', txt)
    if not wrapper_m:
        return 0, 0
    wrapper_body = extract_block(txt, wrapper_m.start())
    for key, body, _ in find_top_level_blocks(wrapper_body):
        if key in {"available", "unit_modifiers", "one_time_effect", "ai_will_do"}:
            continue
        frame = re.search(r'\bframe\s*=\s*([0-9]+)', body)
        icon = re.search(r'\bicon\s*=\s*(\S+)', body)
        cost = re.search(r'\bcost\s*=\s*([0-9]+)', body)
        medal_rows.append([key, frame.group(1) if frame else "", icon.group(1) if icon else "", cost.group(1) if cost else ""])
        um_m = re.search(r'\bunit_modifiers\s*=\s*\{', body)
        if um_m:
            um_body = extract_block(body, um_m.start())
            for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', um_body):
                mod_rows.append([key, mm.group(1), mm.group(2)])
    write_md(OUT / "unit_medals.md", "Unit Medals",
        ["medal_key", "frame", "icon", "cost"],
        medal_rows, "common/unit_medals/00_default.txt")
    write_md(OUT / "unit_medal_modifiers.md", "Unit Medal Modifiers",
        ["medal_key", "modifier_key", "modifier_value"],
        mod_rows, "common/unit_medals/00_default.txt")
    return len(medal_rows), len(mod_rows)


# ── Phase 21: BOP & Continuous Focuses ──────────────────────────────────

def parse_bop_all() -> Tuple[int, int, int, int]:
    d = ROOT / "common" / "bop"
    bop_rows: List[List[str]] = []
    side_rows: List[List[str]] = []
    range_rows: List[List[str]] = []
    rmod_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0, 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for bop_key, bop_body, _ in find_top_level_blocks(txt):
            init_val = re.search(r'\binitial_value\s*=\s*([0-9.\-]+)', bop_body)
            left = re.search(r'\bleft_side\s*=\s*(\S+)', bop_body)
            right = re.search(r'\bright_side\s*=\s*(\S+)', bop_body)
            dec_cat = re.search(r'\bdecision_category\s*=\s*(\S+)', bop_body)
            bop_rows.append([bop_key, init_val.group(1) if init_val else "", left.group(1) if left else "", right.group(1) if right else "", dec_cat.group(1) if dec_cat else "", fp.name])
            # Neutral ranges at root level
            _parse_bop_ranges(bop_key, "neutral", bop_body, range_rows, rmod_rows)
            # Side blocks
            side_pos = 0
            while True:
                sm = re.search(r'\bside\s*=\s*\{', bop_body[side_pos:])
                if not sm:
                    break
                s_body = extract_block(bop_body, side_pos + sm.start())
                sid = re.search(r'\bid\s*=\s*(\S+)', s_body)
                s_icon = re.search(r'\bicon\s*=\s*(\S+)', s_body)
                side_id = sid.group(1) if sid else ""
                # determine position from left_side/right_side
                if left and side_id == left.group(1):
                    pos_label = "left"
                elif right and side_id == right.group(1):
                    pos_label = "right"
                else:
                    pos_label = "unknown"
                side_rows.append([bop_key, side_id, pos_label, s_icon.group(1) if s_icon else ""])
                _parse_bop_ranges(bop_key, side_id, s_body, range_rows, rmod_rows)
                side_pos = side_pos + sm.start() + len(s_body) + 2
    write_md(OUT / "balance_of_power_definitions.md", "Balance of Power Definitions",
        ["bop_key", "initial_value", "left_side", "right_side", "decision_category", "source_file"],
        bop_rows, "common/bop/*.txt")
    write_md(OUT / "bop_sides.md", "BOP Sides",
        ["bop_key", "side_id", "side_position", "icon"],
        side_rows, "common/bop/*.txt")
    write_md(OUT / "bop_ranges.md", "BOP Ranges",
        ["range_id", "bop_key", "side_id", "min_value", "max_value"],
        range_rows, "common/bop/*.txt")
    write_md(OUT / "bop_range_modifiers.md", "BOP Range Modifiers",
        ["range_id", "modifier_key", "modifier_value"],
        rmod_rows, "common/bop/*.txt")
    return len(bop_rows), len(side_rows), len(range_rows), len(rmod_rows)


def _parse_bop_ranges(bop_key: str, side_id: str, body: str,
                       range_rows: list, rmod_rows: list) -> None:
    """Extract range blocks from a BOP side or root body."""
    pos = 0
    while True:
        rm = re.search(r'\brange\s*=\s*\{', body[pos:])
        if not rm:
            break
        r_body = extract_block(body, pos + rm.start())
        rid = re.search(r'\bid\s*=\s*(\S+)', r_body)
        rmin = re.search(r'\bmin\s*=\s*([0-9.\-]+)', r_body)
        rmax = re.search(r'\bmax\s*=\s*([0-9.\-]+)', r_body)
        range_id = rid.group(1) if rid else ""
        range_rows.append([range_id, bop_key, side_id, rmin.group(1) if rmin else "", rmax.group(1) if rmax else ""])
        # modifiers inside this range
        mod_m = re.search(r'\bmodifier\s*=\s*\{', r_body)
        if mod_m:
            mod_body = extract_block(r_body, mod_m.start())
            for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', mod_body):
                rmod_rows.append([range_id, mm.group(1), mm.group(2)])
        pos = pos + rm.start() + len(r_body) + 2


def parse_continuous_focuses_all() -> Tuple[int, int, int]:
    d = ROOT / "common" / "continuous_focus"
    pal_rows: List[List[str]] = []
    foc_rows: List[List[str]] = []
    fmod_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # continuous_focus_palette = { ... }
        pal_pos = 0
        while True:
            pm = re.search(r'\bcontinuous_focus_palette\s*=\s*\{', txt[pal_pos:])
            if not pm:
                break
            pal_body = extract_block(txt, pal_pos + pm.start())
            pid = re.search(r'\bid\s*=\s*(\S+)', pal_body)
            is_default = "yes" if re.search(r'\bdefault\s*=\s*yes', pal_body) else ""
            reset = "yes" if "reset_on_civilwar = yes" in pal_body else ""
            pos_m = re.search(r'\bposition\s*=\s*\{[^}]*x\s*=\s*([0-9.\-]+)[^}]*y\s*=\s*([0-9.\-]+)', pal_body)
            pal_id = pid.group(1) if pid else ""
            pal_rows.append([pal_id, is_default, reset, pos_m.group(1) if pos_m else "", pos_m.group(2) if pos_m else "", fp.name])
            # focus entries
            foc_pos = 0
            while True:
                fm = re.search(r'\bfocus\s*=\s*\{', pal_body[foc_pos:])
                if not fm:
                    break
                f_body = extract_block(pal_body, foc_pos + fm.start())
                fid = re.search(r'\bid\s*=\s*(\S+)', f_body)
                ficon = re.search(r'\bicon\s*=\s*(\S+)', f_body)
                daily = re.search(r'\bdaily_cost\s*=\s*([0-9]+)', f_body)
                cap = "yes" if "available_if_capitulated = yes" in f_body else ""
                dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', f_body)
                foc_id = fid.group(1) if fid else ""
                foc_rows.append([foc_id, pal_id, ficon.group(1) if ficon else "", daily.group(1) if daily else "", cap, dlc.group(1) if dlc else "", fp.name])
                # modifier block
                mod_m = re.search(r'\bmodifier\s*=\s*\{', f_body)
                if mod_m:
                    mod_body = extract_block(f_body, mod_m.start())
                    for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', mod_body):
                        fmod_rows.append([foc_id, mm.group(1), mm.group(2)])
                foc_pos = foc_pos + fm.start() + len(f_body) + 2
            pal_pos = pal_pos + pm.start() + len(pal_body) + 2
    write_md(OUT / "continuous_focus_palettes.md", "Continuous Focus Palettes",
        ["palette_id", "is_default", "reset_on_civilwar", "position_x", "position_y", "source_file"],
        pal_rows, "common/continuous_focus/*.txt")
    write_md(OUT / "continuous_focuses.md", "Continuous Focuses",
        ["focus_id", "palette_id", "icon", "daily_cost", "available_if_capitulated", "dlc_source", "source_file"],
        foc_rows, "common/continuous_focus/*.txt")
    write_md(OUT / "continuous_focus_modifiers.md", "Continuous Focus Modifiers",
        ["focus_id", "modifier_key", "modifier_value"],
        fmod_rows, "common/continuous_focus/*.txt")
    return len(pal_rows), len(foc_rows), len(fmod_rows)


# ── Phase 22: Misc DLC ──────────────────────────────────────────────────

def parse_technology_sharing_all() -> int:
    d = ROOT / "common" / "technology_sharing"
    rows: List[List[str]] = []
    if not d.exists():
        return 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # repeated technology_sharing_group = { ... } blocks
        pos = 0
        while True:
            m = re.search(r'\btechnology_sharing_group\s*=\s*\{', txt[pos:])
            if not m:
                break
            body = extract_block(txt, pos + m.start())
            gid = re.search(r'\bid\s*=\s*(\S+)', body)
            name = re.search(r'\bname\s*=\s*(\S+)', body)
            desc = re.search(r'\bdesc\s*=\s*(\S+)', body)
            pic = re.search(r'\bpicture\s*=\s*(\S+)', body)
            bonus = re.search(r'\bresearch_sharing_per_country_bonus\s*=\s*([0-9.]+)', body)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            rows.append([
                gid.group(1) if gid else "",
                name.group(1) if name else "",
                desc.group(1) if desc else "",
                pic.group(1) if pic else "",
                bonus.group(1) if bonus else "",
                dlc.group(1) if dlc else "",
                fp.name,
            ])
            pos = pos + m.start() + len(body) + 2
    write_md(OUT / "technology_sharing_groups.md", "Technology Sharing Groups",
        ["group_id", "name", "desc", "picture", "research_sharing_per_country_bonus", "dlc_source", "source_file"],
        rows, "common/technology_sharing/*.txt")
    return len(rows)


def parse_dynamic_modifiers_all() -> Tuple[int, int]:
    d = ROOT / "common" / "dynamic_modifiers"
    mod_rows: List[List[str]] = []
    eff_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    skip_keys = {"enable", "remove_trigger", "icon", "attacker_modifier",
                 "ai_will_do", "available", "visible", "OR", "AND", "NOT"}
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            attacker = "yes" if "attacker_modifier = yes" in body else ""
            mod_rows.append([key, icon.group(1) if icon else "", attacker, fp.name])
            # effects: key = value pairs that are NOT structural blocks
            for em in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\s{]+)', body):
                ek = em.group(1)
                ev = em.group(2)
                if ek in skip_keys or ek == "icon" or ek == "attacker_modifier":
                    continue
                # determine if static numeric or variable reference
                try:
                    float(ev)
                    eff_rows.append([key, ek, ev, ""])
                except ValueError:
                    if re.match(r'^[a-zA-Z_]', ev):
                        eff_rows.append([key, ek, "", ev])
    write_md(OUT / "dynamic_modifiers.md", "Dynamic Modifiers",
        ["modifier_key", "icon", "attacker_modifier", "source_file"],
        mod_rows, "common/dynamic_modifiers/*.txt")
    write_md(OUT / "dynamic_modifier_effects.md", "Dynamic Modifier Effects",
        ["modifier_key", "effect_key", "effect_value_static", "effect_value_variable"],
        eff_rows, "common/dynamic_modifiers/*.txt")
    return len(mod_rows), len(eff_rows)


def parse_scientist_traits_all() -> Tuple[int, int]:
    d = ROOT / "common" / "scientist_traits"
    trait_rows: List[List[str]] = []
    mod_rows: List[List[str]] = []
    if not d.exists():
        return 0, 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            icon = re.search(r'\bicon\s*=\s*(\S+)', body)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            trait_rows.append([key, icon.group(1) if icon else "", dlc.group(1) if dlc else ""])
            mod_m = re.search(r'\bmodifier\s*=\s*\{', body)
            if mod_m:
                mod_body = extract_block(body, mod_m.start())
                for mm in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9.\-]+)', mod_body):
                    mod_rows.append([key, mm.group(1), mm.group(2)])
    write_md(OUT / "scientist_traits.md", "Scientist Traits",
        ["trait_key", "icon", "dlc_source"],
        trait_rows, "common/scientist_traits/*.txt")
    write_md(OUT / "scientist_trait_modifiers.md", "Scientist Trait Modifiers",
        ["trait_key", "modifier_key", "modifier_value"],
        mod_rows, "common/scientist_traits/*.txt")
    return len(trait_rows), len(mod_rows)


def parse_peace_action_categories_all() -> int:
    d = ROOT / "common" / "peace_conference" / "categories"
    rows: List[List[str]] = []
    if not d.exists():
        return 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        wrapper_m = re.search(r'\bpeace_action_categories\s*=\s*\{', txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        for key, body, _ in find_top_level_blocks(wrapper_body):
            name = re.search(r'\bname\s*=\s*(\S+)', body)
            is_default = "yes" if "default = yes" in body else ""
            rows.append([key, name.group(1) if name else "", is_default])
    write_md(OUT / "peace_action_categories.md", "Peace Action Categories",
        ["category_key", "name", "is_default"],
        rows, "common/peace_conference/categories/*.txt")
    return len(rows)


def parse_peace_cost_modifiers_all() -> int:
    d = ROOT / "common" / "peace_conference" / "cost_modifiers"
    rows: List[List[str]] = []
    if not d.exists():
        return 0
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        wrapper_m = re.search(r'\bpeace_action_modifiers\s*=\s*\{', txt)
        if not wrapper_m:
            continue
        wrapper_body = extract_block(txt, wrapper_m.start())
        for key, body, _ in find_top_level_blocks(wrapper_body):
            if key in {"enable", "category", "peace_action_type", "cost_multiplier"}:
                continue
            cat = re.search(r'\bcategory\s*=\s*(\S+)', body)
            # peace_action_type can be single or { list }
            pat_m = re.search(r'\bpeace_action_type\s*=\s*\{([^}]*)\}', body)
            if pat_m:
                pat = " ".join(re.findall(r'\b([a-zA-Z_]+)\b', pat_m.group(1)))
            else:
                pat_s = re.search(r'\bpeace_action_type\s*=\s*([a-zA-Z_]+)', body)
                pat = pat_s.group(1) if pat_s else ""
            cost = re.search(r'\bcost_multiplier\s*=\s*([0-9.\-]+)', body)
            dlc = re.search(r'has_dlc\s*=\s*"([^"]+)"', body)
            rows.append([key, cat.group(1) if cat else "", pat, cost.group(1) if cost else "", dlc.group(1) if dlc else "", fp.name])
    write_md(OUT / "peace_cost_modifiers.md", "Peace Cost Modifiers",
        ["modifier_key", "category_key", "peace_action_type", "cost_multiplier", "dlc_source", "source_file"],
        rows, "common/peace_conference/cost_modifiers/*.txt")
    return len(rows)


# ════════════════════════════════════════════════════════════════
# Phase 23 — Doctrines (Officer Corps / Military Experience)
# ════════════════════════════════════════════════════════════════

def parse_doctrine_folders() -> int:
    """Parse common/doctrines/folders/doctrine_folders.txt → doctrine_folders.md."""
    fp = ROOT / "common" / "doctrines" / "folders" / "doctrine_folders.txt"
    if not fp.exists():
        return 0
    txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
    rows: List[List[str]] = []
    for key, body, _ in find_top_level_blocks(txt):
        name = re.search(r'\bname\s*=\s*"?([^"\n]+)"?', body)
        ledger = re.search(r'\bledger\s*=\s*(\w+)', body)
        rows.append([
            key,
            name.group(1).strip() if name else "",
            ledger.group(1) if ledger else "",
            ledger.group(1) if ledger else "",  # xp_type mirrors ledger
        ])
    write_md(OUT / "doctrine_folders.md", "Doctrine Folders",
        ["folder_key", "name_loc", "ledger", "xp_type"],
        rows, "common/doctrines/folders/doctrine_folders.txt")
    return len(rows)


def parse_doctrine_tracks() -> int:
    """Parse common/doctrines/tracks/*.txt → doctrine_tracks.md."""
    d = ROOT / "common" / "doctrines" / "tracks"
    if not d.exists():
        return 0
    # Map track keys to folders based on filename
    folder_map = {"land": "land", "sea": "naval", "air": "air"}
    rows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        # Detect folder from filename
        folder_key = ""
        for prefix, fk in folder_map.items():
            if prefix in fp.stem:
                folder_key = fk
                break
        for key, body, _ in find_top_level_blocks(txt):
            name = re.search(r'\bname\s*=\s*"?([^"\n]+)"?', body)
            mult = re.search(r'\bmultiplier\s*=\s*([0-9.]+)', body)
            rows.append([
                key,
                folder_key,
                name.group(1).strip() if name else "",
                mult.group(1) if mult else "",
            ])
    write_md(OUT / "doctrine_tracks.md", "Doctrine Tracks",
        ["track_key", "folder_key", "name_loc", "mastery_multiplier"],
        rows, "common/doctrines/tracks/*.txt")
    return len(rows)


def parse_grand_doctrines() -> Tuple[int, int]:
    """Parse common/doctrines/grand_doctrines/*.txt → grand_doctrines.md + grand_doctrine_tracks.md."""
    d = ROOT / "common" / "doctrines" / "grand_doctrines"
    if not d.exists():
        return 0, 0
    gd_rows: List[List[str]] = []
    gt_rows: List[List[str]] = []
    for fp in sorted(d.glob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            folder = re.search(r'\bfolder\s*=\s*(\w+)', body)
            name = re.search(r'\bname\s*=\s*"?([^"\n]+)"?', body)
            xp_cost = re.search(r'\bxp_cost\s*=\s*([0-9]+)', body)
            xp_type = re.search(r'\bxp_type\s*=\s*(\w+)', body)
            gd_rows.append([
                key,
                folder.group(1) if folder else "",
                name.group(1).strip() if name else "",
                xp_cost.group(1) if xp_cost else "100",
                xp_type.group(1) if xp_type else "",
                fp.name,
            ])
            # Extract tracks list
            tracks_m = re.search(r'\btracks\s*=\s*\{([^}]*)\}', body)
            if tracks_m:
                track_keys = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', tracks_m.group(1))
                for ordinal, tk in enumerate(track_keys, 1):
                    gt_rows.append([key, tk, str(ordinal)])
    write_md(OUT / "grand_doctrines.md", "Grand Doctrines",
        ["doctrine_key", "folder_key", "name_loc", "xp_cost", "xp_type", "source_file"],
        gd_rows, "common/doctrines/grand_doctrines/*.txt")
    write_md(OUT / "grand_doctrine_tracks.md", "Grand Doctrine Tracks",
        ["doctrine_key", "track_key", "ordinal"],
        gt_rows, "common/doctrines/grand_doctrines/*.txt")
    return len(gd_rows), len(gt_rows)


def parse_subdoctrines() -> int:
    """Parse common/doctrines/subdoctrines/**/*.txt → subdoctrines.md."""
    d = ROOT / "common" / "doctrines" / "subdoctrines"
    if not d.exists():
        return 0
    rows: List[List[str]] = []
    for fp in sorted(d.rglob("*.txt")):
        txt = strip_comments(fp.read_text(encoding="utf-8", errors="ignore"))
        for key, body, _ in find_top_level_blocks(txt):
            track = re.search(r'\btrack\s*=\s*(\w+)', body)
            name = re.search(r'\bname\s*=\s*"?([^"\n]+)"?', body)
            xp_cost = re.search(r'\bxp_cost\s*=\s*([0-9]+)', body)
            xp_type = re.search(r'\bxp_type\s*=\s*(\w+)', body)
            # Count reward keys (top-level blocks within rewards = { })
            reward_count = 0
            rewards_m = re.search(r'\brewards\s*=\s*\{', body)
            if rewards_m:
                rewards_body = extract_block(body, rewards_m.start())
                reward_count = len(find_top_level_blocks(rewards_body))
            rows.append([
                key,
                track.group(1) if track else "",
                name.group(1).strip() if name else "",
                xp_cost.group(1) if xp_cost else "100",
                xp_type.group(1) if xp_type else "",
                str(reward_count),
                fp.name,
            ])
    write_md(OUT / "subdoctrines.md", "Subdoctrines",
        ["subdoctrine_key", "track_key", "name_loc", "xp_cost", "xp_type", "reward_count", "source_file"],
        rows, "common/doctrines/subdoctrines/**/*.txt")
    return len(rows)


def parse_country_starting_doctrines() -> int:
    """Extract set_grand_doctrine / set_sub_doctrine from history/countries/*.txt → country_starting_doctrines.md."""
    dirp = ROOT / "history" / "countries"
    rows: List[List[str]] = []
    for fp in sorted(dirp.glob("*.txt")):
        tag_m = re.match(r"^([A-Z0-9]+)", fp.name)
        if not tag_m:
            continue
        tag = tag_m.group(1)
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        # Track current date context: top-level = base date, inside date block = that date
        # Split into lines and track which date block we're in
        current_date = "1936-01-01"
        depth = 0
        date_stack: List[str] = []
        for line in txt.splitlines():
            stripped = line.split("#")[0]  # remove comments
            # Check for date block start: 1939.1.1 = {
            date_m = re.match(r'\s*(\d{4}\.\d{1,2}\.\d{1,2})\s*=\s*\{', stripped)
            if date_m:
                ds = date_m.group(1)
                parts = ds.split(".")
                iso_date = f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
                date_stack.append(current_date)
                current_date = iso_date
                depth += 1
                continue
            # Track brace depth for date scoping
            opens = stripped.count("{")
            closes = stripped.count("}")
            if date_stack:
                depth += opens - closes
                if depth <= 0:
                    current_date = date_stack.pop()
                    depth = 0
            # Extract doctrine assignments
            gd = re.search(r'\bset_grand_doctrine\s*=\s*(\w+)', stripped)
            if gd:
                rows.append([tag, current_date, "grand", gd.group(1).lower(), fp.name])
            sd = re.search(r'\bset_sub_doctrine\s*=\s*(\w+)', stripped)
            if sd:
                rows.append([tag, current_date, "sub", sd.group(1).lower(), fp.name])
    write_md(OUT / "country_starting_doctrines.md", "Country Starting Doctrines",
        ["country_tag", "date", "doctrine_type", "doctrine_key", "source_file"],
        rows, "history/countries/*.txt")
    return len(rows)


def main() -> None:
    global ROOT

    parser = argparse.ArgumentParser(
        description="Extract Hearts of Iron IV game data into markdown tables.",
    )
    parser.add_argument(
        "--hoi4-root",
        default=None,
        help="Path to the HOI4 installation directory. "
             "Falls back to HOI4_ROOT env var, then default Steam paths.",
    )
    args = parser.parse_args()

    ROOT = _detect_hoi4_root(args.hoi4_root)
    print(f"HOI4 install: {ROOT}")
    print(f"Output dir:   {OUT}")

    OUT.mkdir(parents=True, exist_ok=True)

    stats: Dict[str, int] = {}
    stats["country_tags"] = parse_country_tags()
    stats["provinces"] = parse_map_definition()
    stats["resources"] = parse_resources()

    s, sr, sb, sv, sp = parse_states()
    stats["states"] = s
    stats["state_resources"] = sr
    stats["state_buildings"] = sb
    stats["state_victory_points"] = sv
    stats["state_provinces"] = sp

    ch, ct = parse_country_history()
    stats["country_history"] = ch
    stats["country_starting_technologies"] = ct

    stats["province_building_positions"] = parse_building_positions()

    rg, rp = parse_strategic_regions()
    stats["strategic_regions"] = rg
    stats["strategic_region_provinces"] = rp

    idc, sub = parse_ideologies()
    stats["ideologies"] = idc
    stats["sub_ideologies"] = sub

    c, cr = parse_characters_ger()
    stats["characters_ger"] = c
    stats["character_roles_ger"] = cr

    ft, f, fl = parse_focus_germany()
    stats["focus_trees"] = ft
    stats["focuses_germany"] = f
    stats["focus_links_germany"] = fl

    dt, dr, ds = parse_division_templates_ger()
    stats["division_templates_ger"] = dt
    stats["division_template_regiments_ger"] = dr
    stats["division_template_support_ger"] = ds

    flt, tf, sh = parse_naval_oob_all()
    stats["fleets_all"] = flt
    stats["task_forces_all"] = tf
    stats["ships_all"] = sh

    stats["air_wings_all"] = parse_air_oob_all()
    stats["continents"] = parse_continents()
    stats["building_types"] = parse_building_types()
    t, l, u = parse_technologies_infantry()
    stats["technologies_infantry"] = t
    stats["technology_links_infantry"] = l
    stats["technology_unlocks_infantry"] = u
    stats["supply_nodes"] = parse_map_supply_nodes()

    stats["countries_visuals"] = parse_country_visuals_all()
    ta, tla, tua = parse_technologies_all()
    stats["technologies_all"] = ta
    stats["technology_links_all"] = tla
    stats["technology_unlocks_all"] = tua

    fa_t, fa_f, fa_l = parse_focuses_all()
    stats["focus_trees_all"] = fa_t
    stats["focuses_all"] = fa_f
    stats["focus_links_all"] = fa_l

    ca, car = parse_characters_all()
    stats["characters_all"] = ca
    stats["character_roles_all"] = car

    ia, im = parse_ideas_all()
    stats["ideas_all"] = ia
    stats["idea_modifiers_all"] = im

    loa_t, loa_r, loa_s, loa_d = parse_land_oob_all()
    stats["division_templates_all"] = loa_t
    stats["division_template_regiments_all"] = loa_r
    stats["division_template_support_all"] = loa_s
    stats["divisions_all"] = loa_d

    stats["unit_types_all"] = parse_unit_types_all()

    eq_all, eq_res = parse_equipment_all()
    stats["equipment_all"] = eq_all
    stats["equipment_resources_all"] = eq_res

    stats["state_categories"] = parse_state_categories()
    stats["terrain_types"] = parse_terrain_types()

    # ── Gap fillers: missing tables ──
    sc, so, pb, pch = parse_state_history_extended()
    stats["state_cores"] = sc
    stats["state_ownership_history"] = so
    stats["province_buildings"] = pb
    stats["province_controller_history"] = pch

    tc, tcj = parse_technology_categories_all()
    stats["technology_categories"] = tc
    stats["technology_categories_junction"] = tcj

    ct_t, crt = parse_character_traits_all()
    stats["character_traits"] = ct_t
    stats["character_role_traits"] = crt

    stats["country_starting_ideas"] = parse_country_starting_ideas_all()
    stats["equipment_variants"] = parse_equipment_variants_all()

    te_bld, te_mod = parse_terrain_extended()
    stats["terrain_building_limits"] = te_bld
    stats["terrain_combat_modifiers"] = te_mod

    # ── Phase 11: Map Connectivity ──
    stats["province_adjacencies"] = parse_province_adjacencies()
    stats["province_railways"] = parse_province_railways()

    # ── Phase 12: Governance ──
    auto_s, auto_m = parse_autonomy_states_all()
    stats["autonomy_states"] = auto_s
    stats["autonomy_state_modifiers"] = auto_m

    occ_l, occ_m = parse_occupation_laws_all()
    stats["occupation_laws"] = occ_l
    stats["occupation_law_modifiers"] = occ_m

    # ── Phase 14: Bookmarks ──
    bm_b, bm_c = parse_bookmarks_all()
    stats["bookmarks"] = bm_b
    stats["bookmark_countries"] = bm_c

    # ── Phase 15: Decisions ──
    stats["decision_categories"] = parse_decision_categories_all()
    stats["decisions_all"] = parse_decisions_all()

    # ── Phase 16: Espionage ──
    stats["operation_tokens"] = parse_operation_tokens_all()

    opd_p, opd_e = parse_operation_phase_definitions_all()
    stats["operation_phase_definitions"] = opd_p
    stats["operation_phase_equipment"] = opd_e

    op_o, op_t, op_e, op_pg, op_po = parse_operations_all()
    stats["operations"] = op_o
    stats["operation_awarded_tokens"] = op_t
    stats["operation_equipment_requirements"] = op_e
    stats["operation_phase_groups"] = op_pg
    stats["operation_phase_options"] = op_po

    ia_a, ia_n = parse_intelligence_agencies_all()
    stats["intelligence_agencies"] = ia_a
    stats["intelligence_agency_names"] = ia_n

    iau_b, iau_u, iau_l, iau_p = parse_intel_agency_upgrades_all()
    stats["intel_agency_upgrade_branches"] = iau_b
    stats["intel_agency_upgrades"] = iau_u
    stats["intel_agency_upgrade_levels"] = iau_l
    stats["intel_agency_upgrade_progress_modifiers"] = iau_p

    # ── Phase 17: Resistance ──
    cm_m, cm_e = parse_compliance_modifiers_all()
    stats["compliance_modifiers"] = cm_m
    stats["compliance_modifier_effects"] = cm_e

    rm_m, rm_e = parse_resistance_modifiers_all()
    stats["resistance_modifiers"] = rm_m
    stats["resistance_modifier_effects"] = rm_e

    stats["resistance_activities"] = parse_resistance_activities_all()

    # ── Phase 18: MIO ──
    mio_g, mio_gm = parse_mio_equipment_groups_all()
    stats["mio_equipment_groups"] = mio_g
    stats["mio_equipment_group_members"] = mio_gm

    mio_t, mio_o, mio_et, mio_it = parse_mio_organizations_all()
    stats["mio_templates"] = mio_t
    stats["mio_organizations"] = mio_o
    stats["mio_organization_equipment_types"] = mio_et
    stats["mio_initial_traits"] = mio_it

    mio_p, mio_pb = parse_mio_policies_all()
    stats["mio_policies"] = mio_p
    stats["mio_policy_bonuses"] = mio_pb

    miot, miotb, miotp, miote = parse_mio_traits_all()
    stats["mio_traits"] = miot
    stats["mio_trait_bonuses"] = miotb
    stats["mio_trait_prerequisites"] = miotp
    stats["mio_trait_exclusions"] = miote

    # ── Phase 19: Raids ──
    stats["raid_categories"] = parse_raid_categories_all()

    raid_r, raid_e = parse_raids_all()
    stats["raids"] = raid_r
    stats["raid_equipment_requirements"] = raid_e

    # ── Phase 20: Career Profile ──
    med_m, med_t = parse_medals_all()
    stats["medals"] = med_m
    stats["medal_tiers"] = med_t

    stats["ribbons"] = parse_ribbons_all()

    ace_m, ace_e, ace_t = parse_aces_all()
    stats["ace_modifiers"] = ace_m
    stats["ace_modifier_effects"] = ace_e
    stats["ace_modifier_equipment_types"] = ace_t

    um_m, um_mod = parse_unit_medals_all()
    stats["unit_medals"] = um_m
    stats["unit_medal_modifiers"] = um_mod

    # ── Phase 21: BOP & Continuous Focuses ──
    bop_b, bop_s, bop_r, bop_rm = parse_bop_all()
    stats["balance_of_power_definitions"] = bop_b
    stats["bop_sides"] = bop_s
    stats["bop_ranges"] = bop_r
    stats["bop_range_modifiers"] = bop_rm

    cf_p, cf_f, cf_m = parse_continuous_focuses_all()
    stats["continuous_focus_palettes"] = cf_p
    stats["continuous_focuses"] = cf_f
    stats["continuous_focus_modifiers"] = cf_m

    # ── Phase 22: Misc DLC ──
    stats["technology_sharing_groups"] = parse_technology_sharing_all()

    dm_m, dm_e = parse_dynamic_modifiers_all()
    stats["dynamic_modifiers"] = dm_m
    stats["dynamic_modifier_effects"] = dm_e

    st_t, st_m = parse_scientist_traits_all()
    stats["scientist_traits"] = st_t
    stats["scientist_trait_modifiers"] = st_m

    stats["peace_action_categories"] = parse_peace_action_categories_all()
    stats["peace_cost_modifiers"] = parse_peace_cost_modifiers_all()

    # ── Phase 23: Doctrines ──
    stats["doctrine_folders"] = parse_doctrine_folders()
    stats["doctrine_tracks"] = parse_doctrine_tracks()

    gd_n, gt_n = parse_grand_doctrines()
    stats["grand_doctrines"] = gd_n
    stats["grand_doctrine_tracks"] = gt_n

    stats["subdoctrines"] = parse_subdoctrines()
    stats["country_starting_doctrines"] = parse_country_starting_doctrines()

    summary_lines = ["# Markdown Extraction Summary", "", f"Output directory: `{OUT.as_posix()}`", "", "| dataset | rows |", "|---|---:|"]
    for k in sorted(stats.keys()):
        summary_lines.append(f"| {k} | {stats[k]} |")

    write_text(OUT / "SUMMARY.md", "Markdown Extraction Summary", "\n".join(summary_lines[1:]) + "\n")


if __name__ == "__main__":
    main()
