# HOI4 Database — V2 Implementation Plan

> **Date:** 2026-04-09
> **Branch:** TBD (new feature branch from `main`)
> **Predecessor:** `docs/plans/v1/` (API v1 — 151 tables, 105 tests, complete)
> **Database:** 151 tables → ~158 tables after V2

---

## Motivation

V1 delivers a complete API over the 151-table HOI4 database — starting state,
military, tech trees, focus trees, equipment, ideas, DLC systems. V2 fills four
data gaps identified during walkthrough-guide analysis:

| Gap | Why it matters for walkthroughs |
|-----|-------------------------------|
| **Focus & idea scripted effects** | "What happens when I finish this focus?" — the core walkthrough question |
| **Events** | Narrative glue — Anschluss, Danzig or War, civil wars. Focuses trigger events. |
| **Starting diplomacy** | "Who guarantees Poland?", "Who's in the Axis?" drive early decisions |
| **Wargoal type definitions** | What "puppet wargoal" vs "annex wargoal" means, costs, constraints |

All four systems have static game data files suitable for database modeling.

---

## Architecture Decisions

### Raw Text for Scripted Effects

Focus completion rewards, event triggers/effects, idea effects, and decision
effects are deeply nested Paradox Script with conditionals, DLC guards, and
arbitrary nesting. Two approaches:

| Approach | Queryable | Lossless | Parser effort |
|----------|-----------|----------|---------------|
| Structured rows (one row per effect type) | Yes | No — edge cases lost | Very high |
| Raw TEXT columns | No | Yes | Low |

**Decision:** Raw TEXT columns. The primary consumer (LLM walkthrough generation)
can interpret Paradox Script natively. Structured parsing would take 10x the
effort with lossy results. A future V3 could add structured overlay tables
if queryability becomes important.

### New Tables vs ALTER Existing

- **Focuses & ideas:** ALTER existing tables to add TEXT columns (no new FKs)
- **Events & diplomacy & wargoals:** New tables (new game file parsers needed)
- **Decisions:** ALTER existing tables to add TEXT columns (parsers already exist)

---

## Progress Tracker

### Phase 7: Focus & Idea Scripted Effects
- [ ] 7.1 — Schema changes (ALTER TABLE)
- [ ] 7.2 — Parser updates (extract raw text blocks)
- [ ] 7.3 — Re-extract data & regenerate CSVs
- [ ] 7.4 — Update views (add new columns)
- [ ] 7.5 — Update API schemas & test
- [ ] Test gate: effects data populated, API returns new fields

### Phase 8: Wargoal Type Definitions
- [ ] 8.1 — Schema (new table)
- [ ] 8.2 — Parser (new module)
- [ ] 8.3 — Extract data & generate CSV
- [ ] 8.4 — API router + schema + tests
- [ ] Test gate: wargoal types queryable via REST + GraphQL

### Phase 9: Starting Diplomatic State
- [ ] 9.1 — Schema (new tables)
- [ ] 9.2 — Parser (new module + extend country history)
- [ ] 9.3 — Extract data & generate CSV
- [ ] 9.4 — API router + schema + tests
- [ ] Test gate: diplomacy queryable via REST + GraphQL

### Phase 10: Events
- [ ] 10.1 — Schema (new tables)
- [ ] 10.2 — Parser (new module)
- [ ] 10.3 — Extract data & generate CSV
- [ ] 10.4 — API router + schema + tests
- [ ] Test gate: events queryable via REST + GraphQL

### Phase 11: Decision Scripted Effects
- [ ] 11.1 — Schema changes (ALTER TABLE)
- [ ] 11.2 — Parser updates (extract raw text blocks)
- [ ] 11.3 — Re-extract data & regenerate CSVs
- [ ] 11.4 — Update API schemas & test
- [ ] Test gate: decision effects populated, API returns new fields

### Phase 12: Polish & Integration
- [ ] 12.1 — Update all documentation
- [ ] 12.2 — Regenerate seed SQL
- [ ] 12.3 — Full test suite + smoke tests
- [ ] Final test gate

---

## Phase 7: Focus & Idea Scripted Effects

The simplest gap — no new tables, just new columns on existing tables.

### Step 7.1 — Schema Changes

**Focuses** — add one column:

```sql
ALTER TABLE focuses ADD COLUMN completion_reward TEXT;
```

The `completion_reward` block is the Paradox Script that fires when a focus
completes. Example from `generic_focus`:

```
completion_reward = {
    add_political_power = 100
    add_stability = 0.05
}
```

