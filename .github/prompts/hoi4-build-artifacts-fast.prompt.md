---
description: "Execute the HOI4 database project in fast, resumable slices and write all outputs to files (no chat-only deliverables). Design and pre-database pipeline are COMPLETE (127 tables, 23 phases). Focus on standing up PostgreSQL and building the REST API."
mode: agent
agent: HOI4 Database Architect
---

Build the HOI4 database artifacts with a **productivity-first** approach.

**IMPORTANT**: This is a standalone repo. Game files are in a separate HOI4 install directory. Use `--hoi4-root`, `HOI4_ROOT` env var, or auto-detection to locate game files. See `.github/copilot-instructions.md` for details.

## Current State

- **Design: COMPLETE** — 127 tables across 23 phases (66 core + 55 DLC + 6 Doctrines)
- **DDL: COMPLETE** — `sql/schema.sql` has all 127 tables (127 CREATE TABLE, 4 ALTER TABLE, 50 CREATE INDEX)
- **Views: COMPLETE** — `sql/views.sql` has 14 API views across 3 slices
- **ETL: COMPLETE** — extraction (137 markdown files, ~221K rows) + CSV conversion (127 files, ~221K rows) + seed-load-order (live `\copy` commands)
- **Validation: PASSING** — FK, PK, NOT NULL checks — 0 errors, 0 warnings
- **Not yet done**: Stand up PostgreSQL and load data, REST API implementation

**Authoritative design docs** (always read before generating DDL):
- `docs/hoi4-table-catalog.md` — column specs for all 127 tables
- `docs/hoi4-er-diagram.mmd` — Mermaid ER diagram (127 entities, 133 relationships)
- `docs/hoi4-database-design.md` — narrative, FK build order, DLC register

## Execution Policy

- Prioritize shipping usable artifacts quickly over exhaustive prose.
- Work in slices and checkpoint each slice to files.
- Keep chat output brief; files are the source of truth.
- If interrupted, resume from the checkpoint file and continue.
- **Always read the table catalog before generating DDL** — it is the authoritative spec.

## Required Output Files

- `docs/hoi4-database-design.md`
- `docs/hoi4-er-diagram.mmd`
- `sql/schema.sql`
- `sql/views.sql`
- `sql/seed-load-order.sql`
- `tools/db_etl/manifest.md`
- `tools/db_etl/runbook.md`
- `docs/hoi4-build-checkpoint.md`

## Slice Plan

### Slice A — DONE (15 tables)
Core schema for: countries, states, provinces, resources, buildings, ownership/control, technologies.
- `sql/schema.sql` has DDL for these 15 tables.
- `sql/views.sql` has `/countries/{tag}` and `/states/{id}` views.

### Slice B — Remaining Core Tables (Phases 4–15, ~51 tables)
1. Generate DDL for all remaining core tables following FK build order from `docs/hoi4-database-design.md`.
2. Add OOB land/naval/air tables (division templates, fleets, task forces, ships, air wings).
3. Add characters, ideas, focus trees, equipment variants, supply, bookmarks, decisions, autonomy, occupation.
4. Update ER diagram alignment and load order SQL.
5. Update checkpoint status.

### Slice C — DLC Tables (Phases 16–22, ~55 tables)
1. Generate DDL for all DLC tables: espionage, MIOs, raids, medals, BOP, tech sharing, etc.
2. All DLC tables have `dlc_source VARCHAR(50)` where applicable.
3. Update load order SQL for DLC FK dependencies.
4. Update checkpoint status.

### Slice D — ETL & Validation
1. Build ETL parser modules per data domain.
2. Update `tools/db_etl/manifest.md` with module inventory.
3. Update `tools/db_etl/runbook.md` with execution commands.
4. Final alignment pass between ER diagram, catalog, and schema DDL.
5. Mark checkpoint COMPLETE.

## Checkpoint File Format

Always overwrite `docs/hoi4-build-checkpoint.md` with:

```markdown
# HOI4 Build Checkpoint

Status: IN_PROGRESS | COMPLETE
Current Slice: A | B | C | D
Last Updated: <ISO datetime>

Completed:
- ...

Next:
- ...

Blocking Issues:
- none | <issue>
```

## Acceptance Rules

- Never finish with only chat explanation.
- Every completed slice must update files.
- `sql/schema.sql` and `docs/hoi4-er-diagram.mmd` must stay consistent.
- `sql/seed-load-order.sql` must be FK-safe.
- DDL must match column specs in `docs/hoi4-table-catalog.md` exactly.
