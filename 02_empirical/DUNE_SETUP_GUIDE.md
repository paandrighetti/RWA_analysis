# Dune extraction and snapshot update guide

This guide explains how to refresh the on-chain measurements used by the RWA HQLA framework. The published analytical snapshot is dated **17 June 2026**. Downstream scripts run offline from `data/snapshot_metrics.json`; reproducing the original extraction requires executing the SQL in `02_empirical/dune_queries.sql` and retaining the resulting exports.

## Canonical published snapshot

The repository currently expects the following BUIDL concentration constraints on Ethereum mainnet:

- raw holder count: 76;
- effective holder count: approximately 51 after the documented dust filter;
- Top-3 share: 55.2%;
- Top-10 share: 83.0%;
- Top-25 share: 99.5%;
- constrained Gini reconstruction: 0.863;
- exact feasible Gini interval: [0.850, 0.885];
- Ethereum AUM retained in the public snapshot: approximately USD 181.3 million.

OUSG and bIB01 product-specific Ethereum AUM remain `null` in the canonical JSON because the supporting exports are not included in the public repository. Global product or product-suite AUM must not be substituted for a chain-specific value.

## Refresh procedure

1. Review the contract addresses and chain assumptions in `02_empirical/dune_queries.sql` against primary issuer documentation and a block explorer.
2. Run the relevant Dune queries for holder balances, concentration shares, transfer classification and chain-specific supply or AUM.
3. Export each query result with a filename that includes the query identifier and snapshot date, for example `M2_buidl_holders_2026-07-22.csv`.
4. Record the Dune query URL or identifier, execution timestamp, chain, token address, block or date cutoff and any post-processing formula.
5. Reconcile supply, decimals and USD conversion before updating any AUM field. If a product-specific chain value cannot be established from a retained export, leave it `null`.
6. Update `data/snapshot_metrics.json` only after the corresponding export and calculation note have been retained.
7. Run the offline validation and figure-generation commands below.
8. Review the resulting diff. A changed live snapshot is expected to change figures and metrics; it must not silently change regulatory interpretations or historical claims.

Provider quotas and user-interface steps change over time. Consult Dune's current documentation and account dashboard rather than relying on hard-coded limits in this repository.

## Offline validation

```bash
pip install -r requirements.txt
python validate_publication.py
```

The validator compiles and runs the analytical scripts, checks the canonical snapshot and Gini bounds, confirms that deprecated active artifacts remain absent, and verifies selected publication-hygiene rules.

Individual scripts can also be run directly:

```bash
python 01_framework/scoring_heatmap.py
python 02_empirical/lorenz_real_data.py
python 02_empirical/market_comparison.py
python 02_empirical/aum_timeseries.py
python 03_gradient/gradient_diagram.py
python 04_implications/haircut_calculator.py
```

## Interpreting changes

Holder counts, transfer counts and AUM are point-in-time observations and may legitimately change at every refresh. The address-level Gini is not directly comparable with beneficial-owner or account-level concentration measures in traditional securities. Transfers are also not synonymous with trades: issuance, redemption, operational routing, bridges and custody movements must be considered before drawing market-liquidity conclusions.

The Dune dashboard is a current monitoring surface. The dated files and canonical JSON in this repository are the publication record for the article's stated snapshot.

## Canonical snapshot boundary

The published empirical results use a cutoff of **17 June 2026**.

Queries intended to reproduce the publication must include the following upper boundary:

    AND block_date <= DATE '2026-06-17'

The equivalent exclusive timestamp boundary is:

    AND block_time < TIMESTAMP '2026-06-18 00:00:00 UTC'

A query without an upper boundary is a live query and will not reproduce the published snapshot.
Live dashboard queries must be stored separately from the publication queries.
