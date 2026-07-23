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

    snapshot_path = ROOT / "data/snapshot_metrics.json"
    if not snapshot_path.is_file():
        fail("data/snapshot_metrics.json is missing")
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    if snapshot["snapshot_date"] != "2026-06-17":
        fail("unexpected canonical snapshot date")
    for product, expected in {"BUIDL": 76, "OUSG": 69, "bIB01": 32}.items():
        if snapshot[product]["holders_raw"] != expected:
            fail(f"unexpected {product} holder count")
    if snapshot["OUSG"]["aum_ethereum_usd"] is not None:
        fail("OUSG Ethereum AUM must remain null without a retained export")
    if snapshot["bIB01"]["aum_ethereum_usd"] is not None:
        fail("bIB01 Ethereum AUM must remain null without a retained export")
    require_close(snapshot["BUIDL"]["gini_reconstruction"], 0.863, 1e-12, "Gini")

    scripts = [
        "01_framework/scoring_heatmap.py",
        "02_empirical/lorenz_real_data.py",
        "02_empirical/market_comparison.py",
        "02_empirical/aum_timeseries.py",
        "03_gradient/gradient_diagram.py",
        "04_implications/haircut_calculator.py",
    ]
    for relative in scripts:
        py_compile.compile(str(ROOT / relative), doraise=True)

    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    for relative in scripts:
        subprocess.run([sys.executable, relative], cwd=ROOT, env=env, check=True)

    expected_outputs = [
        ROOT / "05_figures/scoring_heatmap.png",
        ROOT / "05_figures/lorenz_buidl.png",
        ROOT / "05_figures/market_comparison.png",
        ROOT / "05_figures/aum_timeseries.png",
        ROOT / "05_figures/aum_timeseries.svg",
        ROOT / "05_figures/gradient_staircase.png",
        ROOT / "05_figures/gradient_staircase.svg",
    ]
    for path in expected_outputs:
        if not path.is_file():
            fail(f"expected generated figure is missing: {path.relative_to(ROOT)}")
        if path.stat().st_size < 1_000:
            fail(f"generated figure appears empty: {path.relative_to(ROOT)}")

    print("Publication validation passed.")


if __name__ == "__main__":
    main()
