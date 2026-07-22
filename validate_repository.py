"""Non-mutating repository consistency checks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SQL = ROOT / "02_empirical" / "dune_queries.sql"
ARTICLE = ROOT / "article" / "article.md"
GUIDE = ROOT / "02_empirical" / "DUNE_SETUP_GUIDE.md"
METRICS = ROOT / "data" / "snapshot_metrics.json"

REQUIRED_FILES = (
    ROOT / ".gitignore",
    ROOT / ".github" / "workflows" / "ci.yml",
    SQL,
    ARTICLE,
    GUIDE,
    METRICS,
)

REMOVED_FILES = (
    ROOT / "02_empirical" / "onchain_analysis.py",
    ROOT / "article" / "article_plan_v1.md",
    ROOT / "05_figures" / "lorenz_buidl_wide.png",
)

FORBIDDEN_PHRASES = (
    "CRR Article 401",
    "I refuse to guess again",
    "I will stop guessing",
    "RWA_HQLA_M7_AUM",
    "no meaningful secondary market exists",
    "BUIDL ~$181M vs OUSG ~$1.9M",
)


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


for path in REQUIRED_FILES:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

for path in REMOVED_FILES:
    if path.exists():
        fail(f"superseded file still present: {path.relative_to(ROOT)}")

sql = SQL.read_text(encoding="utf-8")
article = ARTICLE.read_text(encoding="utf-8")
guide = GUIDE.read_text(encoding="utf-8")
active_text = sql + "\n" + article + "\n" + guide

for phrase in FORBIDDEN_PHRASES:
    if phrase in active_text:
        fail(f"forbidden phrase remains: {phrase!r}")

sql_lines = sql.splitlines()

for index, line in enumerate(sql_lines):
    if "AND block_date >=" not in line:
        continue

    following_lines = sql_lines[index + 1:index + 5]
    has_upper_boundary = any(
        "AND block_date <=" in candidate
        or "AND block_time <" in candidate
        for candidate in following_lines
    )

    if not has_upper_boundary:
        fail(
            "missing upper snapshot boundary after SQL line "
            f"{index + 1}: {line.strip()}"
        )

if "DATE '2026-06-17'" not in sql:
    fail("canonical snapshot date is missing from SQL")

m7_marker = "-- M7 —"
m7_index = sql.find(m7_marker)

if m7_index == -1:
    fail("M7 section is missing")

m7 = sql[m7_index:]

if "Unified token-supply time series" not in m7:
    fail("M7 is not identified as a token-supply query")

if "AS token_supply_units" not in m7:
    fail("M7 does not expose token_supply_units")

if "It does not calculate USD AUM" not in m7:
    fail("M7 lacks its USD AUM limitation")

if "AS aum_tokens" in m7:
    fail("M7 still exposes aum_tokens")

if "Article 23(2) of Directive 2009/65/EC" not in article:
    fail("UCITS depositary reference has not been corrected")

if "activity proxy rather than a direct measure of trading volume" not in article:
    fail("transfer-activity limitation is missing")

if "## Canonical snapshot boundary" not in guide:
    fail("snapshot section is missing from the Dune guide")

try:
    json.loads(METRICS.read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"snapshot_metrics.json is invalid JSON: {exc}")

print("Repository publication checks passed.")