For complex focuses (e.g., Germany's Anschluss) this can be 50+ lines with
event triggers, state transfers, and DLC conditionals.

**Ideas** — add three columns:

```sql
ALTER TABLE ideas ADD COLUMN on_add_effect TEXT;
ALTER TABLE ideas ADD COLUMN on_remove_effect TEXT;
ALTER TABLE ideas ADD COLUMN allowed_condition TEXT;
```

- `on_add_effect` — fires when the idea is added to a country
- `on_remove_effect` — fires when the idea is removed
- `allowed_condition` — prerequisite conditions (DLC checks, country restrictions)

**Decisions** — add five columns:

```sql
ALTER TABLE decisions ADD COLUMN allowed TEXT;
ALTER TABLE decisions ADD COLUMN available TEXT;
ALTER TABLE decisions ADD COLUMN visible TEXT;
ALTER TABLE decisions ADD COLUMN complete_effect TEXT;
ALTER TABLE decisions ADD COLUMN remove_effect TEXT;
```

- `allowed` — prerequisites to see the decision at all
- `available` — conditions for the decision to be clickable
- `visible` — visibility conditions (often DLC guards)
- `complete_effect` — what happens when the decision completes
- `remove_effect` — what happens when the decision's timer expires

Apply to live DB:

```sql
ALTER TABLE focuses ADD COLUMN completion_reward TEXT;
ALTER TABLE ideas ADD COLUMN on_add_effect TEXT;
ALTER TABLE ideas ADD COLUMN on_remove_effect TEXT;
ALTER TABLE ideas ADD COLUMN allowed_condition TEXT;
ALTER TABLE decisions ADD COLUMN allowed TEXT;
ALTER TABLE decisions ADD COLUMN available TEXT;
ALTER TABLE decisions ADD COLUMN visible TEXT;
ALTER TABLE decisions ADD COLUMN complete_effect TEXT;
ALTER TABLE decisions ADD COLUMN remove_effect TEXT;
```

Update `sql/schema.sql` inline — add the new columns to the existing CREATE TABLE statements.

### Step 7.2 — Parser Updates

**`parse_focuses_all()`** — currently extracts `id`, `x`, `y`, `cost`, `icon`,
prerequisites, and mutually_exclusive. Add extraction of `completion_reward`:

```python
# After existing field extraction:
cr_match = extract_block(focus_body, "completion_reward")
row["completion_reward"] = cr_match.strip() if cr_match else None
```

The `extract_block()` utility already handles nested brace-matched blocks.
This returns the full raw text between the outermost `{ }`.

**`parse_ideas_all()`** — currently skips `on_add`, `on_remove`, `allowed` in
`skip_keys`. Remove them from skip_keys and extract instead:

```python
row["on_add_effect"] = extract_block(idea_body, "on_add")
row["on_remove_effect"] = extract_block(idea_body, "on_remove")
row["allowed_condition"] = extract_block(idea_body, "allowed")
```

**`parse_decisions_all()`** — currently extracts only `decision_key`,
`category_key`, `icon`, `cost`, `fire_only_once`, `dlc_source`. Add:

```python
row["allowed"] = extract_block(decision_body, "allowed")
row["available"] = extract_block(decision_body, "available")
row["visible"] = extract_block(decision_body, "visible")
row["complete_effect"] = extract_block(decision_body, "complete_effect")
row["remove_effect"] = extract_block(decision_body, "remove_effect")
```

### Step 7.3 — Re-extract & Regenerate

```bash
python tools/db_etl/export_markdown_dump.py
python tools/db_etl/md_to_csv.py
python tools/db_etl/gen_seed_sql.py
python tools/db_etl/gen_seed_docker.py
```

Reload into PostgreSQL and verify the new columns are populated:

```sql
SELECT focus_id, length(completion_reward) AS reward_len
FROM focuses WHERE completion_reward IS NOT NULL
LIMIT 5;

SELECT idea_key, length(on_add_effect) AS effect_len
FROM ideas WHERE on_add_effect IS NOT NULL
LIMIT 5;

SELECT decision_key, length(complete_effect) AS effect_len
FROM decisions WHERE complete_effect IS NOT NULL
LIMIT 5;
```

### Step 7.4 — Update Views

**`api_focus_tree_detail`** — add `completion_reward` to the jsonb sub-select:

```sql
-- In the focuses jsonb_agg subquery, add:
f.completion_reward
```

**`api_ideas_detail`** — add `on_add_effect`, `on_remove_effect`, `allowed_condition`:

```sql
-- Add to the SELECT list:
i.on_add_effect, i.on_remove_effect, i.allowed_condition
```

No new views needed.

### Step 7.5 — Update API Schemas & Test

**Pydantic schemas:**

```python
# api/app/schemas/focus.py — add to FocusItem:
completion_reward: str | None = None

# api/app/schemas/idea.py — add to IdeaDetail:
on_add_effect: str | None = None
on_remove_effect: str | None = None
allowed_condition: str | None = None

# api/app/schemas/dlc.py or new decisions schema — add:
allowed: str | None = None
available: str | None = None
visible: str | None = None
complete_effect: str | None = None
remove_effect: str | None = None
```

No router changes needed — existing routers already use `SELECT *` or full
column lists from the views, so the new columns flow through automatically
once the views are updated. Just add the fields to the Pydantic schemas.

### Test Gate: Phase 7

```python
# test_focus_effects.py
async def test_focus_has_completion_reward(client):
    """At least one focus in Germany's tree has a completion_reward."""
    resp = await client.get("/api/v1/focus-trees", params={"country_tag": "GER"})
    assert resp.status_code == 200
    trees = resp.json()
    rewards = [f for t in trees for f in t["focuses"]
               if f.get("completion_reward")]
    assert len(rewards) > 0

# test_idea_effects.py
async def test_idea_has_on_add_effect(client):
    """At least one idea has an on_add_effect."""
    resp = await client.get("/api/v1/ideas")
    assert resp.status_code == 200
    ideas = resp.json()
    with_effects = [i for i in ideas if i.get("on_add_effect")]
    assert len(with_effects) > 0
```

**Exit criteria:** completion_reward populated for ~80%+ of non-generic focuses. on_add_effect populated for a meaningful subset of ideas. Decision effects populated. New fields appear in Swagger docs and GraphQL schema.

---

## Phase 8: Wargoal Type Definitions

Small, self-contained phase. One new table, one new parser.

### Step 8.1 — Schema

```sql
-- ============================================================
-- Phase 8: Wargoal Types
-- ============================================================

CREATE TABLE wargoal_types (
    wargoal_key         VARCHAR(80) PRIMARY KEY,
    war_name_key        VARCHAR(200),          -- localisation key
    generate_cb_type    VARCHAR(80),           -- e.g. 'annex_everything'
    icon                INT,
    peace_action_type   VARCHAR(80),           -- e.g. 'take_states', 'puppet'
    allowed_block       TEXT,                  -- raw Paradox Script
    visibility_block    TEXT,                  -- raw Paradox Script
    dlc_source          VARCHAR(50)
);
```

**Game files:** `common/wargoals/*.txt`

Example Paradox Script:

```
take_state = {
    war_name = WAR_NAME_TAKE_STATE
    generate_cb_type = take_state
    icon = 1
    allowed { ... }
    visibility { ... }
}
```

### Step 8.2 — Parser

New function `parse_wargoal_types()` in `export_markdown_dump.py`:

```python
def parse_wargoal_types(hoi4_root, out_dir):
    """Parse common/wargoals/*.txt → wargoal_types table."""
    wargoal_dir = os.path.join(hoi4_root, "common", "wargoals")
    rows = []
    for fname in sorted(os.listdir(wargoal_dir)):
        if not fname.endswith(".txt"):
            continue
        path = os.path.join(wargoal_dir, fname)
        content = open(path, encoding="utf-8-sig").read()
        for block_name, block_body in find_top_level_blocks(content):
            row = {
                "wargoal_key": block_name,
                "war_name_key": extract_value(block_body, "war_name"),
                "generate_cb_type": extract_value(block_body, "generate_cb_type"),
                "icon": extract_int(block_body, "icon"),
                "peace_action_type": extract_value(block_body, "peace_action_type"),
                "allowed_block": extract_block(block_body, "allowed"),
                "visibility_block": extract_block(block_body, "visibility"),
                "dlc_source": current_dlc,
            }
            rows.append(row)
    write_md_table(out_dir, "wargoal_types", rows)
```

**Expected row count:** ~10-20 wargoal types.

### Step 8.3 — Extract, CSV, Seed

```bash
python tools/db_etl/export_markdown_dump.py    # adds wargoal_types.md
python tools/db_etl/md_to_csv.py               # adds wargoal_types.csv
python tools/db_etl/gen_seed_sql.py            # regenerate seed with new table
python tools/db_etl/gen_seed_docker.py
```

### Step 8.4 — API Router + Schema + Tests

**Schema** (`api/app/schemas/wargoal.py`):

```python
from pydantic import BaseModel

class WargoalType(BaseModel):
    wargoal_key: str
    war_name_key: str | None = None
    generate_cb_type: str | None = None
    icon: int | None = None
    peace_action_type: str | None = None
    allowed_block: str | None = None
    visibility_block: str | None = None
    dlc_source: str | None = None
```

**Router** — add to existing `dlc.py` or create `wargoals.py`:

```python
@router.get("/api/v1/wargoals", response_model=list[WargoalType], tags=["Wargoals"])
async def list_wargoal_types(db=Depends(get_db)):
    rows = await db.fetch("SELECT * FROM wargoal_types ORDER BY wargoal_key")
    return [dict(r) for r in rows]

@router.get("/api/v1/wargoals/{key}", response_model=WargoalType, tags=["Wargoals"])
async def get_wargoal_type(key: str, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM wargoal_types WHERE wargoal_key = $1", key
    )
    if not row:
        raise HTTPException(404, detail="Wargoal type not found")
    return dict(row)
```

**GraphQL** — add `wargoals` resolver:

```python
@strawberry.type
class WargoalType:
    wargoal_key: str
    war_name_key: str | None
    ...

class Query:
    @strawberry.field
    async def wargoals(self, info) -> list[WargoalType]:
        ...
```

### Test Gate: Phase 8

```python
# test_wargoals.py (3 tests)
async def test_list_wargoals_200(client):
    resp = await client.get("/api/v1/wargoals")
    assert resp.status_code == 200
    assert len(resp.json()) > 0

async def test_wargoal_detail(client):
    resp = await client.get("/api/v1/wargoals")
    key = resp.json()[0]["wargoal_key"]
    detail = await client.get(f"/api/v1/wargoals/{key}")
    assert detail.status_code == 200
    assert detail.json()["wargoal_key"] == key

async def test_wargoal_404(client):
    resp = await client.get("/api/v1/wargoals/nonexistent_xyz")
    assert resp.status_code == 404
```

**Exit criteria:** wargoal_types table populated, REST + GraphQL endpoints working.

---

## Phase 9: Starting Diplomatic State

Medium complexity — new tables, new parser, extends existing country history parser.

### Step 9.1 — Schema

```sql
-- ============================================================
-- Phase 9: Starting Diplomacy
-- ============================================================

CREATE TABLE diplomatic_relations (
    relation_id     SERIAL PRIMARY KEY,
    tag1            CHAR(3) NOT NULL REFERENCES countries(tag),
    tag2            CHAR(3) NOT NULL REFERENCES countries(tag),
    relation_type   VARCHAR(30) NOT NULL,
    -- Types: 'guarantee', 'non_aggression_pact', 'military_access',
    --        'puppet', 'dominion', 'mandate', 'wargoal'
    autonomy_type   VARCHAR(50),           -- for subject relations: 'puppet', 'dominion', etc.
    date            DATE NOT NULL,         -- when this relation takes effect
    dlc_source      VARCHAR(50),
    CONSTRAINT chk_diplo_tags CHECK (tag1 <> tag2)
);

CREATE INDEX ix_diplo_tag1 ON diplomatic_relations(tag1);
CREATE INDEX ix_diplo_tag2 ON diplomatic_relations(tag2);
CREATE INDEX ix_diplo_type ON diplomatic_relations(relation_type);

CREATE TABLE starting_factions (
    faction_id      SERIAL PRIMARY KEY,
    faction_name    VARCHAR(100) NOT NULL,  -- e.g. 'axis', 'allies', 'comintern'
    leader_tag      CHAR(3) NOT NULL REFERENCES countries(tag),
    date            DATE NOT NULL,
    dlc_source      VARCHAR(50)
);

CREATE TABLE starting_faction_members (
    faction_id      INT NOT NULL REFERENCES starting_factions(faction_id),
    member_tag      CHAR(3) NOT NULL REFERENCES countries(tag),
    date            DATE NOT NULL,
    PRIMARY KEY (faction_id, member_tag)
);
```

### Step 9.2 — Parser

**Game files:** Two sources.

**Source A — `history/diplomacy/*.txt`:**

Simple flat files with blocks like:

```
guarantee = {
    first = ENG
    second = POL
    start_date = 1939.3.31
    end_date = 1948.1.1
}

non_aggression_pact = {
    first = GER
    second = SOV
    start_date = 1939.8.23
    end_date = 1949.1.1
}
```

**New parser function `parse_diplomacy_relations()`:**

```python
def parse_diplomacy_relations(hoi4_root, out_dir):
    """Parse history/diplomacy/*.txt → diplomatic_relations."""
    diplo_dir = os.path.join(hoi4_root, "history", "diplomacy")
    rows = []
    relation_types = {
        "guarantee", "non_aggression_pact", "military_access",
        "puppet", "embargo", "give_military_access"
    }
    for fname in sorted(os.listdir(diplo_dir)):
        if not fname.endswith(".txt"):
            continue
        content = open(os.path.join(diplo_dir, fname), encoding="utf-8-sig").read()
        for block_name, block_body in find_top_level_blocks(content):
            if block_name in relation_types:
                tag1 = extract_value(block_body, "first")
                tag2 = extract_value(block_body, "second")
                date_str = extract_value(block_body, "start_date")
                rows.append({
                    "tag1": tag1,
                    "tag2": tag2,
                    "relation_type": block_name,
                    "autonomy_type": None,
                    "date": _pdx_date_to_iso(date_str) if date_str else "1936-01-01",
                    "dlc_source": None,
                })
    write_md_table(out_dir, "diplomatic_relations", rows)
```

**Source B — `history/countries/*.txt` (extend `parse_country_history()`):**

The existing parser processes country history files but skips diplomatic
commands. Extend it to also extract:

- `create_faction = "Axis"` → insert into `starting_factions`
- `add_to_faction = GER` → insert into `starting_faction_members`
- `set_autonomy = { target = TAG autonomy_state = ... }` → insert into `diplomatic_relations` with `relation_type = 'subject'`
- `give_guarantee = TAG` → insert into `diplomatic_relations` with `relation_type = 'guarantee'`

Faction commands are tricky — they appear across multiple country files (Germany creates Axis, then other files add members). The parser must:
1. First pass: collect all `create_faction` commands → build faction lookup
2. Second pass: collect `add_to_faction` → match to faction by leader tag

**Expected row counts:**
- ~50-100 diplomatic relations (guarantees, NAPs, access agreements)
- ~3-5 starting factions (Axis, Allies, Comintern + maybe DLC factions)
- ~20-30 faction members

### Step 9.3 — Extract, CSV, Seed

Standard pipeline. New files:
- `docs/data-dump/diplomatic_relations.md`
- `docs/data-dump/starting_factions.md`
- `docs/data-dump/starting_faction_members.md`
- `data/csv/diplomatic_relations.csv`
- `data/csv/starting_factions.csv`
- `data/csv/starting_faction_members.csv`

### Step 9.4 — API Router + Schema + Tests

**Schema** (`api/app/schemas/diplomacy.py`):

```python
from pydantic import BaseModel

class DiplomaticRelation(BaseModel):
    relation_id: int
    tag1: str
    tag2: str
    relation_type: str
    autonomy_type: str | None = None
    date: str
    dlc_source: str | None = None

class FactionMember(BaseModel):
    member_tag: str
    date: str

class StartingFaction(BaseModel):
    faction_id: int
    faction_name: str
    leader_tag: str
    date: str
    members: list[FactionMember] = []
```

**Router** (`api/app/routers/diplomacy.py`):

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/diplomacy` | List all diplomatic relations |
| GET | `/api/v1/diplomacy?tag=GER` | Filter by country tag (either side) |
| GET | `/api/v1/diplomacy?type=guarantee` | Filter by relation type |
| GET | `/api/v1/factions/starting` | List starting factions with members |

**View** (`sql/views.sql`):

```sql
CREATE OR REPLACE VIEW api_starting_factions AS
SELECT
    sf.faction_id,
    sf.faction_name,
    sf.leader_tag,
    sf.date,
    COALESCE(jsonb_agg(
        jsonb_build_object('member_tag', sfm.member_tag, 'date', sfm.date)
    ) FILTER (WHERE sfm.member_tag IS NOT NULL), '[]'::jsonb) AS members
FROM starting_factions sf
LEFT JOIN starting_faction_members sfm USING (faction_id)
GROUP BY sf.faction_id, sf.faction_name, sf.leader_tag, sf.date;
```

### Test Gate: Phase 9

```python
# test_diplomacy.py (6 tests)
async def test_list_diplomacy_200(client):
    resp = await client.get("/api/v1/diplomacy")
    assert resp.status_code == 200
    assert len(resp.json()) > 0

async def test_diplomacy_filter_by_tag(client):
    resp = await client.get("/api/v1/diplomacy", params={"tag": "ENG"})
    assert resp.status_code == 200
    for r in resp.json():
        assert "ENG" in (r["tag1"], r["tag2"])

async def test_diplomacy_filter_by_type(client):
    resp = await client.get("/api/v1/diplomacy", params={"type": "guarantee"})
    assert resp.status_code == 200
    for r in resp.json():
        assert r["relation_type"] == "guarantee"

async def test_starting_factions_200(client):
    resp = await client.get("/api/v1/factions/starting")
    assert resp.status_code == 200
    factions = resp.json()
    assert len(factions) >= 1
    assert any(f["faction_name"] for f in factions)

async def test_faction_has_members(client):
    resp = await client.get("/api/v1/factions/starting")
    factions = resp.json()
    # At least one faction should have members
    with_members = [f for f in factions if len(f["members"]) > 0]
    assert len(with_members) > 0

async def test_no_self_relations(client):
    """No country has a diplomatic relation with itself."""
    resp = await client.get("/api/v1/diplomacy")
    for r in resp.json():
        assert r["tag1"] != r["tag2"]
```

**Exit criteria:** Diplomatic relations populated from `history/diplomacy/` and country history. Starting factions with members queryable. Date filtering works (1936 vs 1939 shows different relations).

---

## Phase 10: Events

The largest phase — hundreds of event files, potentially thousands of events.

### Step 10.1 — Schema

```sql
-- ============================================================
-- Phase 10: Events
-- ============================================================

CREATE TABLE events (
    event_key           VARCHAR(120) PRIMARY KEY,  -- e.g. 'germany.1', 'news_event.1'
    event_type          VARCHAR(30) NOT NULL,       -- 'country_event', 'news_event'
    title_key           VARCHAR(200),               -- localisation key
    description_key     VARCHAR(200),               -- localisation key
    is_triggered_only   BOOLEAN DEFAULT FALSE,
    is_hidden           BOOLEAN DEFAULT FALSE,
    is_fire_only_once   BOOLEAN DEFAULT FALSE,
    trigger_block       TEXT,                       -- raw Paradox Script
    immediate_block     TEXT,                       -- raw Paradox Script
    mean_time_block     TEXT,                       -- raw MTTH block
    source_file         TEXT NOT NULL,
    dlc_source          VARCHAR(50)
);

CREATE TABLE event_options (
    event_option_id     SERIAL PRIMARY KEY,
    event_key           VARCHAR(120) NOT NULL REFERENCES events(event_key),
    option_name_key     VARCHAR(200),              -- localisation key (button text)
    option_index        INT NOT NULL,              -- display order within event
    ai_chance_block     TEXT,                      -- raw AI weight
    effect_block        TEXT                       -- raw Paradox Script
);

CREATE INDEX ix_event_options_event ON event_options(event_key);
```

**Why only 2 tables (not 3)?**

An `event_files` table was considered but adds no queryable value — the
`source_file` column on `events` captures the same info. Keep it simple.

### Step 10.2 — Parser

New function `parse_events()` in `export_markdown_dump.py`.

**Game file structure:**

```
# events/Germany.txt
country_event = {
    id = germany.1
    title = germany.1.t
    desc = germany.1.d
    is_triggered_only = yes

    immediate = {
        hidden_effect = { ... }
    }

    option = {
        name = germany.1.a
        ai_chance = { factor = 90 }
        GER = { transfer_state = 4 }
    }

    option = {
        name = germany.1.b
        ai_chance = { factor = 10 }
        add_political_power = -100
    }
}
```

**Parser approach:**

```python
def parse_events(hoi4_root, out_dir):
    """Parse events/*.txt → events + event_options tables."""
    events_dir = os.path.join(hoi4_root, "events")
    event_rows = []
    option_rows = []
    event_types = {"country_event", "news_event"}

    for fname in sorted(os.listdir(events_dir)):
        if not fname.endswith(".txt"):
            continue
        path = os.path.join(events_dir, fname)
        content = open(path, encoding="utf-8-sig").read()

        for block_name, block_body in find_top_level_blocks(content):
            if block_name not in event_types:
                continue
            event_id = extract_value(block_body, "id")
            if not event_id:
                continue

            event_rows.append({
                "event_key": event_id,
                "event_type": block_name,
                "title_key": extract_value(block_body, "title"),
                "description_key": extract_value(block_body, "desc"),
                "is_triggered_only": "is_triggered_only" in block_body,
                "is_hidden": "hidden = yes" in block_body,
                "is_fire_only_once": "fire_only_once = yes" in block_body,
                "trigger_block": extract_block(block_body, "trigger"),
                "immediate_block": extract_block(block_body, "immediate"),
                "mean_time_block": extract_block(block_body, "mean_time_to_happen"),
                "source_file": fname,
                "dlc_source": None,  # detect from path if under dlc/
            })

            # Extract options (can have multiple)
            option_idx = 0
            for opt_body in extract_all_blocks(block_body, "option"):
                option_rows.append({
                    "event_key": event_id,
                    "option_name_key": extract_value(opt_body, "name"),
                    "option_index": option_idx,
                    "ai_chance_block": extract_block(opt_body, "ai_chance"),
                    "effect_block": opt_body,
                })
                option_idx += 1

    write_md_table(out_dir, "events", event_rows)
    write_md_table(out_dir, "event_options", option_rows)
```

**New utility needed:** `extract_all_blocks(content, key)` — returns a list of
all blocks matching the key (unlike `extract_block()` which returns the first).
Needed because events have multiple `option = { }` blocks.

**DLC events:** DLC event files live under `dlc/*/events/` (e.g.,
`dlc/mtg/events/MTG_Britain.txt`). The parser must also scan DLC directories
and set `dlc_source` accordingly.

**Expected row counts:**
- ~1,000-3,000 events
- ~3,000-8,000 event options

### Step 10.3 — Extract, CSV, Seed

New files:
- `docs/data-dump/events.md` (may need splitting if >10K rows)
- `docs/data-dump/event_options.md`
- `data/csv/events.csv`
- `data/csv/event_options.csv`

### Step 10.4 — API Router + Schema + Tests

**Schema** (`api/app/schemas/event.py`):

```python
from pydantic import BaseModel

class EventOption(BaseModel):
    event_option_id: int
    option_name_key: str | None = None
    option_index: int
    ai_chance_block: str | None = None
    effect_block: str | None = None

class EventSummary(BaseModel):
    event_key: str
    event_type: str
    title_key: str | None = None
    is_triggered_only: bool
    is_hidden: bool
    source_file: str
    dlc_source: str | None = None

class EventDetail(BaseModel):
    event_key: str
    event_type: str
    title_key: str | None = None
    description_key: str | None = None
    is_triggered_only: bool
    is_hidden: bool
    is_fire_only_once: bool
    trigger_block: str | None = None
    immediate_block: str | None = None
    mean_time_block: str | None = None
    source_file: str
    dlc_source: str | None = None
    options: list[EventOption] = []
```

**Router** (`api/app/routers/events.py`):

| Method | Path | Params | Description |
|--------|------|--------|-------------|
| GET | `/api/v1/events` | `?type=country_event&source_file=Germany.txt&limit=50&offset=0` | List events (paginated) |
| GET | `/api/v1/events/{key}` | — | Event detail with options |

**View** (`sql/views.sql`):

```sql
CREATE OR REPLACE VIEW api_event_detail AS
SELECT
    e.event_key,
    e.event_type,
    e.title_key,
    e.description_key,
    e.is_triggered_only,
    e.is_hidden,
    e.is_fire_only_once,
    e.trigger_block,
    e.immediate_block,
    e.mean_time_block,
    e.source_file,
    e.dlc_source,
    COALESCE(jsonb_agg(
        jsonb_build_object(
            'event_option_id', eo.event_option_id,
            'option_name_key', eo.option_name_key,
            'option_index', eo.option_index,
            'ai_chance_block', eo.ai_chance_block,
            'effect_block', eo.effect_block
        ) ORDER BY eo.option_index
    ) FILTER (WHERE eo.event_option_id IS NOT NULL), '[]'::jsonb) AS options
FROM events e
LEFT JOIN event_options eo USING (event_key)
GROUP BY e.event_key;
```

### Test Gate: Phase 10

```python
# test_events.py (5 tests)
async def test_list_events_200(client):
    resp = await client.get("/api/v1/events")
    assert resp.status_code == 200
    assert len(resp.json()) > 0

async def test_event_detail_has_options(client):
    """Find an event and verify it has options."""
    list_resp = await client.get("/api/v1/events", params={"limit": 1})
    key = list_resp.json()[0]["event_key"]
    resp = await client.get(f"/api/v1/events/{key}")
    assert resp.status_code == 200
    assert "options" in resp.json()

async def test_event_filter_by_type(client):
    resp = await client.get("/api/v1/events", params={"type": "country_event"})
    assert resp.status_code == 200
    for e in resp.json():
        assert e["event_type"] == "country_event"

async def test_event_404(client):
    resp = await client.get("/api/v1/events/nonexistent_event_xyz")
    assert resp.status_code == 404

async def test_event_graphql(client):
    query = '{ events(limit: 3) { eventKey eventType options { optionNameKey } } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    assert "errors" not in resp.json()
```

**Exit criteria:** Events and options extracted from base game + DLCs. REST + GraphQL endpoints working. Swagger docs show event models.

---

## Phase 11: Decision Scripted Effects

Simple extension — the `decisions` table already exists, just needs the TEXT
columns added in Phase 7's schema changes. This phase handles any remaining
parser/API work specific to decisions.

### Step 11.1 — Schema Changes

Already applied in Phase 7 (the ALTER TABLE statements for `allowed`,
`available`, `visible`, `complete_effect`, `remove_effect`).

If Phase 7 didn't handle decisions (implemented as a separate phase), apply:

```sql
ALTER TABLE decisions ADD COLUMN allowed TEXT;
ALTER TABLE decisions ADD COLUMN available TEXT;
ALTER TABLE decisions ADD COLUMN visible TEXT;
ALTER TABLE decisions ADD COLUMN complete_effect TEXT;
ALTER TABLE decisions ADD COLUMN remove_effect TEXT;
```

### Step 11.2 — Parser Updates

Extend `parse_decisions_all()` to extract the five raw text blocks (same
approach as Phase 7 ideas).

### Step 11.3 — Re-extract & Regenerate

Standard pipeline. Verify population:

```sql
SELECT decision_key, length(complete_effect) AS len
FROM decisions WHERE complete_effect IS NOT NULL
LIMIT 5;
```

### Step 11.4 — Update API Schemas & Test

Add the five new optional fields to the decisions Pydantic schema. The existing
router should pick them up automatically.

### Test Gate: Phase 11

```python
async def test_decision_has_effects(client):
    """At least one decision has a complete_effect."""
    # Query decisions directly if there's an endpoint, or via DB
    ...
```

**Exit criteria:** Decision effects populated. Existing decision endpoints return new fields.

---

## Phase 12: Polish & Integration

### Step 12.1 — Update Documentation

- `docs/hoi4-database-design.md` — update table count, row count, add new phases
- `docs/hoi4-table-catalog.md` — add column specs for new tables/columns
- `docs/hoi4-source-to-table-map.md` — add `events/*.txt`, `history/diplomacy/`, `common/wargoals/`
- `docs/hoi4-er-diagram.md` — add new entities and relationships
- `README.md` — update counts
- `sql/README.md` — update counts
- `tools/db_etl/manifest.md` — add new parser modules
- `tools/db_etl/runbook.md` — update counts

### Step 12.2 — Regenerate Seed SQL

```bash
python tools/db_etl/gen_seed_sql.py
python tools/db_etl/gen_seed_docker.py
```

Ensure new tables are in the correct FK tier.

### Step 12.3 — Full Test Suite + Smoke Tests

```bash
cd api
pytest tests/ -v --tb=short
bash ../tools/smoke-test.sh     # update with new endpoints first
```

### Final Test Gate

**Exit criteria:**
- All automated tests pass (target: ~125+ tests)
- All new endpoints appear in Swagger docs
- GraphQL schema includes new types
- `smoke-test.sh` updated and passes
- Documentation consistent across all files

---

## Summary: Implementation Order & Dependencies

```
Phase 7   Focus/idea/decision scripted effects (ALTER existing tables)
   │      └─ TEST GATE: effects populated, API returns new fields
   │
Phase 8   Wargoal types (new table, independent)
   │      └─ TEST GATE: wargoals queryable
   │
Phase 9   Starting diplomacy (new tables, FK → countries)
   │      └─ TEST GATE: relations + factions queryable
   │
Phase 10  Events (new tables, largest dataset)
   │      └─ TEST GATE: events + options queryable
   │
Phase 11  Decision effects (deferred from Phase 7 if needed)
   │      └─ TEST GATE: decision effects populated
   │
Phase 12  Polish (docs, seed, integration)
          └─ FINAL TEST GATE: full suite + smoke
```

**New tables:** 5 (`wargoal_types`, `diplomatic_relations`, `starting_factions`, `starting_faction_members`, `events`, `event_options`) — wait, that's 6. Plus 9 new columns across 3 existing tables.

**New parser functions:** 4 (`parse_wargoal_types`, `parse_diplomacy_relations`, `parse_events`, plus extensions to `parse_focuses_all`, `parse_ideas_all`, `parse_decisions_all`)

**New API files:** 3 routers (`wargoals.py`, `diplomacy.py`, `events.py`), 3 schemas (`wargoal.py`, `diplomacy.py`, `event.py`), 3 test files

**Estimated post-V2 totals:**
- ~157-158 tables (from 151)
- ~230-240K+ game rows (from ~225K)
- ~125+ tests (from 105)
- ~40+ REST endpoints (from 35)
