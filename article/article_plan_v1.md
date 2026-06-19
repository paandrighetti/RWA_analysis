# Article Final — Detailed Plan

**Working title** (to validate): *"Why no tokenized RWA is HQLA — a regulatory gradient analysis of BUIDL, OUSG, and bIB01"*

**Version**: 1.0 — 2026-05-11
**Format**: long-form article, target 4500 words
**Channel**: Mirror (primary), cross-posted GitHub README
**Audience triple targeting**: bank tokenisation desks (FORGE, BNP DA, Sygnum), DeFi risk (Steakhouse, Block Analitica), fintech (Circle, Memo Bank)

## Editorial principles

1. **Verdict first**. Reader has 90 seconds. Section 0 must deliver: 3 products, non-HQLA, here's why, here's what it would take.
2. **Empirical anchor**. Every qualitative claim is paired with a quantified empirical data point (Gini 0.77, $0 volume 24h, 1.72 tx/day) or a primary legal citation (Art. XVII bIB01 Final Terms, DR 2015/61 Art. 7(2)).
3. **No marketing language**. Avoid "revolutionising", "unlocking", "innovative". Use BCBS, ESMA, CRR vocabulary throughout.
4. **One key insight per section**. If a section doesn't have a key insight, kill it.
5. **Code and data behind a click**. The article is the executive layer ; deep dive is in the GitHub repo and Dune dashboard. Don't bury the executive layer in technical detail.

## Section-by-section plan

### Section 0 — Hook + verdict (250 words)

**Key insight**: BlackRock's BUIDL has $2.28B AUM and zero 24h trading volume. This contradiction reveals what tokenization currently is and isn't.

**Open with the contradiction**: BUIDL announcements describe it as "revolutionary 24/7 tokenised liquidity". The on-chain reality shows 54 holders, 1.72 daily transfers, and $0 secondary volume. This is a wholesale institutional product wearing a blockchain wrapper, not a liquid market.

**State the verdict in plain English**: Under Basel III LCR, none of BUIDL, OUSG, or bIB01 qualifies as High-Quality Liquid Assets. Not Level 1. Not Level 2A. Not Level 2B. This is a structural feature of the current wrappers, not a transient growing pain.

**Preview the article**: framework with 24 criteria, three structural disqualifiers identified, gradient of changes required to reach eligibility (L0 → L3), and practical implications for bank treasurers today.

**Visual**: none (textual hook only).

### Section 1 — Why this matters now (350 words)

**Key insight**: European supervisors are in active review mode. EBA published its tokenised deposits report (Dec 2024), ESMA submitted DLT Pilot Regime functioning report (Jun 2025), and the European Commission's review of the Pilot Regime is due March 2026. The window for analytical contributions is open and short.

**Content**:
- Tokenised treasuries market: $0 in early 2023 → $12.88B in April 2026 (cite RWA.xyz)
- BlackRock filed two new tokenised fund offerings on 9 May 2026 (Daily Reinvestment Stablecoin Reserve Vehicle + onchain shares for $7B MMF)
- AFME and supervisors are explicitly asking about ECB collateral eligibility (cite AFME submission April 2025)
- The current cadre Basel III/CRR has not been adapted to tokenised instruments — DR 2015/61 unchanged since 2018/1620 amendment
- This article fills the analytical gap between primary regulatory texts and tokenised product reality

**Visual**: none.

### Section 2 — The framework in 5 minutes (500 words)

**Key insight**: HQLA eligibility is a cascade — first the asset must fall in a category (Block A), then satisfy operational tests (Block B), market tests (Block C), and survive wrapper-specific frictions (Block D). 24 criteria total.

**Content**:
- BCBS 238 origins (2013) and EU transposition via CRR + DR 2015/61
- Three levels: Level 1 (0% haircut), Level 2A (15%), Level 2B (25-50%)
- The two cumulative tests: eligibility category + operational requirements
- Introduce the 4-block framework (A: eligibility category, B: operational, C: market, D: wrapper friction)
- Methodology: Pass/Conditional/Fail/N/A scoring with primary legal references per cell

**Visual**: scoring heatmap (preview/teaser).

### Section 3 — Product anatomy: BUIDL, OUSG, bIB01 (900 words)

**Key insight**: The three products look similar (tokenised treasury exposure) but have radically different legal structures. BUIDL is a fund share. OUSG is a fund-of-funds. bIB01 is a debt instrument tracking an ETF.

**Content** (300 words per product):

