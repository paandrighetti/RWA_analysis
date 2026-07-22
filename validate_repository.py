"""Non-mutating repository consistency checks."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
SQL = ROOT / "02_empirical/dune_queries.sql"
ARTICLE = ROOT / "article/article.md"
GUIDE = ROOT / "02_empirical/DUNE_SETUP_GUIDE.md"
METRICS = ROOT / "data/snapshot_metrics.json"
WORKFLOW = ROOT / ".github/workflows/ci.yml"


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def main() -> None:
    required = (ROOT / ".gitignore", README, CHANGELOG, SQL, ARTICLE, GUIDE, METRICS, WORKFLOW)
    removed = (
        ROOT / "02_empirical/onchain_analysis.py",
        ROOT / "article/article_plan_v1.md",
        ROOT / "05_figures/lorenz_buidl_wide.png",
        ROOT / ".github/workflows/figures.yml",
    )
    for path in required:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")
    for path in removed:
        if path.exists():
            fail(f"superseded file still present: {path.relative_to(ROOT)}")

    readme = README.read_text(encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    sql = SQL.read_text(encoding="utf-8")
    article = ARTICLE.read_text(encoding="utf-8")
    guide = GUIDE.read_text(encoding="utf-8")
    workflow = WORKFLOW.read_text(encoding="utf-8")
    active_text = "\n".join((readme, sql, article, guide, workflow))
    forbidden = (
        "CRR Article 401", "I refuse to guess again", "I will stop guessing",
        "IF YOU HAVE A SPECIFIC ERROR", "RWA_HQLA_M7_AUM",
        "no meaningful secondary market exists", "BUIDL ~$181M vs OUSG ~$1.9M",
        "M1 — AUM time-series", "AS aum_tokens",
    )
    for phrase in forbidden:
        if phrase in active_text:
            fail(f"forbidden active phrase remains: {phrase!r}")

    sql_lines = sql.splitlines()
    for index, line in enumerate(sql_lines):
        if "AND block_date >=" not in line:
            continue
        following = sql_lines[index + 1 : index + 5]
        if not any("AND block_date <=" in item or "AND block_time <" in item for item in following):
            fail(f"missing upper snapshot boundary after SQL line {index + 1}")

    if "DATE '2026-06-17'" not in sql:
        fail("canonical snapshot date is missing from SQL")
    if "Article 23(2) of Directive 2009/65/EC" not in article:
        fail("UCITS depositary reference has not been corrected")
    if "activity proxy rather than a direct measure of trading volume" not in article:
        fail("transfer-activity limitation is missing")
    if "## Canonical snapshot boundary" not in guide:
        fail("snapshot section is missing from the Dune guide")
    if "version-1.1.4-blue" not in readme or "RWA HQLA Framework v1.1.4:" not in readme:
        fail("README version markers are not v1.1.4")
    if "## v1.1.4 " not in changelog:
        fail("v1.1.4 changelog entry is missing")
    if "run: python validate_repository.py" not in workflow:
        fail("CI does not run validate_repository.py")
    if "run: python validate_publication.py" not in workflow:
        fail("CI does not regenerate and validate publication figures")

    try:
        json.loads(METRICS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"snapshot_metrics.json is invalid JSON: {exc}")
    print("Repository publication checks passed.")


if __name__ == "__main__":
    main()
