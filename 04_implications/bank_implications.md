# Implications for Bank Treasurers: An Illustrative Analytical Framework

**Version**: 1.1.2, 2026-07-21

## Why this section matters

Under the assessment in this repository, the three products are not HQLA today. They may still be considered for other permitted balance-sheet purposes, subject to the institution's accounting, legal, prudential and risk-governance framework.

> **Use of this note.** The numerical ranges below are illustrative stress-test inputs for analytical discussion. They are not empirically calibrated recommendations, regulatory haircuts, suitable exposure limits or a model policy for any institution.

## 7.1: Current prudential classification

### Where tokenised treasuries fit in the LCR

Under Regulation (EU) 575/2013 (CRR), the Liquidity Coverage Ratio is computed as: HQLA / Net Cash Outflows over 30-day stress. As established in Sections 4-5, tokenised treasuries (BUIDL, OUSG, bIB01) currently fail Block A and Block C tests for HQLA inclusion. The mechanical consequence:

- **Numerator (HQLA)**: zero contribution. Tokenised treasury holdings cannot be included as Level 1, 2A, or 2B HQLA. They are reported "outside" the LCR numerator.
- **Denominator (Net Cash Outflows)**: no direct impact. Holdings do not create outflow obligations.
- **COREP C72 (liquid assets template)**: non-eligible instruments simply do not enter the C72 liquid-asset rows; there is no catch-all "other assets" HQLA line for them. Any monitoring of the position happens outside the HQLA stack (internal reporting and, where applicable, additional monitoring metrics), which is precisely the operational consequence of ineligibility.

### ILAAP and internal liquidity reporting

Within the Internal Liquidity Adequacy Assessment Process, tokenised treasuries should be classified in a distinct category:

- *Not* cash and equivalents (insufficient settlement finality, restricted transferability)
- *Not* sovereign debt holdings (wrapper introduces issuer and operational risk)
- *Not* conventional corporate bonds for prudential bucketing: bIB01 is issuer debt (a tracker certificate), so the exposure class and risk weight must be confirmed under the applicable CRR provisions rather than assumed
- A new category: "Tokenised RWA" or "Digital Asset Backed Securities", with sub-classification by product type (fund share, debt instrument, structured note)

This classification choice has knock-on effects: internal stress testing, contingency funding plan, ICAAP/ILAAP risk categorisation (capital and operational aspects sit in ICAAP; liquidity, survival horizon and buffer policy sit in ILAAP). The treasury function should treat the establishment of this new category as a deliberate ALM committee decision, not a default operational classification.

### What this means in practice

A €50 million BUIDL holding by a European bank today:
- Contributes €0 to the LCR numerator
- Does not increase outflow obligations
- Should appear in internal liquidity reports under a "Tokenised RWA" line
- Requires a distinct ALM treatment justification documented in policy
- Is subject to operational risk monitoring per ICAAP

The €50 million is therefore a *yielding* asset (with returns aligned to short-term US Treasury yields) that contributes to balance sheet productivity but provides zero regulatory liquidity relief. This is the central trade-off treasurers face.

## 7.2: Internal haircut framework

### The valuation challenge

Since tokenised treasuries are not HQLA, the standard regulatory haircuts (0% Level 1, 15% Level 2A, 25-50% Level 2B) do not apply by reference. But treasurers nonetheless need a way to value the asset for internal liquidity buffer purposes, particularly if the holding is to be considered part of a *contingency* liquidity reserve (even if not LCR-eligible).

The following table illustrates four wrapper-risk components that an institution could test. The ranges are scenario inputs, not calibrated target haircuts:

| Risk component | Haircut range | Rationale |
|---|---|---|
| Custody chain risk | 5-10% | Reflects intermediaries between token and underlying Treasury (BUIDL: 2 layers, OUSG: 3, bIB01: 3). More layers = higher haircut. |
| Settlement finality risk | 10-15% | No SFD coverage; settlement legally finalized at chain confirmation, vulnerable to reorganisation in extreme cases. |
| Contract upgradeability risk | 3-5% | Admin keys risk; pause/freeze functions could be triggered by issuer in stress |
| Issuer concentration risk | 5-10% | Single fund manager (BlackRock for BUIDL), single tokenisation provider (Securitize, Backed Finance), single chain dominance |
| **Cumulative range** | **23-40%** | Envelope across profiles, aggregation method (additive is the conservative bound) and stress overlay; the coded presets sit at roughly 27-32% multiplicative before overlay |