**3.1 BUIDL** — BlackRock USD Institutional Digital Liquidity Fund Ltd
- BVI exempted company under Investment Company Act §3(c)(7) + Securities Act Rule 506(c)
- Investment Manager: BlackRock Financial Management Inc (SEC RIA)
- Custodian: BNY Mellon
- Min investment: $5M
- Multi-chain: 8 chains, Ethereum 95% of AUM
- $5M minimum investment, US Qualified Purchasers + non-US institutionals only

**3.2 OUSG** — Ondo Short-Term US Government Treasuries
- Delaware LP, same §3(c)(7) + 506(c) regime as BUIDL
- Fund-of-funds composition: BUIDL primary + Franklin Templeton + WisdomTree + Fidelity + bank deposits
- Coinbase custody for USDC; SEC RIA = Ondo Capital Management LLC
- $5K instant / $100K non-instant minimums
- 5 chains, cross-border settlement validated with JPM/Mastercard/Ripple (6 May 2026)

**3.3 bIB01** — Backed IB01 $ Treasury Bond 0-1yr
- **Debt instrument** (CFI DEMMRM), not a fund share. This is the structural pivot.
- Issuer: Backed Assets (JE) Limited (Jersey), parent Backed Finance AG (Switzerland)
- Tracker certificate referencing iShares IB01 UCITS ETF (Irish-domiciled)
- Liechtenstein FMA-approved Base Prospectus (FMA-ID 351548), EU passport to 30 states
- Custodians Maerki Baumann + InCore Bank, Security Agent Services AG (Zug)
- ISIN CH1173294260, issuance currency CHF, max issue volume CHF 100M

**Visual**: AUM time-series 2024-2026 for the three products (to be produced in S7).

### Section 4 — The eligibility verdict, block by block (1000 words)

**Key insight**: All three products fail Block A categorically. They are not direct sovereign claims, not UCITS, not rated corporate debt. bIB01 additionally fails due to its debt-instrument legal form under CRR Article 122.

**Content**:

**4.1 Block A — Eligibility category (300 words)**
- A.1 Direct sovereign claim: Fail for all (token = interest in wrapper, not Treasury directly)
- A.2 UCITS look-through (Art. 15 DR 2015/61): Fail for all. bIB01's underlying *is* a UCITS but holding bIB01 is not holding a UCITS unit — it's holding contractual debt referenced to UCITS price. Important legal distinction.
- A.3 Corporate debt rated CQS1: Fail for bIB01 (Backed Assets JE unrated → 100% RW under CRR Art. 122). N/A for BUIDL/OUSG (equity-like)
- Cascade closed: no product passes Block A.

**4.2 Block B — Operational requirements (250 words)**
- B.1 Unencumbered: Fail for all due to whitelists, freeze functions, pause functions
- B.2-B.4 mostly Conditional
- bIB01 has additional B.3 conditional due to T+5 settlement maximum

**4.3 Block C — Market criteria (250 words)**
- Empirical disaster across the board:
  - BUIDL: $0 24h volume, 54 holders Ethereum
  - OUSG: minimal AMM volume, ~80 holders
  - bIB01: ~$5K daily volume estimate, ~35 holders
- C.1 Listed exchange: bIB01 listed at INX ATS but **explicitly without market making**. Verbatim from Final Terms.
- C.3 Committed market makers: bIB01 Final Terms § 1.1 literally states "Market Maker: Not applicable"

**4.4 Block D — Wrapper-specific frictions (200 words)**
- BUIDL/OUSG: 3 fails (settlement finality, contract upgradeability, pause function) — these are inherent to current DLT infrastructure
- bIB01: **8 fails** including five contractual particularities:
  - Article XVII Extraordinary Event: Redemption can fall to $0.01
  - Article VI.iii unilateral Issuer Call with 30 BD notice "without specific reason"
  - Article XXIV Substitution without investor consent
  - Article XXII three creditor layers ahead of investors in realization
  - Section 6 explicit "Product not expected to be ECB eligible"

**Visual**: scoring heatmap (full version, 18+ criteria × 3 products).

### Section 5 — The empirical layer, on-chain reality (600 words)

**Key insight**: The market microstructure of tokenised treasuries is structurally more concentrated than the traditional HQLA reference. Tokenisation has not increased participation breadth — it has decreased it.

**Content**:

**5.1 Three concentration metrics**
- BUIDL Ethereum mainnet: 54 holders, Gini estimated 0.77, Top-3 = 63%
- Compare to traditional 1-year Treasury: 100,000+ holders worldwide, Gini ~0.50
- Compare to iShares IB01 UCITS ETF: Gini ~0.40 (institutional ETF wrapper)

