"""Non-mutating repository consistency checks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
SQL = ROOT / "02_empirical" / "dune_queries.sql"
ARTICLE = ROOT / "article" / "article.md"
GUIDE = ROOT / "02_empirical" / "DUNE_SETUP_GUIDE.md"
METRICS = ROOT / "data" / "snapshot_metrics.json"
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"

REQUIRED_FILES = (
    ROOT / ".gitignore",
    README,
    CHANGELOG,
    SQL,
    ARTICLE,
    GUIDE,
    METRICS,
    WORKFLOW,
)

REMOVED_FILES = (
    ROOT / "02_empirical" / "onchain_analysis.py",
    ROOT / "article" / "article_plan_v1.md",
    ROOT / "05_figures" / "lorenz_buidl_wide.png",
)

FORBIDDEN_ACTIVE_PHRASES = (
    "CRR Article 401",
    "I refuse to guess again",
    "I will stop guessing",
    "IF YOU HAVE A SPECIFIC ERROR",
    "RWA_HQLA_M7_AUM",
    "no meaningful secondary market exists",
    "BUIDL ~$181M vs OUSG ~$1.9M",
    "M1 — AUM time-series",
    "AS aum_tokens",
    "Not HQLA: and What It Would Take",
    "materially more concentrated than that of traditional HQLA reference assets",
    "The overall HQLA verdict requires Pass in Blocks A and C",
)


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


for path in REQUIRED_FILES:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

for path in REMOVED_FILES:
    if path.exists():
        fail(f"superseded file still present: {path.relative_to(ROOT)}")

readme = README.read_text(encoding="utf-8")
changelog = CHANGELOG.read_text(encoding="utf-8")
sql = SQL.read_text(encoding="utf-8")
article = ARTICLE.read_text(encoding="utf-8")
guide = GUIDE.read_text(encoding="utf-8")
workflow = WORKFLOW.read_text(encoding="utf-8")

active_text = "\n".join((readme, sql, article, guide, workflow))

for phrase in FORBIDDEN_ACTIVE_PHRASES:
    if phrase in active_text:
        fail(f"forbidden active phrase remains: {phrase!r}")

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

if "-- RWA HQLA Framework — Dune SQL Queries v1.3" not in sql:
    fail("SQL version is not v1.3")

if "-- Updated 2026-07-22" not in sql:
    fail("SQL update date is not 2026-07-22")

if "DATE '2026-06-17'" not in sql:
    fail("canonical snapshot date is missing from SQL")

m1_marker = "-- M1 —"
m7_marker = "-- M7 —"
m1_index = sql.find(m1_marker)
m7_index = sql.find(m7_marker)

if m1_index == -1 or m7_index == -1:
    fail("M1 or M7 section is missing")

m1 = sql[m1_index:m7_index]
m7 = sql[m7_index:]

if "BUIDL token-supply time series" not in m1:
    fail("M1 is not identified as a BUIDL token-supply query")

if "AS supply_tokens" not in m1:
    fail("M1 does not expose supply_tokens")

if "AS aum_tokens" in m1:
    fail("M1 still exposes aum_tokens")

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

if "The overall HQLA verdict requires an eligible route in Block A" not in article:
    fail("cumulative Block A/B/C verdict logic is missing")

if "Direct comparison with traditional HQLA reference assets is not like-for-like" not in article:
    fail("cross-market concentration qualification is missing")

if "## Canonical snapshot boundary" not in guide:
    fail("snapshot section is missing from the Dune guide")

if "version-1.1.4-blue" not in readme:
    fail("README version badge is not v1.1.4")

if "RWA HQLA Framework v1.1.4:" not in readme:
    fail("README citation version is not v1.1.4")

if "## v1.1.4 " not in changelog:
    fail("v1.1.4 changelog entry is missing")

if "uses: actions/checkout@v6" not in workflow:
    fail("CI does not use actions/checkout@v6")

if "uses: actions/setup-python@v6" not in workflow:
    fail("CI does not use actions/setup-python@v6")

if "run: python validate_repository.py" not in workflow:
    fail("CI does not run validate_repository.py")

if "run: python validate_publication.py" in workflow:
    fail("CI still executes the figure-regenerating validator")

try:
    json.loads(METRICS.read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"snapshot_metrics.json is invalid JSON: {exc}")

print("Repository publication checks passed.")