These are not regulatory haircuts. They are internal management adjustments to reflect wrapper-specific risks that the regulatory framework does not yet price.

### Reference point and calibration warning

Level 2B HQLA receives a regulatory haircut of 25-50% when the asset is otherwise eligible. That regulatory treatment is not a calibration source for an ineligible tokenised wrapper. The remaining ranges in this note are illustrative only; the repository does not publish empirical evidence for a universal internal haircut.

### Adjustment dynamics

An institution-specific methodology could include:
- **Quarterly recalibration** by the ALM committee
- **Stress event trigger**: predefined escalation and revaluation procedures following a smart-contract, oracle, custody or pause event; this note does not calibrate the size of the adjustment
- **Regulatory evolution monitoring**: reassessment if the legal structure or prudential classification changes; no automatic reduction is assumed
- **Eurosystem collateral route**: reassessment only if the specific asset becomes eligible and operationally mobilisable; DLT issuance alone does not justify a reduction

## 7.3: Internal limits matrix

### Why limits matter more than haircut

A 25% haircut on a €10 million holding means little. A 25% haircut on a €500 million holding means significant capital and liquidity impact. Concentration limits are the primary control mechanism for tokenised treasury exposure.

The following matrix is an illustrative concentration-stress scenario. Its percentages are not recommended limits:

| Limit dimension | Illustrative scenario input | Rationale to test |
|---|---|---|
| Single-product cap (e.g., BUIDL alone) | 5% of total liquid assets | Avoid material exposure to a single wrapper + issuer |
| Single-issuer cap (e.g., BlackRock-managed) | 10% of total liquid assets | Avoid management concentration |
| Single-chain cap (e.g., Ethereum-deployed) | 25% of total tokenised RWA | Diversify chain risk |
| Single-custodian cap (e.g., Anchorage, Fireblocks) | 33% of total tokenised RWA | Diversify operational custody risk |
| Total tokenised RWA cap | 1-2% of total liquid assets | Aggregate cap pending regulatory clarity |

### Calibration logic

The aggregate and component percentages are included only to make concentration interactions concrete in a stress exercise. They are not inferred from observed loss data and should not be used as policy defaults. A live limit framework would need to be derived from the institution's permitted purpose, redemption and secondary-liquidity tests, legal opinions, operational capacity, capital and liquidity treatment, and risk appetite.

### Caveat: to calibrate per institution

Any institution-specific limits would need to be determined by the relevant governance bodies using evidence on:
- Institution size and complexity
- Existing liquid asset diversification
- Risk appetite framework
- Regulatory dialogue with home supervisor (ACPR, BaFin, CSSF, etc.)
- Operational maturity (custody, monitoring, audit)

No inference should be drawn from the example percentages about an appropriate limit for a G-SIB, another bank, a fintech or an entity outside the LCR perimeter.

## 7.4: Regulatory monitoring checklist

A monitoring framework could cover the following indicators at a frequency determined by the institution:

### EU supervisory developments
- EBA work programme on tokenised HQLA classification
- ECB collateral framework evolution post-30 March 2026 (which subsets of DLT-based assets become eligible next)
- ESMA review of UCITS Eligible Assets Directive (the review starts 2026, conclusion expected 2027)
- ESMA monitoring of MiCAR implementation impact on tokenised assets

### Global supervisory developments
- BCBS work programme on cryptoasset prudential treatment (BCBS 538 + follow-up consultations)
- FSB recommendations on tokenisation
- IOSCO standards on tokenised funds

### US supervisory developments
- FRB/OCC/FDIC interagency guidance evolution post-March 2026 joint FAQ
- SEC Division of Investment Management positions on tokenised funds
- FINRA expectations on broker-dealer activity in tokenised securities
- Federal Reserve Wholesale Settlement work programme

### Market evolution indicators
- New product launches (Superstate, Hashnote, OpenEden, etc.) and their structural choices
- Existing product restructurings (BUIDL share class additions, OUSG fund-of-funds composition changes)
- Cross-border settlement pilots (JPMorgan / Mastercard / Ripple type collaborations)
- DLT Pilot Regime authorisation pipeline (six infrastructures authorised by March 2026; current list maintained by ESMA)

