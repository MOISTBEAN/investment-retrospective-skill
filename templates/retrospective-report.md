# {{ticker}} Investment Retrospective

> Replace every placeholder. Retain `[RESEARCH NEEDED]`, `[VERIFY]`, `[CALCULATE]`, `[ADD]`, or `[DATA NOT PROVIDED]` where evidence is unavailable; never guess.

## 0. Scope

- Company:
- Ticker:
- Time range:
- Sector/theme:
- Main question:
- Materials reviewed:
- Price benchmark and peers:
- Information cutoff date:

### Fact / Reaction / Causal Attribution confidence

- Fact confidence: high / medium / low — {{whether the event, number, quote, or source claim is reliable}}
- Reaction confidence: high / medium / low / pending — {{whether price action is stock-specific versus market, sector, and peers with follow-through}}
- Causal Attribution confidence: high / medium / low / pending — {{whether source evidence explains why the market moved; price alone is not enough}}

## 0.1 First-read Finding Card

> Generate this card only after scoring and classification are complete. Place it here for reading order; do not use it to create or upgrade findings.

- **Sharp finding:** {{one-sentence finding already supported by the scored report}}
- **Strongest evidence:** {{2–4 strongest evidence layers or windows}}
- **Most misleading false signal or strongest limiting evidence:** {{the evidence most likely to be overread, or the strongest constraint on the finding}}
- **Current classification:** {{supported finding type and, if applicable, narrative-shift level}}
- **Still unproven:** {{material missing evidence, alternatives, or Pending tests}}
- **Fact confidence:** high / medium / low
- **Reaction confidence:** high / medium / low / pending
- **Causal Attribution confidence:** high / medium / low / pending

The card must preserve overlapping-window limitations, alternative explanations, and `Pending` status. It does not replace the executive summary, attribution matrix, or source register.

## 1. Executive Summary

Summarize in 5–8 bullets:

- Original market fear
- Key turning events
- Event-window verdict
- Price reaction and relative return evidence
- Main attribution hypothesis and strongest alternative explanation
- True signal versus noise conclusion
- Main lesson
- Future watchlist implication

Use this confidence format for each material conclusion:

- Fact confidence:
- Reaction confidence:
- Causal Attribution confidence:

## 2. Original Market Fear

### What the market appeared to fear

Describe the dominant bear case or uncertainty. Label this as fact, sourced market interpretation, or inference.

### Why this fear mattered

Explain which assumption it affected:

- Revenue growth
- Margins
- Customer concentration
- Competitive position
- Balance sheet
- Valuation multiple
- Business model viability

### Evidence of fear

List dated supporting evidence:

- Price decline or peer-relative underperformance
- Analyst concerns
- Earnings call questions
- News headlines
- Management responses
- Sector context

### Counter-evidence available at the time

- Evidence that limited or contradicted the fear
- Information not yet knowable

### Fact / Reaction / Causal Attribution confidence

- Fact confidence:
- Reaction confidence:
- Causal Attribution confidence:

## 3. Event Timeline

| Date | Event | Event Type | Claim Type | Source | Source Quality | Initial Interpretation at the Time | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---|---|---|---|---|---|---|
| {{date}} | {{what happened}} | {{type}} | {{fact/claim/reaction/inference}} | {{citation}} | {{tier/grade}} | {{contemporaneous interpretation}} | {{H/M/L}} | {{H/M/L/Pending}} | {{H/M/L/Pending}} |

## 4. Event Window Map

Define event windows before interpreting price action. Use the first regular session after after-hours disclosure as Effective T0 unless the disclosure occurred during market hours.

| Window ID | Anchor event | Event date | Disclosure timing | Effective T0 | Pre-event fear / setup | Reaction window | Follow-through window | Calculation required | Attribution test |
|---|---|---|---|---|---|---|---|---|---|
| W1 | {{event}} | {{date}} | {{before market / during market / after-hours / [VERIFY TIME]}} | {{date or [VERIFY TIME]}} | {{fear or setup}} | T+1 | T+5 / T+20 | {{stock vs market, sector, peers, volume, estimates}} | {{what would support or weaken attribution}} |

## 5. Claim Ledger

Split fact claims from interpretation claims. Do not mix reported facts, price reactions, and causal explanations in the same claim.

