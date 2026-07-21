from __future__ import annotations

import json
import os
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def main() -> None:
    deleted = [
        ROOT / "article/article_plan_v1.md",
        ROOT / "02_empirical/onchain_analysis.py",
        ROOT / "05_figures/lorenz_buidl_wide.png",
    ]
    for path in deleted:
        if path.exists():
            fail(f"superseded file still exists: {path.relative_to(ROOT)}")

    snapshot = json.loads((ROOT / "data/snapshot_metrics.json").read_text(encoding="utf-8"))
    assert snapshot["snapshot_date"] == "2026-06-17"
    assert snapshot["BUIDL"]["holders_raw"] == 76
    assert snapshot["OUSG"]["holders_raw"] == 69
    assert snapshot["bIB01"]["holders_raw"] == 32
    assert snapshot["OUSG"]["aum_ethereum_usd"] is None
    assert snapshot["bIB01"]["aum_ethereum_usd"] is None
    assert abs(snapshot["BUIDL"]["gini_reconstruction"] - 0.863) < 1e-12

    matrix = json.loads((ROOT / "01_framework/eligibility_matrix.json").read_text(encoding="utf-8"))
    assert matrix["framework"]["version"] == "1.1.2"
    assert "Six DLT market infrastructures" in matrix["gradient_of_eligibility_roadmap"]["L2"]["current_state"]

    limits = json.loads((ROOT / "04_implications/limits_matrix.json").read_text(encoding="utf-8"))
    assert limits["framework"]["status"] == "illustrative_stress_scenario_inputs_not_policy"

    scripts = [
        "01_framework/scoring_heatmap.py",
        "02_empirical/market_comparison.py",
        "02_empirical/aum_timeseries.py",
        "03_gradient/gradient_diagram.py",
        "04_implications/haircut_calculator.py",
    ]
    for rel in scripts:
        py_compile.compile(str(ROOT / rel), doraise=True)

    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    for rel in [
        "01_framework/scoring_heatmap.py",
        "02_empirical/market_comparison.py",
        "03_gradient/gradient_diagram.py",
    ]:
        subprocess.run([sys.executable, rel], cwd=ROOT, env=env, check=True)

    active_files = [
        ROOT / "README.md",
        ROOT / "article/article.md",
        ROOT / "01_framework/eligibility_matrix.md",
        ROOT / "01_framework/methodology.md",
        ROOT / "02_empirical/empirical_findings.md",
        ROOT / "03_gradient/gradient_deepdive.md",
        ROOT / "04_implications/bank_implications.md",
    ]
    forbidden = [
        "lorenz_buidl.png (+_wide)",
        "Conclusions are not opinions",
        "almost certainly operated",
        "source material for Section",
        "Editorial voice",
        "target 400 words",
        "target 600 words",
    ]
    for path in active_files:
        text = path.read_text(encoding="utf-8")
        for needle in forbidden:
            if needle in text:
                fail(f"forbidden active wording {needle!r} in {path.relative_to(ROOT)}")

    print("Publication validation passed.")


if __name__ == "__main__":
    main()
