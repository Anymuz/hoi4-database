#!/usr/bin/env python3
"""Convert seed-load-order.sql to Docker-compatible COPY commands."""
import re

with open("sql/seed-load-order.sql") as f:
    txt = f.read()

txt = txt.replace("\\set ON_ERROR_STOP on\n", "")

def conv_cols(m):
    table = m.group(1)
    cols = m.group(2)
    path = m.group(3).replace("data/csv/", "/data_csv/")
    opts = m.group(4)
    return f"COPY {table} ({cols}) FROM '{path}' WITH ({opts})"

def conv_nocols(m):
    table = m.group(1)
    path = m.group(2).replace("data/csv/", "/data_csv/")
    opts = m.group(3)
    return f"COPY {table} FROM '{path}' WITH ({opts})"

# Match \copy with column list
txt = re.sub(
    r"\\copy (\S+)\(([^)]+)\) FROM '([^']+)' WITH \(([^)]+)\)",
    conv_cols,
    txt,
)
# Match \copy without column list (staging tables)
txt = re.sub(
    r"\\copy (\S+) FROM '([^']+)' WITH \(([^)]+)\)",
    conv_nocols,
    txt,
)

with open("sql/seed-docker.sql", "w") as f:
    f.write(txt)

print("Done — sql/seed-docker.sql written")
