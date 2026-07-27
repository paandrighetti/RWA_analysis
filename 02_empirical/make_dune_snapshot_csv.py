"""Flatten data/snapshot_metrics.json into a key-value CSV for Dune upload.

Emits sort_order, metric, value rows from the canonical snapshot file, so the
dashboard's frozen-snapshot panel is generated from the publication record
rather than typed by hand. Null values are kept and rendered as the literal
string "null": they are deliberate under the repository's null policy and the
panel should show them, not hide them.

Skipped on purpose: the _source subtree (prose provenance, documented in the
repository, too long for a table cell) and any *note* field.

Run from the repository root:

    python 02_empirical/make_dune_snapshot_csv.py

Upload the output as the Dune dataset rwa_hqla_snapshot_2026_06_17. Regenerate
and upload under a new dated name only if the canonical snapshot itself is
ever reissued.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

SRC = Path("data/snapshot_metrics.json")
DST = Path("02_empirical/dune_upload_snapshot_2026_06_17.csv")

SKIP_PREFIXES = ("_source",)
SKIP_SUBSTRINGS = ("note",)
MAX_STRING_LEN = 60


def leaves(obj, path=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            child = f"{path}.{key}" if path else key
            yield from leaves(value, child)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from leaves(value, f"{path}[{index}]")
    else:
        yield path, obj


def keep(path: str, value) -> bool:
    lowered = path.lower()
    if any(lowered.startswith(p) for p in SKIP_PREFIXES):
        return False
    if any(s in lowered for s in SKIP_SUBSTRINGS):
        return False
    if isinstance(value, str) and len(value) > MAX_STRING_LEN:
        return False
    return True


def main() -> None:
    if not SRC.exists():
        sys.exit(f"{SRC} missing: run from the repository root")
    data = json.loads(SRC.read_text(encoding="utf-8"))
    rows = [
        (path, "null" if value is None else value)
        for path, value in leaves(data)
        if keep(path, value)
    ]
    with DST.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sort_order", "metric", "value"])
        for order, (path, value) in enumerate(rows, 1):
            writer.writerow([order, path, value])
    print(f"Wrote {DST}: {len(rows)} rows")


if __name__ == "__main__":
    main()