**5.2 Volume reality**
- $0 24h secondary volume for BUIDL on CoinGecko (snapshot 6 May 2026)
- 1.72 average daily transactions on Ethereum since launch
- Total cumulative transactions over 26 months: 1,359

**5.3 What this means**
- The "tokenisation enables 24/7 liquid markets" narrative is empirically falsified for treasuries specifically
- These are wholesale institutional B2B products, not retail markets
- The Block C scoring fails are not theoretical — they reflect the actual market microstructure
- This is not necessarily a problem *for the products' purposes* (institutional cash management), but it disqualifies HQLA framing

**Visual**: Lorenz curve BUIDL + 4-panel market comparison chart.

### Section 6 — What it would take: the gradient (600 words) [S5 CONTENT]

**Key insight**: The path to HQLA is not incremental wrapper improvement. It requires structural redesign — and BlackRock has the institutional capacity to execute it.

**Content** (focus on BUIDL specifically as the most credible candidate):

**6.1 L0 → L1: UCITS MMF restructuration**
- Required: launch a Luxembourg or Ireland UCITS Money Market Fund version of BUIDL
- Regulatory framework: Regulation (EU) 2017/1131 (MMF Regulation), category "Short-Term VNAV MMF"
- Authorisation: CSSF (Lux) or Central Bank of Ireland
- Custodian: CRR Article 401 compliant (not BNY Mellon BVI arm — needs EU bank custodian)
- Listing: SIX Digital Exchange, Euronext Lux, or Deutsche Börse
- Precedent: Franklin Templeton FOBXX is under US 1940 Act ; the EU UCITS MMF equivalent doesn't exist yet
- Timeline: 12-18 months optimistic
- Result: Level 2A potential via Art. 15 look-through

**6.2 L1 → L2: DLT Pilot Regime compliance**
- Required: token issuance via authorised DLT-SS or DLT-TSS under Reg (EU) 2022/858
- As of Q1 2026: 3 entities authorised (21X AG, 360X AG, one DLT-SS)
- Restructuration: BlackRock Securitize tokenisation moves under a DLT-PR authorised infrastructure
- Settlement finality: resolved via Pilot Regime Article 7 exemption from CSDR
- Timeline: 18-24 months
- Result: ECB collateral eligibility discussion opens

**6.3 L2 → L3: Native sovereign DLT issuance**
- Required: US Treasury or Eurozone sovereign issues debt natively on a DLT-SS
- Precedents in trial: ECB Eurosystem wholesale CBDC trials 2024-2026, Banque de France TARGET on DLT
- Not a wrapper change — a fundamental change in the issuance infrastructure
- Timeline: 3-5 years
- Result: direct Level 1 status, full ECB collateral eligibility

**6.4 What about bIB01 and OUSG?**
- bIB01: requires reformulation from debt instrument to fund unit. Effectively a new product.
- OUSG: harder pivot due to fund-of-funds structure. Would need to flatten holdings first.

**Visual**: gradient roadmap diagram (4-step staircase, to be produced in S7).

### Section 7 — Implications for bank treasurers today (400 words) [S6 CONTENT]

**Key insight**: Tokenised treasuries are not HQLA today, but they are not excluded from a bank's balance sheet either. Treasurers need a classification framework now.

**Content**:

**7.1 Current classification**
- Tokenised RWA exposures should be classified as "Other Liquid Assets" — outside LCR numerator
- For Internal Liquidity Adequacy Assessment Process (ILAAP), they belong to a distinct category from cash + sovereign debt
- Reporting: typically not in COREP C72 / LCR template ; classification in internal liquidity reports

