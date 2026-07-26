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
    active_version_files = (
        ROOT / "01_framework/scoring_heatmap.py",
        ROOT / "01_framework/methodology.md",
        ROOT / "01_framework/eligibility_matrix.md",
        ROOT / "01_framework/eligibility_matrix.json",
        ROOT / "02_empirical/aum_timeseries.py",
        ROOT / "02_empirical/empirical_findings.md",
        ROOT / "03_gradient/gradient_deepdive.md",
        ROOT / "04_implications/bank_implications.md",
        ROOT / "04_implications/haircut_calculator.py",
        ROOT / "04_implications/limits_matrix.json",
        ARTICLE,
    )
    active_version_text = "\n".join(
        path.read_text(encoding="utf-8") for path in active_version_files
    )
    active_text = "\n".join((readme, sql, article, guide, workflow, active_version_text))
    forbidden = (
        "CRR Article 401", "I refuse to guess again", "I will stop guessing",
        "IF YOU HAVE A SPECIFIC ERROR", "RWA_HQLA_M7_AUM",
        "no meaningful secondary market exists", "BUIDL ~$181M vs OUSG ~$1.9M",
        "M1, AUM time-series", "AS aum_tokens",
        "does not create a secondary market in any meaningful sense",
        "secondary transfers are largely re-routing through this single intermediary",
        "referenced via StreetInsider, CIK pending direct EDGAR fetch",
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
    if "1.1.3" in active_version_text:
        fail("an active publication file still declares version 1.1.3")
    if "## v1.1.4 " not in changelog:
        fail("v1.1.4 changelog entry is missing")
    if "run: python validate_repository.py" not in workflow:
        fail("CI does not run validate_repository.py")
    if "run: python validate_publication.py" not in workflow:
        fail("CI does not regenerate and validate publication figures")

    compiled_artifacts = [
        path for path in ROOT.rglob("*")
        if path.is_file() and ("__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"})
    ]
    if compiled_artifacts:
        fail(
            "compiled Python artifacts are present: "
            + ", ".join(str(path.relative_to(ROOT)) for path in compiled_artifacts[:10])
        )

    try:
        json.loads(METRICS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"snapshot_metrics.json is invalid JSON: {exc}")
    print("Repository publication checks passed.")


if __name__ == "__main__":
    main()
