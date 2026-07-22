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


def require_close(value: float, expected: float, tolerance: float, label: str) -> None:
    if abs(value - expected) > tolerance:
        fail(f"{label}: expected {expected}, found {value}")


def main() -> None:
    deleted = [
        ROOT / "article/article_plan_v1.md",
        ROOT / "02_empirical/onchain_analysis.py",
        ROOT / "05_figures/lorenz_buidl_wide.png",
        ROOT / ".github/workflows/figures.yml",
    ]
    for path in deleted:
        if path.exists():
            fail(f"superseded file still exists: {path.relative_to(ROOT)}")

    required = [
        ROOT / ".gitignore",
        ROOT / ".github/workflows/ci.yml",
        ROOT / "data/snapshot_metrics.json",
    ]
    for path in required:
        if not path.exists():
            fail(f"required publication file is missing: {path.relative_to(ROOT)}")

    snapshot = json.loads((ROOT / "data/snapshot_metrics.json").read_text(encoding="utf-8"))
    if snapshot["snapshot_date"] != "2026-06-17":
        fail("unexpected canonical snapshot date")
    expected_holders = {"BUIDL": 76, "OUSG": 69, "bIB01": 32}
    for product, expected in expected_holders.items():
        if snapshot[product]["holders_raw"] != expected:
            fail(f"unexpected {product} holder count")
    if snapshot["OUSG"]["aum_ethereum_usd"] is not None:
        fail("OUSG Ethereum AUM must remain null until a retained source export is published")
    if snapshot["bIB01"]["aum_ethereum_usd"] is not None:
        fail("bIB01 Ethereum AUM must remain null until a retained source export is published")
    require_close(snapshot["BUIDL"]["gini_reconstruction"], 0.863, 1e-12, "Gini reconstruction")
    require_close(snapshot["BUIDL"]["gini_feasible_lower"], 0.850, 1e-12, "Gini lower bound")
    require_close(snapshot["BUIDL"]["gini_feasible_upper"], 0.885, 1e-12, "Gini upper bound")

    matrix = json.loads((ROOT / "01_framework/eligibility_matrix.json").read_text(encoding="utf-8"))
    if matrix["framework"]["version"] not in {"1.1.2", "1.1.3"}:
        fail("unexpected framework version")
    l2_state = matrix["gradient_of_eligibility_roadmap"]["L2"]["current_state"].lower()
    if "esma" not in l2_state or "current" not in l2_state:
        fail("L2 state must refer readers to ESMA's current authorised list")

    limits = json.loads((ROOT / "04_implications/limits_matrix.json").read_text(encoding="utf-8"))
    if limits["framework"]["status"] != "illustrative_stress_scenario_inputs_not_policy":
        fail("limits matrix is not labelled as an illustrative scenario")

    scripts = [
        "01_framework/scoring_heatmap.py",
        "02_empirical/lorenz_real_data.py",
        "02_empirical/market_comparison.py",
        "02_empirical/aum_timeseries.py",
        "03_gradient/gradient_diagram.py",
        "04_implications/haircut_calculator.py",
    ]
    for rel in scripts:
        py_compile.compile(str(ROOT / rel), doraise=True)

    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    for rel in scripts:
        subprocess.run([sys.executable, rel], cwd=ROOT, env=env, check=True)

    active_files = [
        ROOT / "README.md",
        ROOT / "article/article.md",
        ROOT / "01_framework/eligibility_matrix.md",
        ROOT / "01_framework/methodology.md",
        ROOT / "02_empirical/DUNE_SETUP_GUIDE.md",
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
        "Volume is non-existent",
        "explanation is mechanical",
        "thousands of transfers per day",
        "50-60 holders",
        "tweet a screenshot",
        "onchain_analysis.py",
    ]
    for path in active_files:
        text = path.read_text(encoding="utf-8")
        for needle in forbidden:
            if needle in text:
                fail(f"forbidden active wording {needle!r} in {path.relative_to(ROOT)}")

    print("Publication validation passed.")


if __name__ == "__main__":
    main()