**7.2 Suggested internal haircut framework**
- Beyond standard HQLA haircut (which doesn't apply), apply internal management haircut to reflect wrapper risk:
  - Custody risk haircut: 5-10% (depending on custodian chain)
  - Settlement finality haircut: 10-15% (no SFD coverage)
  - Contract upgradeability haircut: 5% (admin keys risk)
  - Cumulative: 20-30% haircut over book value
- These are bank-internal numbers, not regulatory standards. For comparison, Level 2B HQLA gets 25-50% regulatory haircut.

**7.3 Internal limits to consider**
- Single-issuer cap: BUIDL = 100% BlackRock issuer concentration
- Single-chain cap: 95% on Ethereum for BUIDL = chain failure single point
- Single-custodian cap: depends on chosen custody (Anchorage / Fireblocks / Coinbase)
- Contract risk cap: limit aggregate exposure to upgradeable contracts

**7.4 What to monitor for regulatory evolution**
- EBA opinion on tokenised HQLA (anticipated but not yet published)
- ECB stance on collateral eligibility via DLT-PR
- ESMA review of UCITS Eligible Assets Directive
- BCBS work programme on cryptoasset prudential treatment (BCBS 538 + ongoing)

**Visual**: none (textual).

### Section 8 — Caveats and outlook (200 words)

**Key insight**: This framework is v1.0. It's intended as an opening contribution to a debate, not a closed verdict.

**Content**:
- Methodology limitations: based on public documentation (PPMs for BUIDL/Ondo not public)
- bIB01 Securities Note expires 7 May 2026 — Successor Base Prospectus status pending
- Empirical snapshot is 2026-05-11 ; products evolve fast
- The framework can be re-applied to new products (Superstate, Hashnote, OpenEden) using the same methodology
- Open invitation: GitHub repo for community contributions, Dune dashboard for live monitoring
- Closing thought: HQLA-grade tokenised treasury is coming — but not from the current wrapper generation

### Call-to-action and resources (50 words)

- Link to GitHub repo (full matrix + Dune queries + Python analysis)
- Link to Dune dashboard for live metrics
- LinkedIn / X handles for discussion
- Author bio: signaling per editorial decision (subtle vs explicit per validation)

## S5 — required content production checklist

To produce Section 6 (gradient L0→L3 for BUIDL specifically), the following sub-deliverables are needed in S5:

| Sub-deliverable | Estimated effort | Required for article? |
|---|---|---|
| L0 → L1 UCITS MMF restructuration walkthrough (legal + operational steps) | 3h | Yes — core of Section 6 |
| Franklin BENJI comparison (1940 Act framework vs UCITS) | 2h | Yes — credibility anchor |
| L1 → L2 DLT-PR compliance walkthrough | 2h | Yes — but lighter |
| L2 → L3 native sovereign issuance (with ECB Eurosystem precedents) | 2h | Yes — closing the gradient |
| Gradient roadmap diagram (staircase visualisation) | 1h | Yes — visual centerpiece |
| **Total S5** | **10h** | |

## S6 — required content production checklist

For Section 7 (practical implications), the following are needed:

| Sub-deliverable | Estimated effort | Required for article? |
|---|---|---|
| Current LCR/COREP classification mapping | 2h | Yes |
| Internal haircut framework proposal | 2h | Yes — differentiator |
| Internal limits recommendation matrix | 1h | Yes |
| Regulatory monitoring checklist | 1h | Optional but valuable |
| ICAAP risk category mapping | 1h | Optional |
| **Total S6** | **7h** | |

## S7 — final assembly checklist

| Sub-deliverable | Estimated effort |
|---|---|
| Article drafting (sections 0-8) | 6h |
| Visual production (AUM time-series + gradient diagram) | 1h |
| GitHub repo finalisation (README, matrix MD/JSON, queries, Python notebook) | 1h |
| Dune dashboard published | 1h |
| LinkedIn post draft | 0.5h |
| X thread draft | 0.5h |
| **Total S7** | **10h** |

## Total remaining effort

| Phase | Hours |
|---|---|
| S5 (gradient deep-dive) | 10 |
| S6 (bank implications) | 7 |
| S7 (article + assets + distribution) | 10 |
| **Total to publication** | **27h** |

## Key narrative arcs to maintain

1. **From narrative to reality** — opening contradiction sets tone
2. **Cascade of disqualifiers** — Block A → B → C → D builds the verdict layer by layer
3. **bIB01 as outlier** — five contractual particularities give a sharp differentiation point
4. **Gradient as roadmap** — turns negative verdict into actionable analysis
5. **Bank treasurer's day-1 framework** — practical anchor for the work-relevant reader
6. **Outlook = sovereign DLT** — closes on what tokenisation actually needs to be, not what it claims to be

## Risk register for the article

| Risk | Mitigation |
|---|---|
| Reads as "anti-tokenisation" / negative-only | Section 6 (gradient) explicitly positive on what's needed ; Section 7 actionable for treasurers |
| BlackRock / Ondo / Backed take exception to verdict | Cite primary sources verbatim ; framework is methodological, verdict is mechanically derived |
| Over-technical for LinkedIn audience | Hook (Section 0) is non-technical ; thread X version simplifies further |
| Out-of-date by publication time (products evolve) | Date framework v1.0 explicitly ; commit to v1.1 if material changes pre-publication |
| NDA CASA challenge despite formal clearance | Avoid CASA-specific operational details ; ground analysis only in public BCBS/CRR/DR texts |
| Methodological challenge by academic reviewer | Open-source the matrix, invite peer feedback in Section 8 |