## 7.5: ICAAP/ILAAP risk category mapping

The Internal Capital Adequacy Assessment Process should explicitly map tokenised RWA exposures to standard risk categories:

| ICAAP risk category | Specific risk for tokenised RWA | Mitigation / control |
|---|---|---|
| Liquidity risk | Settlement may delay beyond 30-day window under stress (T+1 BUIDL, T+5 bIB01); whitelist counterparty acceptance may freeze under stress | Internal haircut framework (7.2); single-product caps (7.3); monthly redemption stress testing |
| Market risk | Wrapper-specific basis risk between NAV and on-chain price; oracle valuation lag | Mark-to-NAV with daily reconciliation; oracle quality monitoring |
| Operational risk | Smart contract bug; oracle failure; custody key compromise; chain reorganisation | Custody chain diligence; bug bounty awareness; multi-signature governance; chain selection limited to mature L1 chains |
| Concentration risk | Single issuer / chain / custodian dominance | Internal limits matrix (7.3) |
| Legal risk | Non-bankruptcy-remote structure for some products (bIB01 creditor cascade); jurisdictional uncertainty (BVI for BUIDL, Jersey for bIB01) | Pre-investment legal opinion; documentation review per ALM committee |
| Reputation risk | Public chain transparency means all holdings are visible to competitors and journalists | Communication strategy; coordinated disclosure |

Liquidity-dimension items above belong primarily to the ILAAP. Any ICAAP capital response would depend on the institution-specific materiality, accounting classification, risk measurement, controls and supervisory assessment; this note does not estimate a Pillar 2 capital impact.

## 7.6: Decision framework for a hypothetical treasury review

This section is an analytical checklist, not a recommendation to allocate.

1. **Permitted purpose**: determine whether the exposure is intended for yield, settlement experimentation, client service or another approved purpose. Do not treat it as an HQLA substitute under the present framework.
2. **Product evidence**: review the legal claim, redemption mechanics, insolvency ranking, transfer restrictions, pause and upgrade controls, current prospectus status and any chain-specific terms.
3. **Custody and operational design**: assess regulated custody options, key governance, insurance scope, transaction controls, incident response, reconciliation and the consequences of each additional intermediary. This note does not rank or endorse providers.
4. **Chain and settlement perimeter**: select the chain only after testing settlement finality, operational resilience, liquidity access, supported custody and contingency procedures. This note does not prescribe Ethereum or any other network.
5. **Liquidity testing and limits**: calibrate limits from institution-specific redemption tests, observable secondary depth, concentration, legal opinions and risk appetite. The example ranges elsewhere in this note are stress-test inputs, not target limits.
6. **Monitoring and exit criteria**: define measurable triggers for contract pauses, oracle failures, custody incidents, legal-document changes, loss of redemption access, concentration breaches and regulatory action before entering the position.

The resulting decision depends on the institution's balance-sheet purpose, risk appetite, ALM and risk-committee governance, accounting and prudential treatment, operational maturity and supervisor dialogue. Product comparisons in this repository should not be converted directly into allocations.

## Caveats and limitations

1. This framework is one analyst's proposal. Other analysts may propose different cap percentages, haircut compositions, or product preferences with equally defensible rationales.
2. The framework reflects June 2026 product structures. Any later legal or regulatory change requires a new assessment; no automatic change in haircuts or limits is assumed.
3. The framework focuses on European prudential context (CRR, DR 2015/61, ECB collateral framework). US bank treasurers operating under FRB/OCC/FDIC technology-neutral guidance (March 2026) have a different starting point and may calibrate differently.
4. Fintechs and neo-banks not subject to LCR have more operational flexibility but should still consider the haircut and limits framework for prudent treasury management.

## Sources

- Regulation (EU) 575/2013 (CRR), Articles 411-419
- Commission Delegated Regulation (EU) 2015/61, Articles 7-17
- EBA Guidelines on ILAAP
- BCBS 238 (January 2013): Basel III LCR
- BCBS 538: Prudential treatment of cryptoasset exposures (December 2022, updated 2025)
- ECB Press Release 27 January 2026: DLT-based collateral eligibility
- FRB/OCC/FDIC Joint FAQ 5 March 2026: Capital Treatment of Tokenized Securities
- ESMA Report on DLT Pilot Regime functioning (ESMA75-117376770-460, 25 June 2025)