| Claim ID | Window | Claim class | Claim | Source | Claim type | Fear / assumption mapped | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---|---|---|---|---|---|---|
| C1F | W1 | Fact | {{reported event or number}} | {{S#}} | {{reported_number / management_claim / filing / transcript}} | {{assumption}} | {{H/M/L}} | N/A | N/A |
| C1I | W1 | Interpretation | {{interpretation or hypothesis}} | {{S#}} | {{analyst_interpretation / inference / reaction}} | {{assumption}} | {{H/M/L}} | {{H/M/L/Pending}} | {{Pending unless causal evidence is verified}} |

## 6. Price Reaction & Relative Return Map

State return convention, event-window treatment, benchmark, peer set, data source, and whether values are adjusted.

**Important:** Price movement is reaction evidence, not proof of causality. A large move only becomes useful attribution evidence after comparison against market, sector, peers, and follow-through.

| Window / Event Date | Effective T0 | Event | Horizon | Stock Return | Market Benchmark | Sector Benchmark | Peer Basket | Abnormal vs Market | Abnormal vs Sector | Abnormal vs Peer Basket | Interpretation | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|
| W1 / {{date}} | {{date}} | {{event}} | 1D / 5D / 20D | {{return or [CALCULATE]}} | {{return or [CALCULATE]}} | {{return or [CALCULATE]}} | {{return or [CALCULATE]}} | {{excess return or [CALCULATE]}} | {{excess return or [CALCULATE]}} | {{excess return or [CALCULATE]}} | {{reaction only; no causal proof}} | {{H/M/L}} | {{H/M/L/Pending}} | Pending |

## 6.1 Benchmark Layers

Benchmark Layers define what the price move is compared against.

| Layer | Instruments / metrics | Purpose | Required windows | Status |
|---|---|---|---|---|
| Broad market | QQQ, Nasdaq-100, SPY, relevant local index | Control for market-wide risk-on / risk-off | W1-Wn | [ADD] |
| Sector | Sector ETFs or industry indexes | Control for sector beta | W1-Wn | [ADD] |
| Core peers | Declared peer basket | Test stock-specific reaction against close comparables | W1-Wn | [ADD] |
| Adjacent peers | Theme-specific or supply-chain peers | Test whether the theme moved as a group | Relevant windows | [ADD] |
| Flow / positioning | Volume, short interest, options implied move, put/call, ETF flows | Test whether price action was flow-driven | Key windows | Pending |
| Consensus model | FY+1/FY+2 revenue, EPS, EBITDA, target price, rating | Test whether forward assumptions changed | Key windows | Pending |

## 6.2 Expanded Data Layer

The current price map may support stock-specific reactions, but this is not full peer-relative validation. A stronger version should expand the data panel before upgrading causal attribution.

| Data layer | Instruments / metrics | Purpose | Required windows | Status |
|---|---|---|---|---|
| Broad market | QQQ, Nasdaq-100, SPY | Control for market-wide risk-on / risk-off | W1-Wn | [ADD] |
| Sector | Sector ETFs and industry indexes | Control for sector beta | W1-Wn | [ADD] |
| Core peers | {{peer 1}}, {{peer 2}}, {{peer 3}} | Test stock-specific reaction against closer peers | W1-Wn | [ADD] |
| Adjacent peers | {{theme peer 1}}, {{theme peer 2}} | Test whether related narrative moved as a group | Relevant windows | [ADD] |
| Trading / positioning | Volume vs 20D average, short interest, options implied move, put/call, ETF flows | Test whether price action was flow-driven | Key windows | Pending |
| Consensus model | FY+1/FY+2 revenue, EPS, EBITDA, target price, rating | Test whether forward assumptions changed | Key windows | Pending |

Expanded price data can raise Reaction confidence, but it cannot by itself raise Causal Attribution confidence to High.

## 6.3 Valuation Re-rating Layer

Valuation re-rating should not be inferred from price action alone. The test is whether the company’s forward multiple changed versus its own history and versus peer median around the same event windows. A narrative or market-model shift becomes stronger only if valuation spread, consensus revision, analyst language, and operating follow-through point in the same direction.

| Window | Date point | Company EV/NTM Revenue | Company forward P/E | Peer median EV/NTM Revenue | Peer median forward P/E | Company premium / discount | Interpretation |
|---|---|---:|---:|---:|---:|---:|---|
| W1 | T-20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Pre-event valuation setup |
| W1 | T+20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Test derating / rerating |
| W2 | T-20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Pre-event valuation setup |
| W2 | T+20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Test derating / rerating |

| Window | Stock move | FY+2 revenue estimate change | FY+2 EPS estimate change | EV/Sales change | Forward P/E change | Main driver | Valuation attribution |
|---|---:|---:|---:|---:|---:|---|---|
| W1 | {{20D return or [CALCULATE]}} | [ADD] | [ADD] | [ADD] | [ADD] | [Estimate revision / multiple change / both] | Pending |
| W2 | {{20D return or [CALCULATE]}} | [ADD] | [ADD] | [ADD] | [ADD] | [Estimate revision / multiple change / both] | Pending |

A stock move should not be labeled valuation rerating unless forward multiples expand versus the company’s own pre-event baseline and versus the selected peer median. If price rises only because revenue or EPS estimates rise, classify it as estimate-driven rather than multiple-driven. Until these fields are populated with reliable historical forward valuation and consensus data, valuation attribution must remain Pending.

## 6.4 Candidate Driver Attribution Matrix

| Window | Price anomaly | Candidate driver | Driver type | Finding type | Direction | Evidence | Benchmark support | Expanded data support | Valuation support | Attribution score | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | {{return evidence or [CALCULATE]}} | {{candidate explanation}} | {{fundamental / expectations / sector / macro / flow / policy / valuation / analyst / technical}} | {{finding type}} | {{positive/negative/mixed}} | {{S# / C#}} | {{market, sector, peer comparison}} | {{expanded data status}} | {{valuation status}} | {{0-4 / Pending}} | {{H/M/L}} | {{H/M/L/Pending}} | {{Pending unless causal evidence is verified}} |

## 6.5 Attribution Scoring Rubric

| Score | Requirement |
|---:|---|
| 0 | Required event, return, or benchmark evidence is unavailable. |
| 1 | Timing coincidence or one evidence layer supports the candidate driver. |
| 2 | Credible event evidence and directional price reaction align, but benchmark or follow-through support is weak. |
| 3 | Credible event evidence, benchmark comparison, and multi-window follow-through support a stock-specific reaction. |
| 4 | Multiple independent causal layers align, including operating, analyst, valuation, customer, backlog, policy, macro, flow, or positioning evidence as applicable. |

An attribution score measures the evidence stack, not certainty about cause. Price action alone may support Reaction confidence, but it cannot establish Causal Attribution confidence.

**Story synthesis gate:** Complete the candidate-driver matrix and attribution scoring before drafting the narrative. Do not use the story to justify scores after the fact; preserve `Pending` where evidence is missing.

## 7. Narrative Shift Map

### Old narrative

Describe the prior market view and the dated evidence that it existed.

### Transition period

Describe when evidence started to challenge the old view. Distinguish early signals from later confirmation.

### Candidate new narrative

Describe the candidate new market framing and whether it became consensus or remained contested. Do not call it confirmed unless multiple independent evidence layers support it.

### Evidence supporting the shift

- Evidence 1
- Evidence 2
- Evidence 3

### Evidence against or limiting the shift

- Counter-evidence 1
- Counter-evidence 2

### Shift date or period

- Earliest knowable signal:
- Confirmation period:

### Fact / Reaction / Causal Attribution confidence

- Fact confidence:
- Reaction confidence:
- Causal Attribution confidence:

## 8. Attribution Hypotheses

Repeat this block for each major price move. Use hypotheses, not definitive causal claims.

### Move: {{price_move_or_period}}

#### Primary attribution hypothesis

Describe the most likely explanation and label it as a hypothesis.

#### Affected assumption

Select and explain:

- Growth
- Margin
- Customer adoption
- Technology validation
- Financing risk
- Valuation multiple
- Competitive position

#### Supporting evidence

- Evidence 1
- Evidence 2
- Evidence 3

#### Counter-evidence

- Evidence that weakens the primary hypothesis

#### Alternative explanations

- Sector-wide rally or selloff
- Macro risk-on or risk-off move
- Short covering or positioning
- Valuation multiple expansion or compression
- Peer sympathy move
- Index effect
- Other company-specific news

#### Discriminating test

State the observation that would make the primary hypothesis more likely than its strongest alternative, and the observation that would falsify it.

#### Fact / Reaction / Causal Attribution confidence

- Fact confidence:
- Reaction confidence:
- Causal Attribution confidence:

## 9. True Signal vs Noise

### True signals

| Signal | Why It Mattered | Evidence | What Was Knowable Then | Alternative Explanation | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---|---|---|---|---|

### Possible signals or too uncertain

| Signal | Missing Confirmation | Evidence Needed | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---|---|---|

### Noise or weaker signals

| Signal | Why It Was Less Useful | Risk of Overinterpretation |
|---|---|---|

## 10. Lessons Learned

List 3–7 lessons. For each lesson include:

- **Lesson:**
- **Why it mattered in this case:**
- **How it could apply in future cases:**
- **False-positive risk:**
- **Fact confidence:**
- **Reaction confidence:**
- **Causal Attribution confidence:**

## 11. Future Watchlist Rules

### Pattern name

Example: AI infrastructure narrative reversal

### Conditions to monitor

- Condition 1
- Condition 2
- Condition 3

### Evidence required

- Primary-source evidence
- Independent validation
- Price-reaction confirmation
- Peer-relative confirmation
- Valuation / estimate confirmation where relevant

### Disconfirming evidence

- Evidence that would weaken or invalidate the pattern

### False-positive risks

- Management commentary without external validation
- Short-term price bounce without thesis change
- Sector-wide rally mistaken for a stock-specific shift
- Already priced-in catalyst

### Applicable company types or themes

- {{company type/theme}}

## 12. Open Questions

List unresolved questions, missing sources, and data gaps that require further research.

Group by:

- Price / relative return
- Benchmark / peer set
- Expanded data layer
- Valuation / multiple data
- Consensus / estimate revisions
- Transcript / management language
- Customer / ecosystem validation
- Backlog / design-win visibility
- Margin / EPS follow-through
- Macro / flow / policy / technical alternatives

## 13. Final Retrospective Takeaway

Write one concise paragraph explaining what this case teaches about market narrative change or attribution discipline. Do not include a recommendation or forecast.

## 14. Source Register

Record every source used for a material claim. Group repeated reporting that traces to the same origin. Do not add sources for volume; every source must support a defined claim or attribution test.

| ID | Date Published | Issuer/Publisher | Title or Document | URL/Identifier | Tier | Proximity | Grade | Claim / Window IDs Supported | Access Notes |
|---|---|---|---|---|---|---|---|---|---|
| S1 | {{date}} | {{issuer}} | {{title}} | {{URL or filing ID}} | {{1–5}} | {{direct/near-direct/indirect/speculative}} | {{A–D}} | {{C# / W#}} | {{paywall/correction/context}} |

## 14.1 Required Source Backlog

These are required source categories, not active sources. Add them only when they are used to test a defined attribution claim.

| Backlog ID | Date | Source category | URL | Tier | Claim / Window IDs | Event / claim covered | Use in retrospective | Limitation |
|---|---|---|---|---|---|---|---|---|
| B1 | [VERIFY] | Earnings call transcripts | [VERIFY URL] | Tier 1 | Transcript claims / W# | Management language on guidance, demand, customer breadth, margin conversion, or risk | Verify exact wording and separate management facts from interpretation | Transcript language may be promotional and requires market-reaction testing |
| B2 | [VERIFY] | Sell-side estimate revisions and target-price changes | [VERIFY URL] | Tier 3 | Estimate revision claims / W# | Revenue / EPS / target-price changes after event windows | Test whether expectations actually changed | Sell-side changes may lag price and can be reactive |
| B3 | [VERIFY] | Customer, partner, or ecosystem validation sources | [VERIFY URL] | Tier 1 / Tier 2 | Customer validation claims / W# | Customer, partner, or ecosystem confirmation | Verify customer breadth and concentration-risk claims | Do not use rumors or social media as factual validation |
| B4 | [VERIFY] | Event-window valuation snapshot source | [VERIFY URL] | Tier 4 | Valuation snapshot claims / W# | EV/Sales, forward P/E, revenue multiple, peer premium / discount | Provide event-window valuation snapshots for initial valuation context | Snapshot data alone does not prove rerating |
| B5 | [VERIFY] | Historical forward valuation dataset | [VERIFY URL] | Tier 4 | Valuation rerating claims / W# | EV/NTM Revenue, forward P/E, EV/EBITDA, peer median, premium / discount | Test whether the company experienced multiple expansion or compression around event windows | Requires reliable historical consensus and enterprise value data |
| B6 | [VERIFY] | Consensus estimate revision dataset | [VERIFY URL] | Tier 4 | Estimate revision claims / W# | FY+1/FY+2 revenue, EPS, EBITDA, target price, rating changes | Decompose stock move into estimate revision versus multiple expansion | Public data may be incomplete or stale |
| B7 | [VERIFY] | Expanded peer price dataset | [VERIFY URL] | Tier 4 | Expanded benchmark claims / W# | Broad market, sector, core peers, adjacent peers | Test whether reaction remains stock-specific under broader peer comparison | Peer selection can bias attribution if not declared before analysis |
| B8 | [VERIFY] | Macro / rates dataset | [VERIFY URL] | Tier 4 | Macro claims / W# | QQQ/SPY, rates, credit spreads, dollar, liquidity indicators | Test whether move reflects macro risk-on / risk-off rather than company-specific attribution | Macro variables rarely prove single-name causality |
| B9 | [VERIFY] | Flow / positioning dataset | [VERIFY URL] | Tier 4 | Flow claims / W# | Volume, options, short interest, ETF flows, 13F, institutional positioning | Test whether move reflects short covering, crowding, ETF flow, or positioning | Flow data can be lagged or incomplete |
| B10 | [VERIFY] | Policy / regulatory source set | [VERIFY URL] | Tier 1 / Tier 2 | Policy claims / W# | Export controls, tariffs, subsidies, antitrust, regulation, industrial policy | Test whether policy changed the risk/reward setup | Requires company exposure mapping |
| B11 | [VERIFY] | Technical / mean-reversion dataset | [VERIFY URL] | Tier 4 | Technical claims / W# | Prior drawdown, support/resistance, moving averages, RSI, volume, gap behavior | Test whether move was technical reversal rather than fundamental or narrative shift | Technical evidence should not override source-based attribution |
