# Changelog

## v1.1.2 (2026-07-20)

- Article title and conclusions scoped to the three products examined
  (previously generalised to all tokenised RWAs); the supervisory
  sentence made conditional (classification may differ).
- Editorial planning file removed from the tree.
- Figure scripts made runnable from any directory (root-anchored
  output paths under the main guard).
- Data snapshot unchanged (2026-06-17); no measured value changes.

---

## v1.1.1 (2026-07-13) - honesty and consistency pass

- Concentration reporting reframed: Top-3/10/25 shares and the 25 smallest
  balances are measured; the scalar Gini (0.868) is computed on a constrained
  reconstruction. Exact LP bounds under the same constraints give Gini in
  [0.850, 0.885]; the point value moves from 0.866 to 0.868 once the
  intra-Top-3 split is renormalised to the measured 55.22% aggregate; figure legend and all documents updated accordingly.
- Removed the superseded v1.0 illustrative pipeline (`onchain_analysis.py`,
  Pareto placeholders, unverified OUSG address).
- Haircut calculator: corrected the aggregation docstring (multiplicative is
  the LESS conservative bound) and now reports the additive bound alongside.
- Bank implications: corrected the COREP C72 description, split ICAAP/ILAAP
  responsibilities, tightened the bIB01 classification wording.
- Framework wording: cascade rule flagged as a framework convention; gradient
  L3 outcome stated as candidate Level 1 subject to standard criteria.
- Added `requirements.txt`.
- Reconstruction made constraint-exact: the former power-law blocks
  interleaved across the Top-10 boundary (the sorted multiset showed
  Top-10 = 83.5% against the measured 83.02%). Near-flat tilted blocks now
  guarantee every Top-k constraint on the sorted result; the
  reconstruction-dependent scalar moves 0.868 -> 0.863, and the
  assumption-free LP bounds [0.850, 0.885] are the citable quantity.
- Exact LP bounds computation embedded in `lorenz_real_data.py`
  (scipy HiGHS): the [0.850, 0.885] claim is now recomputed at every run
  instead of stated; `requirements.txt` updated accordingly.
- README reproducibility section rewritten (legacy script and notebook
  references removed; the five offline scripts listed).
- Scope disclaimer added (README and article).
- Effective holder count harmonised to ~51 (76 holders, 25 dust).
- Continuous integration workflow added (compile + regenerate all figures).
- Repository hygiene: `.gitignore` added, cached bytecode removed.


---

## v1.1: 2026-06-17

**Empirical data refresh via Dune Analytics queries.**

All concentration and volume metrics in Section 5 of the article have been replaced with directly measured values from the Dune SQL queries in `02_empirical/dune_queries.sql`. The framework verdict is unchanged; the empirical numbers are more precise and more defensible.

### Changes

**Section 3.1 (BUIDL anatomy)**:
- Removed obsolete claim "Ethereum 95% of AUM".
- Added current Ethereum share: ~8% of $2.28B global AUM ($181M on Ethereum mainnet).
- Documented the multi-chain rebalancing away from Ethereum toward Solana and other networks since launch.

**Section 4.3 (Block C empirical)**:
- BUIDL holder count: 54 → 76 (of which ~25 are dust wallets, effective ~50).
- Top-3 share: estimated 63% → measured 55.2%.

**Section 5 (empirical layer)**:
- Gini coefficient: estimated 0.77 → measured **0.866**.
- Top concentration shares: Top-3 = 55%, Top-10 = 83%, Top-25 = 99.5%.
- Volume data: replaced "$0 24h volume" snapshot with cumulative transfer counts (BUIDL: 14,046 total, 3,151 secondary; OUSG: 2,119 / 851; bIB01: 510 / 492).
- **Added bIB01 paradox discussion**: 96% secondary share ratio but only 0.43 transfers per day in absolute terms.
- **Identified BUIDL primary redemption agent**: `0x8780dd016171b91e4df47075da0a947959c34200`, 162 burns totalling $1.51B.
- **Identified secondary redeemer**: `0x54d0a1447e1431db925e871ae799f23f408631a1` (likely Ondo OUSG), 14 burns totalling $411M Aug-Oct 2025, explains the Top-3 share decline.

### Figures

**Figure 2 (Lorenz curve)**: regenerated using real per-holder data from M2-bis Dune query. New Gini = 0.866 (vs estimated 0.77). Curve shape is sharper (more L-shaped) than the previous Pareto fit.

### Methodology evolution

The previous version (v1.0) relied on Pareto-distribution estimates anchored on the historical observation that Ondo OUSG held ~35% of BUIDL in July 2024. These estimates were within the right order of magnitude but the actual distribution is even more concentrated than the Pareto fit predicted, because the tail of the distribution contains many dust wallets (sub-$2 balances) that inflate the holder count without affecting the concentration meaningfully.

### Methodological learning

When reporting concentration metrics for tokenised assets:
- Always distinguish "raw holder count" from "effective holder count" (after dust filtering).
- The secondary transfer ratio is misleading without the absolute count denominator.
- Identify the principal redemption agents, they account for most "transfer activity" but are not peer-to-peer market.

### Reproducibility

All v1.1 numbers are reproducible via:
1. Running M2 in `02_empirical/dune_queries.sql` on Dune (returns the headline shares).
2. Running M2-bis (returns per-holder balances).
3. The M2-bis measured constraints (Top-k shares, 25 smallest balances) are embedded in `02_empirical/lorenz_real_data.py`; running it recomputes the Gini, the exact LP bounds, and the figure.
4. Running M6 (cross-product comparison) for the BUIDL/OUSG/bIB01 transfer counts.

Snapshot date for all v1.1 measurements: **17 June 2026**.

---

## v1.0: 2026-05-11

Initial publication. See `article/article.md` for the full framework, the 24-criteria eligibility matrix in `01_framework/`, and the original Pareto-anchored estimates that v1.1 refines with measured data.

