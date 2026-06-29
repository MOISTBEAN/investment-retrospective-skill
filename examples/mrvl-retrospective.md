# MRVL Investment Retrospective — Working Example v0.9.1

## 0. Status and Verification Notes

Compact v0.9.1 working example for `investment-retrospective-skill`, adding expanded data and valuation audit layers without upgrading causal attribution. It is not an investment report, financial advice, or a buy/sell recommendation. The purpose is event-window attribution discipline: separate fact claims, interpretation claims, reaction evidence, and causality.

Items requiring verification: remaining T+1/T+5/T+20 price reactions outside W1, W4, and W5; earnings-call language; sell-side notes; customer-specific claims; and claim status as official, reported, analyst interpretation, inference, or speculation.

Confidence rules use three separate labels: **Fact confidence** measures whether an event or number is accurate; **Reaction confidence** measures whether price action is stock-specific versus SMH/SOXX and peers with T+1/T+5/T+20 follow-through; **Causal attribution confidence** measures whether source evidence explains why the market moved. Causal attribution stays **Pending** until transcript evidence, sell-side revisions, customer validation, or valuation / multiple data map to the same event window. Preserve `[CALCULATE]` when price data is unavailable.

## 0.1 Executive Attribution Takeaway

MRVL is not a single-cause retrospective. The current evidence supports several attribution findings, but causal attribution is not confirmed. The strongest supported evidence is price-reaction evidence for W1 and W5, with W4 showing a strong immediate but weak sustained reaction.

| Window | Price move | Best-supported finding | What likely changed | Reaction confidence | Causal attribution confidence |
|---|---:|---|---|---|---|
| W1 / Mar 2025 | -19.81% 1D; -29.85% 20D | Negative expectation reset | Strong AI growth did not clear elevated market expectations; guidance was not enough to sustain the prior AI premium. | High | Pending |
| W4 / Aug 2025 | -18.60% 1D; -18.00% 5D; +7.69% 20D | Custom ASIC visibility retest / possible mean reversion | Below-consensus guide and ASIC lumpiness triggered an immediate selloff, but the 20D reversal weakens durable negative attribution. | High immediate / Low-Medium sustained | Pending |
| W5 / Mar 2026 | +18.35% 1D; +41.53% 20D | Positive long-term target validation candidate | FY2027/FY2028 targets supported a broader AI infrastructure framing and created the strongest positive stock-specific window. | High | Pending |
| W6 / May 2026 | [CALCULATE] | TAM / customer breadth reinforcement | FY2029 custom chip target and hyperscaler breadth claims may reinforce the candidate narrative, but price reaction and customer-side validation remain missing. | Pending | Pending |

Current conclusion: MRVL is best classified as a candidate narrative shift, not a confirmed narrative shift. W1 and W5 show strong stock-specific price anomalies. W4 shows a sharp immediate reaction but weak sustained attribution. Full confirmation requires sell-side model changes, valuation spread expansion, customer or ecosystem validation, backlog / design-win evidence, and margin / EPS follow-through to align with the same event windows.

The v0.9.1 data and valuation patch does not change the current conclusion. It clarifies what additional evidence is required before W5 or W6 can be upgraded from candidate narrative shift to market-model shift.

## 0.2 Multi-Dimensional Key Findings

Key findings should not be limited to narrative shift. A retrospective may conclude that the move was driven by fundamentals, guidance, sector rotation, macro/rate changes, flow/positioning, policy, valuation, analyst model revision, technical mean reversion, or narrative change.

### 0.2.1 Finding Type Summary

| Finding type | What it tests | MRVL status | Evidence status |
|---|---|---|---|
| Price anomaly | Did the stock move unusually versus market, sector, and peers? | Supported for W1 and W5; W4 immediate but weak sustained | W1/W4/W5 calculated |
| Narrative shift | Did the market start classifying MRVL differently? | Candidate / externally testable | Needs analyst language, valuation spread, customer/ecosystem validation |
| Fundamental improvement | Did revenue, guidance, backlog, margins, or EPS improve? | Partially supported through data-center growth and long-term targets | Needs follow-through |
| Fundamental deterioration | Did guidance, margins, or segment performance weaken? | Relevant in W1/W4 because expectations and custom visibility were challenged | Needs transcript and estimate revision checks |
| Sector rotation | Was the move driven by semiconductor / AI sector beta? | Controlled partly through SMH/SOXX comparison | Needs broader peer basket |
| Macro / rates | Was the move caused by risk-on/risk-off or interest-rate changes? | Not yet tested | Needs QQQ/SPY/rate context |
| Flow / positioning | Was the move driven by short covering, ETF flows, institutional positioning, or crowded AI trade unwind? | Not yet tested | Needs short interest, ETF flow, 13F, volume / options data |
| Policy / regulatory | Was there a policy, export-control, industrial-policy, or regulatory driver? | Not central in current MRVL example | Keep as a standard check |
| Valuation rerating | Did the market assign a different multiple versus peers? | Pending | Needs EV/Sales, forward P/E, peer-spread analysis |
| Analyst / consensus revision | Did sell-side models, ratings, target prices, or estimates change? | Pending | Needs estimate / rating / target-price data |
| Mean reversion | Was the move a rebound or reversal after overreaction? | Possible in W4 due to 20D reversal | Needs technical / prior drawdown context |

## 0.3 Event-Driven Strength Summary

| Window | Event | Event-driven strength | Why |
|---|---|---|---|
| W1 | March 2025 expectation reset | Strong negative stock-specific reaction | MRVL materially underperformed SMH/SOXX and the AVGO/NVDA peer basket over 1D, 5D, and 20D. |
| W4 | August 2025 custom ASIC visibility retest | Strong immediate reaction, weak sustained attribution | MRVL underperformed sharply over 1D and 5D, but 20D relative performance reversed, weakening durable attribution. |
| W5 | March 2026 long-term target shift | Strong positive stock-specific reaction | MRVL materially outperformed SMH/SOXX and the AVGO/NVDA peer basket through 1D, 5D, and 20D. |
| W2 / W3 / W6 | Other events | Pending | Price windows are not yet calculated. |

## 0.4 Narrative Shift Classification

Narrative shift is a classification outcome, not a default explanation. MRVL should not be upgraded unless the same event windows show stock-specific reaction, expectation change, valuation or model change, and external / operating validation.

| Level | Classification | Meaning | MRVL v0.9.1 status |
|---|---|---|---|
| Level 0 | No shift | Events occurred, but no meaningful stock-specific reaction or expectation change is visible. | Rejected for W1 and W5 because price reaction is stock-specific. |
| Level 1 | Reaction only | Stock moved abnormally, but forward assumptions are not shown to have changed. | Minimum supported level for W1 and W5. |
| Level 2 | Company-framed candidate shift | Management provides stronger guidance, targets, TAM, or product framing, but external validation is incomplete. | Supported for W5 / W6 as a candidate. |
| Level 3 | Externally validated candidate shift | Customer, partner, ecosystem, backlog, or design-win evidence supports the company framing. | Pending until external validation and backlog / design-win evidence are added. |
| Level 4 | Market-model shift | Estimates, target prices, analyst language, valuation spreads, or peer frameworks change with the same event window. | Pending. |
| Level 5 | Confirmed narrative shift | Price, estimates, valuation, external validation, backlog / guidance, and fundamental follow-through align. | Not supported in v0.9.1. |

Current classification: **candidate narrative shift, not confirmed**. W5 is the strongest positive price-reaction window, but MRVL should not be treated as a confirmed narrative shift until Level 4 / Level 5 evidence is verified.

Level 4 cannot be assigned from price action alone. It requires valuation spread, consensus revision, sell-side language, or peer-framework evidence tied to the same event window.


## 1. Case Framing

Marvell Technology (MRVL) is a data-infrastructure semiconductor company with exposure to custom ASICs, data-center switching, interconnect, optical modules, and storage controllers. During FY2025–FY2026, its data-center business became the central growth driver as hyperscalers increased AI infrastructure spending.

**Retrospective question:** When did the market begin to treat Marvell less as a cyclical networking/custom ASIC story and more as a broader AI infrastructure scaling beneficiary?

Working hypothesis to test: the story was not simply “market feared Amazon order loss, then fear resolved.” The cleaner hypothesis is that the market already knew MRVL had AI exposure; the issue was whether visible evidence justified elevated AI expectations.

## 2. Original Market Fear

### 2.1 Fear summary

By early 2025, investors already knew MRVL had AI exposure. The fear was whether visible revenue, customer breadth, and margin conversion justified elevated AI expectations. The fear set: AI expectations too high; custom silicon visibility uncertain; customer concentration risk; non-AI weakness; margin / EPS conversion risk.

### 2.2 Fear cluster table

| Fear cluster | Affected assumption | Evidence | Counter-evidence | Fact confidence | Reaction confidence | Causal attribution confidence |
|---|---|---|---|---|---|---|
| AI expectations too high | AI revenue acceleration / valuation multiple | March 2025 guide near consensus; Reuters said investors expected stronger AI growth and shares fell about 15% after hours. [S2] | Q4 FY2025 revenue up 27% YoY; data-center up 78% YoY. [S1] | High | High after W1 calculation | Pending |
| Custom silicon visibility uncertainty | ASIC growth durability | August 2025 below-consensus guide and analyst concern about ASIC lumpiness. [S5] | Management said lumpiness was normal. [S5] | High | High immediate / Low-Medium sustained after W4 calculation | Pending |
| Customer concentration risk | Customer breadth / follow-on wins | Amazon exposure and Microsoft delay concerns were reported. [S2], [S5] | Later Reuters report cited engagements across all U.S. hyperscalers. [S7] | Medium | Pending | Pending |
| Non-AI / legacy weakness | Total-company growth quality | Consumer and industrial weakness reported in May 2025. [S4] | Data center was roughly three-quarters of revenue. [S4] | Medium | Pending | Pending |
| Margin / EPS conversion | Revenue-to-earnings conversion | Custom silicon may carry lower gross margins; CFRA expected profit contribution over time. [S4] | Q1 FY2026 non-GAAP gross margin guide around 60%. [S1] | Medium | Pending | Pending |

### 2.3 Evidence of fear

The core fear was not one customer rumor. It was a repeated demand for more proof: March 2025 showed expectation risk; August 2025 showed ASIC lumpiness could reset confidence; May 2025 showed AI strength could be diluted by weak non-AI segments. [S2], [S4], [S5]

## 3. Key Timeline

| Date | Event | Type | Source / claim | Initial interpretation | Verification |
|---|---|---|---|---|---|
| Mar 5, 2025 | FY2025 Q4 revenue $1.817B, data-center up 78% YoY; Q1 FY2026 guide about $1.875B. | earnings / guide | S1, S2 / reported_number + reaction | Strong AI growth, but not enough versus expectations. | Price windows calculated in §6 |
| May 6, 2025 | Investor day postponed; custom silicon webinar announced; Q1 guide midpoint reaffirmed. | management / investor_event | S3 / management_claim | Management tried to keep focus on custom AI opportunity. | Reaction [CALCULATE] |
| May 29, 2025 | Q2 guide above estimates; data center about 76% of revenue; weak consumer/industrial. | earnings / guide | S4 / reported_number + analyst_interpretation | AI demand strong, total-company quality mixed. | Price windows [CALCULATE] |
| Aug 28, 2025 | Q3 guide below estimates; custom ASIC lumpiness cited; shares down >12% after hours. | earnings / guide | S5 / market_reaction | Reconfirmed custom silicon visibility fear. | Price windows calculated in §6 |
| Mar 5, 2026 | FY2028 revenue target near $15B; FY2027 revenue growth >30%; shares up about 15% after hours. | earnings / long-term guide | S6 / management_claim + reaction | Potential shift to broader AI infrastructure platform. | Relative return calculated in §6 |
| May 27, 2026 | FY2029 custom chip revenue target >$10B; FY2028 forecast raised to $16.5B. | long-term guide | S7 / management_claim | Narrative reinforcement. | Price windows [CALCULATE] |

## 4. Claim Ledger

| ID | Window | Claim class | Claim | Source | Claim type | Fear mapped | Fact confidence | Reaction confidence | Causal attribution confidence |
|---|---|---|---|---|---|---|---|---|---|
| C1F | W1 | Fact | FY2025 Q4 revenue was $1.817B; Q1 FY2026 guide was about $1.875B. | S1, S2 | reported_number | AI expectations | High | N/A | N/A |
| C1I | W1 | Interpretation | The March selloff likely reflected an expectations gap, not weak reported AI growth. | S2 | analyst_interpretation / reaction | AI expectations | Medium | High | Pending |
| C2F | W1 | Fact | Q4 FY2025 data-center revenue grew 78% YoY. | S1, S2 | reported_number | AI durability | High | N/A | N/A |
| C3F | W2 | Fact | Marvell postponed investor day, announced a custom silicon webinar, and reaffirmed the Q1 guide midpoint. | S3 | management_claim | Custom visibility | High | N/A | N/A |
| C3I | W2 | Interpretation | The webinar announcement was a management attempt to clarify the custom AI silicon opportunity. | S3 | inference | Custom visibility | Medium | Pending | Pending |
| C4F | W3 | Fact | Marvell guided Q2 revenue above estimates; data center was about 76% of revenue; consumer and industrial were weak. | S4 | reported_number | Non-AI / margin | High | N/A | N/A |
| C4I | W3 | Interpretation | Strong AI evidence was still mixed because non-AI weakness and margin questions remained. | S4 | analyst_interpretation | Non-AI / margin | Medium | Pending | Pending |
| C5F | W4 | Fact | Marvell guided Q3 revenue below estimates; Reuters reported shares down more than 12% after hours. | S5 | reported_number / reaction | Custom visibility | High | N/A | N/A |
| C5I | W4 | Interpretation | Custom ASIC lumpiness revived old visibility fears. | S5 | analyst_interpretation | Custom visibility | Medium | High immediate / Low-Medium sustained | Pending |
| C6F | W5 | Fact | Reuters reported FY2028 revenue target near $15B, FY2027 growth above 30%, and shares up about 15% after hours. | S6 | management_claim / reaction | Long-term opportunity | High | N/A | N/A |
| C6I | W5 | Interpretation | The target supported, but did not prove, a broader AI infrastructure platform framing. | S6 | inference | Long-term opportunity | Medium | High | Pending |
| C7F | W6 | Fact | Reuters reported FY2029 custom chip revenue target above $10B and FY2028 forecast raised to $16.5B. | S7 | management_claim | TAM / breadth | High | N/A | N/A |
| C7I | W6 | Interpretation | The targets reinforced the platform narrative, pending price and follow-through tests. | S7 | inference | TAM / breadth | Medium | Pending | Pending |
| C8F | W6 | Fact | Reuters reported management said Marvell had custom engagements across all U.S. hyperscalers. | S7 | management_claim | Customer breadth | Medium-High | N/A | N/A |
| C8I | W6 | Interpretation | The hyperscaler breadth claim addresses concentration risk but needs customer validation. | S7 | inference | Customer breadth | Medium | Pending | Pending |

## 5. Event Window Map

| Window ID | Anchor event | Event date | Disclosure Timing | Effective T0 | Pre-event fear / setup | Reaction window | Follow-through window | Calculation required | Attribution test |
|---|---|---|---|---|---|---|---|---|---|
| W1 | FY2025 Q4 earnings and Q1 FY2026 guide | Mar 5, 2025 | After-hours earnings / Reuters same day | Mar 6, 2025 (first regular session after disclosure) | AI expectations too high after 2024 AI run-up | T+1 | T+5 / T+20 | MRVL vs SMH, SOXX, AVGO, NVDA; volume; estimate revisions | If MRVL underperforms peers through T+5/T+20, selloff is more likely stock-specific. |
| W2 | Custom silicon webinar announcement | May 6, 2025 | Press release; exact time [VERIFY TIME] | Same session or next session depending on release time [VERIFY TIME] | Custom silicon visibility uncertain | T+1 | Through Jun 17 webinar | MRVL return into webinar; relative return; analyst preview notes | Determine whether announcement changed expectations or was ignored. |
| W3 | Q1 FY2026 earnings / Q2 guide | May 29, 2025 | Earnings / Reuters; exact market timing [VERIFY TIME] | Next regular session if after-hours; otherwise same session [VERIFY TIME] | Need proof AI demand persists | T+1 | T+5 / T+20 | MRVL vs peers; estimate changes; segment mix | Test whether above-consensus guide created durable confidence. |
| W4 | Q2 FY2026 earnings / Q3 guide | Aug 28, 2025 | After-hours earnings / Reuters same day | Aug 29, 2025 (first regular session after disclosure) | Concern about ASIC lumpiness | T+1 | T+5 / T+20 | MRVL vs SMH/SOXX/AVGO/NVDA; custom ASIC estimate changes | Classify as immediate reaction but weak sustained attribution unless estimate revisions or transcript evidence confirm durable concern. |
| W5 | FY2026 results / FY2028 target | Mar 5, 2026 | After-hours earnings / Reuters same day | Mar 6, 2026 (first regular session after disclosure) | Need broader platform evidence | T+1 | T+5 / T+20 | MRVL relative return; target-price revisions; FY2027/FY2028 estimate revisions | Primary positive narrative-shift test window. Upgrade reaction confidence only if relative T+5/T+20 outperformance remains material; keep causal attribution pending until source evidence confirms why expectations changed. |
| W6 | FY2029 custom chip target | May 27, 2026 | Reuters report / management target; exact market timing [VERIFY TIME] | Same session or next session depending on disclosure time [VERIFY TIME] | Need customer breadth and TAM proof | T+1 | T+5 / T+20 | MRVL relative return; peer comparison; hyperscaler comments | Keep attribution Pending until the market reaction is stock-specific. |

## 6. Price Reaction & Relative Return Map

Price action is reaction evidence, not causality proof. A large move only becomes useful attribution evidence after comparing the event window against peers, indexes, and follow-through.

Return convention: unadjusted regular-session close-to-close price return. 1D runs from the T−1 close to the effective-T0 close; 5D and 20D use the same base close through the fifth and twentieth trading-session closes, inclusive of T0. Abnormal return equals MRVL return minus the comparator return. The peer basket is the equal-weight arithmetic mean of AVGO and NVDA. Source: Nasdaq Historical Quotes [S8].

| Window / event date | Effective T0 | Event | Horizon | MRVL | SMH | SOXX | AVGO | NVDA | Abnormal vs SMH | Abnormal vs SOXX | Peer basket | Abnormal vs peer basket | Interpretation | Reaction confidence | Causal attribution confidence |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| W1 / Mar 5, 2025 | Mar 6, 2025 | FY2025 Q4 / Q1 guide | 1D (Mar 6) | -19.81% | -4.19% | -4.16% | -6.33% | -5.74% | -15.62 pp | -15.66 pp | -6.03% | -13.78 pp | Initial reaction fits “expectations too high,” but causality not proven. | High | Pending |
| W1 / Mar 5, 2025 | Mar 6, 2025 | FY2025 Q4 / Q1 guide | 5D (Mar 12) | -22.51% | -3.87% | -5.11% | +1.38% | -1.33% | -18.64 pp | -17.40 pp | +0.03% | -22.54 pp | Initial reaction fits “expectations too high,” but causality not proven. | High | Pending |
| W1 / Mar 5, 2025 | Mar 6, 2025 | FY2025 Q4 / Q1 guide | 20D (Apr 2) | -29.85% | -6.67% | -8.30% | -10.17% | -5.87% | -23.18 pp | -21.55 pp | -8.02% | -21.83 pp | Initial reaction fits “expectations too high,” but causality not proven. | High | Pending |
| W2 / May 6, 2025 | [VERIFY TIME] | Webinar announcement / investor day delay | 1D / 5D / 20D | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | Could be neutral, cautious, or positive depending on price and analyst follow-up. | Pending | Pending |
| W3 / May 29, 2025 | [VERIFY TIME] | Q1 results / Q2 guide | 1D / 5D / 20D | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | Mixed evidence: good AI guide, lingering segment/margin concerns. | Pending | Pending |
| W4 / Aug 28, 2025 | Aug 29, 2025 | Q2 results / Q3 guide | 1D (Aug 29) | -18.60% | -2.87% | -2.86% | -3.65% | -3.32% | -15.73 pp | -15.74 pp | -3.49% | -15.11 pp | Immediate stock-specific selloff, but 20D reversal weakens sustained attribution. | High immediate / Low-Medium sustained | Pending |
| W4 / Aug 28, 2025 | Aug 29, 2025 | Q2 results / Q3 guide | 5D (Sep 5) | -18.00% | -1.87% | -2.18% | +8.50% | -7.30% | -16.12 pp | -15.82 pp | +0.60% | -18.60 pp | Immediate stock-specific selloff, but 20D reversal weakens sustained attribution. | High immediate / Low-Medium sustained | Pending |
| W4 / Aug 28, 2025 | Aug 29, 2025 | Q2 results / Q3 guide | 20D (Sep 26) | +7.69% | +7.68% | +6.45% | +8.38% | -1.10% | +0.02 pp | +1.25 pp | +3.64% | +4.05 pp | Immediate stock-specific selloff, but 20D reversal weakens sustained attribution. | High immediate / Low-Medium sustained | Pending |
| W5 / Mar 5, 2026 | Mar 6, 2026 | FY2026 results / FY2028 target | 1D (Mar 6) | +18.35% | -3.74% | -4.22% | -0.69% | -3.01% | +22.09 pp | +22.57 pp | -1.85% | +20.20 pp | Primary positive narrative-shift test window; relative follow-through supports a stock-specific reaction, but not causal attribution by itself. | High | Pending |
| W5 / Mar 5, 2026 | Mar 6, 2026 | FY2026 results / FY2028 target | 5D (Mar 12) | +15.84% | -1.83% | -2.24% | +0.96% | -0.11% | +17.67 pp | +18.08 pp | +0.43% | +15.42 pp | Primary positive narrative-shift test window; relative follow-through supports a stock-specific reaction, but not causal attribution by itself. | High | Pending |
| W5 / Mar 5, 2026 | Mar 6, 2026 | FY2026 results / FY2028 target | 20D (Apr 2) | +41.53% | -0.77% | +0.55% | -5.48% | -3.25% | +42.30 pp | +40.98 pp | -4.36% | +45.89 pp | Primary positive narrative-shift test window; relative follow-through supports a stock-specific reaction, but not causal attribution by itself. | High | Pending |
| W6 / May 27, 2026 | [VERIFY TIME] | FY2029 custom chip target | 1D / 5D / 20D | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | Long-term target supports narrative but price attribution unknown. | Pending | Pending |

## 6.1 Price-Anomaly-First Workflow

1. Detect price anomaly.
2. Define the abnormal window: 1D, 5D, 20D, 60D, or longer.
3. Benchmark the move against broad market, sector, peers, and valuation spread.
4. Search candidate drivers around the event window.
5. Classify driver type.
6. Classify finding type.
7. Score each driver.
8. Assign Fact / Reaction / Causal Attribution confidence.
9. Generate findings.
10. Generate the narrative story only after scoring.

The workflow should allow a non-narrative conclusion. Some abnormal moves are better explained by fundamentals, sector rotation, macro, flows, policy, valuation, or mean reversion than by narrative shift.

## 6.2 Benchmark Layers

Benchmark Layers define what the price move is compared against. Benchmark layers keep the retrospective from forcing every abnormal return into a narrative-shift explanation. Each layer should be tested against the same disclosure window before it is used as attribution evidence.

| Benchmark layer | What it tests | Required evidence | MRVL v0.9.1 status |
|---|---|---|---|
| Stock-specific reaction | Did MRVL move beyond sector beta and closest peers? | T+1 / T+5 / T+20 abnormal return versus SMH, SOXX, AVGO, NVDA, and expanded peers | Supported for W1 and W5; W4 high immediate / Low-Medium sustained |
| Company fundamentals / guidance | Did reported results or forward targets change the business outlook? | Revenue, guide, long-term targets, segment mix, backlog, bookings, design wins | Partially supported; needs follow-through |
| Analyst / consensus model | Did forward models change after the event? | FY+1 / FY+2 revenue, EPS, EBITDA, target-price and rating changes | Pending |
| Valuation spread | Did MRVL receive a different multiple versus peers? | EV/Sales, forward P/E, revenue multiple versus AVGO, NVDA, AMD, ANET, optical peers, and SOXX median | Pending |
| Customer / ecosystem validation | Did external customers, partners, or ecosystem actors validate the narrative? | Customer, hyperscaler, NVIDIA, partner, or official ecosystem source | Pending |
| Macro / rates | Was the move explained by risk appetite, rates, credit, dollar, or liquidity? | QQQ/SPY, 10Y yield, credit spreads, dollar, liquidity indicators | Not yet tested |
| Flow / positioning | Was the move driven by short covering, ETF flows, options, or institutional positioning? | Volume, options, short interest, ETF flows, 13F / ownership data | Not yet tested |
| Policy / regulatory | Was the move linked to export controls, tariffs, subsidies, antitrust, or industrial policy? | Official policy source, exposure map, sector reaction | Not central; standard check only |
| Technical / mean reversion | Was the move a reversal after overreaction? | Prior drawdown, support/resistance, volume, momentum, lack of new confirming evidence | Possible for W4 after 20D reversal |
| Margin / EPS conversion | Did revenue growth convert into earnings power? | Gross margin, operating margin, EPS, operating leverage | Pending |


## 6.2.1 Expanded Data Layer

The current price map supports W1 and W5 as stock-specific reactions against SMH, SOXX, AVGO, and NVDA. However, this is not yet full peer-relative validation. A stronger version should expand the data panel before upgrading causal attribution.

| Data layer | Instruments / metrics | Purpose | Required windows | MRVL v0.9.1 status |
|---|---|---|---|---|
| Broad market | QQQ, Nasdaq-100, SPY | Control for market-wide risk-on / risk-off | W1-W6 | [ADD] |
| Semiconductor sector | SMH, SOXX | Control for chip-sector beta | W1-W6 | Partially done |
| Core AI / data-center peers | AVGO, AMD, QCOM, NVDA, ANET | Test stock-specific reaction against closer peers | W1-W6 | Expand beyond AVGO/NVDA |
| Optical / interconnect peers | LITE, COHR, CIEN | Test whether optical / interconnect narrative moved as a group | W5-W6 | [ADD] |
| Trading / positioning | Volume vs 20D average, short interest, options implied move, put/call, ETF flows | Test whether price action was flow-driven | W1/W4/W5/W6 | Pending |
| Consensus model | FY+1/FY+2 revenue, EPS, EBITDA, target price, rating | Test whether forward assumptions changed | W1/W4/W5/W6 | Pending |

Expanded price data can raise Reaction confidence, but it cannot by itself raise Causal Attribution confidence to High.

## 6.2.2 Valuation Re-rating Layer

Valuation re-rating should not be inferred from price action alone. The test is whether MRVL’s forward multiple changed versus its own history and versus peer median around the same event windows. A narrative shift becomes stronger only if valuation spread, consensus revision, analyst language, and operating follow-through point in the same direction.

| Window | Date point | MRVL EV/NTM Revenue | MRVL forward P/E | Peer median EV/NTM Revenue | Peer median forward P/E | MRVL premium / discount | Interpretation |
|---|---|---:|---:|---:|---:|---:|---|
| W1 | T-20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Pre-event valuation setup |
| W1 | T+20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Test derating |
| W4 | T-20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Pre-event visibility-risk setup |
| W4 | T+20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Test whether derating persisted |
| W5 | T-20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Pre-positive-window setup |
| W5 | T+20 | [ADD] | [ADD] | [ADD] | [ADD] | [ADD] | Test rerating |
| W6 | T+20 | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | [CALCULATE] | Test TAM / breadth reinforcement |

| Window | Stock move | FY+2 revenue estimate change | FY+2 EPS estimate change | EV/Sales change | Forward P/E change | Main driver | Valuation attribution |
|---|---:|---:|---:|---:|---:|---|---|
| W1 | -29.85% 20D | [ADD] | [ADD] | [ADD] | [ADD] | [Estimate cut / multiple compression / both] | Pending |
| W4 | -18.60% 1D; -18.00% 5D; +7.69% 20D | [ADD] | [ADD] | [ADD] | [ADD] | [Reversal / no durable derating / both] | Pending |
| W5 | +41.53% 20D | [ADD] | [ADD] | [ADD] | [ADD] | [Estimate revision / multiple rerating / both] | Pending |
| W6 | [CALCULATE] | [ADD] | [ADD] | [ADD] | [ADD] | [TAM reinforcement / no price proof yet] | Pending |

A stock move should not be labeled valuation rerating unless forward multiples expand versus the company’s own pre-event baseline and versus the selected peer median. If price rises only because revenue or EPS estimates rise, classify it as estimate-driven rather than multiple-driven.

Until these fields are populated with reliable historical forward valuation and consensus data, valuation attribution must remain Pending.

## 6.2.3 Data Quality Mode

The skill should support two data modes so that it can run with limited public data while still distinguishing basic price reaction from research-grade causal attribution.

| Mode | Data available | What it can support | What it cannot support |
|---|---|---|---|
| Basic mode | Price data, broad market ETFs, sector ETFs, close peers, company releases | Reaction confidence and preliminary finding classification | High causal attribution, valuation rerating, market-model shift |
| Research mode | Consensus estimates, historical forward multiples, sell-side revisions, target prices, analyst language, flow / positioning data | Causal attribution upgrade, valuation rerating test, market-model shift test | Still cannot confirm without later fundamental follow-through |

Expanded price data can raise Reaction confidence. Valuation and consensus data can raise Causal Attribution confidence. Price data alone cannot raise Causal Attribution confidence to High.


## 6.3 Candidate Driver Taxonomy

Candidate Driver Taxonomy defines what type of explanation is being tested after an abnormal window is identified.

| Driver type | What it covers | Evidence required |
|---|---|---|
| Company fundamentals | Revenue, margins, EPS, backlog, customer wins, or operating deterioration | Primary financial disclosures and later operating follow-through |
| Expectations / visibility | Guidance, design-win timing, customer concentration, or custom-silicon lumpiness | Guidance, transcript language, estimate revisions, customer or backlog evidence |
| Sector | Semiconductor or AI-sector rotation and peer sympathy | SMH/SOXX, declared peer basket, and sector breadth |
| Macro / rates | Discount rates, liquidity, risk appetite, credit, or dollar conditions | QQQ/SPY, rates, credit spreads, dollar, and liquidity indicators |
| Flow / positioning | Short covering, crowded positioning, options, ETF, or institutional flows | Volume, options, short interest, ETF flows, and 13F data |
| Policy / regulatory | Export controls, tariffs, subsidies, antitrust, or other regulatory exposure | Official policy source, company exposure map, and sector reaction |
| Valuation | Multiple expansion or compression relative to peers | EV/Sales, forward P/E, revenue multiple, and peer spread |
| Analyst / consensus | Estimate, rating, target-price, or model-framework changes | Dated FY+1/FY+2 estimates, ratings, target prices, and analyst language |
| Technical / mean reversion | Reversal after overreaction without equivalent new information | Prior drawdown, technical conditions, volume, and event chronology |

## 6.4 Candidate Driver Attribution Matrix

| Window | Price anomaly | Candidate driver | Driver type | Finding type | Direction | Evidence | Benchmark support | Expanded data support | Valuation support | Attribution score | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | -19.81% 1D; negative abnormal return persists through 20D | Near-consensus guide failed to clear elevated AI expectations | Expectations / visibility; possible fundamental disappointment versus expectations | Price anomaly + expectation reset + possible fundamental disappointment versus expectations | Negative | S1, S2; §6 price map | Strong versus SMH, SOXX, AVGO/NVDA basket through 20D | Current narrow benchmark support is strong; broader market, expanded peer basket, volume, positioning, and consensus data remain pending. | Pending. Need T-20 to T+20 EV/Sales, forward P/E, peer spread, and estimate-revision decomposition. | 3 / 4 | Fact: High; Reaction: High; Causal Attribution: Pending |
| W4 | -18.60% 1D and -18.00% 5D; +7.69% by 20D | Below-consensus guide and custom ASIC visibility pressure, followed by reversal | Expectations / visibility; technical / mean reversion | Guidance / custom ASIC visibility pressure + possible mean reversion after 20D reversal | Negative initially; reversed | S5; §6 price map | Strong negative abnormal return through 5D, but little sector-relative abnormal return at 20D | Current benchmark support is strong through 5D but weak by 20D; expanded peer, technical, volume, and positioning checks remain pending. | Pending. Need to test whether the immediate derating persisted or reversed by T+20. | 2 / 4 | Fact: High; Reaction: High immediate / Low-Medium sustained; Causal Attribution: Pending |
| W5 | +18.35% 1D and +41.53% 20D | FY2027/FY2028 guidance and long-term target | Company fundamentals / guidance; candidate narrative / valuation | Price anomaly + guidance raise / long-term target + candidate narrative shift | Positive | S6; §6 price map | Strong versus SMH, SOXX, AVGO/NVDA basket through 20D | Current narrow benchmark support is strong through 20D; broad market, expanded peer basket, optical/interconnect peers, and consensus model data remain pending. | Pending. Need to test whether the +41.53% 20D move was driven by estimate revision, multiple expansion, or both. | 3 / 4 | Fact: High; Reaction: High; Causal Attribution: Pending |
| W6 | [CALCULATE] | FY2029 custom-chip target, hyperscaler breadth, and product-scope broadening | Company fundamentals / management-reported customer breadth | TAM / customer breadth reinforcement / candidate narrative shift | Candidate positive | S7 | [CALCULATE] | Pending. W6 price reaction, broad market, sector, peer, and optical/interconnect comparison are still [CALCULATE]. | Pending. Need valuation and consensus data before treating W6 as market-model evidence. | Pending | Fact: High for targets; Reaction: Pending; Causal Attribution: Pending |

## 6.5 Finding Type Taxonomy

| Finding type | Definition | Evidence needed | Common false positive |
|---|---|---|---|
| Narrative shift | Market starts valuing the company under a different business category or forward story | Language shift, valuation spread, analyst model change, external validation, sustained price reaction | Confusing one strong price move with narrative change |
| Fundamental improvement | Business results or forward assumptions improve | Revenue, margin, EPS, backlog, guidance, customer wins | Treating management targets as realized performance |
| Fundamental deterioration | Business results or outlook worsen | Missed guidance, margin compression, demand slowdown, backlog decline | Overreacting to temporary lumpiness |
| Sector rotation | Stock moves because capital rotates into or out of the sector | Sector ETF / peer basket comparison | Calling sector beta stock-specific |
| Macro / rate regime change | Stock moves because discount rates, liquidity, or risk appetite changed | QQQ/SPY, rates, credit spreads, dollar, liquidity indicators | Forcing company-specific explanations onto macro moves |
| Flow / positioning | Move reflects crowded positioning, short covering, ETF flow, or institutional buying/selling | Volume, short interest, options, ETF flow, 13F | Mistaking flow for fundamental conviction |
| Policy / regulatory | Policy, export controls, subsidies, antitrust, tariffs, or regulation affected expectations | Official policy source, company exposure, sector reaction | Overstating policy relevance without exposure mapping |
| Valuation rerating | Multiple changes relative to peers | EV/Sales, forward P/E, revenue multiple, peer spread | Confusing earnings revision with multiple expansion |
| Analyst / consensus model change | Sell-side or consensus assumptions change | Ratings, target prices, FY+1/FY+2 revenue/EPS estimates | Treating reactive target changes as causal |
| Mean reversion | Move reflects reversal after overreaction | Prior drawdown, technical conditions, lack of new information | Calling a bounce a thesis change |

## 6.6 Attribution Scoring Rubric

| Score | Requirement |
|---:|---|
| 0 | Required event, return, or benchmark evidence is unavailable. |
| 1 | Timing coincidence or one evidence layer supports the candidate driver. |
| 2 | Credible event evidence and directional price reaction align, but benchmark or follow-through support is weak. |
| 3 | Credible event evidence, benchmark comparison, and multi-window follow-through support a stock-specific reaction. |
| 4 | Multiple independent causal layers align, including operating, analyst, valuation, customer, backlog, policy, or flow evidence as applicable. |

An attribution score measures the evidence stack, not certainty about cause. Price action alone may support Reaction confidence, but it cannot establish Causal Attribution confidence.

## 6.7 Finding Confidence Rubric

| Confidence level | Requirement |
|---|---|
| Low | Finding is based on timing coincidence, weak source, or one-day price action only |
| Medium | Finding is supported by credible event evidence and benchmark comparison, but lacks model / valuation / follow-through confirmation |
| High | Finding is supported by event evidence, peer-relative move, source quality, and at least one follow-through layer such as analyst revision, valuation spread, guidance, backlog, or customer validation |
| Confirmed | Finding is supported by multiple independent layers and later fundamental follow-through |

No finding should be labeled Confirmed from price action alone. Confirmed findings require independent evidence beyond abnormal return.

## 6.8 Story Generation Rule

The final story should not assume narrative shift by default. It should first state which finding types are supported, which are pending, and which are rejected. The story is generated from the scored evidence, not used to justify the scorecard after the fact. If the scorecard is incomplete, the story must preserve uncertainty.

## 6.9 Story Synthesis After Scoring

Story synthesis should come after driver scoring, not before it. The output should read as a staged explanation, not a single-catalyst narrative.

| Phase | Window | Stage label | What the evidence supports | What remains unproven |
|---|---|---|---|---|
| Phase 1 | W1 | Expectation reset | MRVL had strong data-center growth, but the stock-specific selloff shows elevated AI expectations were not cleared. | Whether the market lowered estimates, valuation multiples, or only de-risked positioning. |
| Phase 2 | W2 / W3 | Mixed transition evidence | Management emphasized custom AI silicon and data-center demand, while non-AI weakness and margin questions kept the setup incomplete. | Whether these events produced a measurable market-model change. |
| Phase 3 | W4 | Custom visibility retest | The immediate selloff maps to ASIC lumpiness and visibility concerns. The 20D reversal makes durable negative attribution weak. | Whether estimate revisions or transcript evidence confirm a lasting concern. |
| Phase 4 | W5 | Long-term target validation candidate | W5 is the strongest positive price-reaction window because MRVL outperformed SMH/SOXX and the AVGO/NVDA basket through 1D, 5D, and 20D. | Whether the reaction represented valuation rerating, consensus revision, or external validation rather than price momentum alone. |
| Phase 5 | W6 | TAM / breadth reinforcement | FY2029 custom chip targets and hyperscaler breadth claims may reinforce the candidate platform narrative. | Price reaction is still [CALCULATE], and customer-side validation remains missing. |

**Staged story:** MRVL moved through expectation reset, mixed transition evidence, custom-visibility retest, and later long-term target validation. This staged story is useful, but it is still not a confirmed narrative shift. Causal attribution remains pending until analyst model changes, valuation spread, customer / ecosystem validation, backlog or design-win visibility, and margin / EPS conversion align with the same event windows.


## 7. Narrative Shift Hypothesis Map

### 7.1 Old narrative

MRVL had AI exposure, but investors questioned whether custom silicon and data-center growth were visible enough to justify elevated expectations. The March 2025 selloff is the cleanest early event showing that expectations, not reported growth alone, were the issue. Fact confidence: **High**. Reaction confidence: **High after W1 calculation**. Causal attribution confidence: **Pending**.

### 7.2 Transition narrative

From May to August 2025, evidence stayed mixed. The company emphasized custom AI silicon and data center strength, but non-AI weakness and custom ASIC lumpiness limited confidence. Fact confidence: **Medium-High**. Reaction confidence: **Pending / mixed**. Causal attribution confidence: **Pending**.

### 7.3 Candidate new narrative

The candidate new narrative is that MRVL moved from an expectation-sensitive custom ASIC supplier toward a broader AI infrastructure participant across custom silicon, interconnect, optics, and data-center scale-out / scale-up infrastructure. This is a narrative-shift hypothesis, not a confirmed conclusion. Fact confidence: **High** for stated targets. Reaction confidence: **High for W5 stock-specific reaction**. Causal attribution confidence: **Pending** until analyst model changes, valuation spread, customer / ecosystem validation, backlog or design-win visibility, and margin / EPS conversion are tied to the same windows.

### 7.4 Evidence limiting the shift

- External ecosystem validation should require customer-side, partner-side, or ecosystem-side sources; management-reported breadth alone is not enough.
- Customer concentration may remain even if engagements are broad.
- Custom ASIC revenue may still be lumpy.
- Margin and EPS conversion remain separate from revenue growth.
- A stock move may be sector beta, Nvidia halo, or ETF/index flow.
- Long-term TAM and revenue targets may already be priced in.

## 8. Attribution Hypotheses

### 8.1 W1 — March 2025 expectation reset

**Primary attribution hypothesis:** W1 may reflect an AI-expectation reset: guidance was near consensus while the market expected stronger AI upside. **Affected assumptions:** AI revenue acceleration, valuation multiple, total-company growth. **Evidence:** Reuters reported a ~15% after-hours selloff and analyst commentary around elevated expectations; data-center growth was still strong. [S1], [S2] **Alternatives:** sector compression, macro risk-off, AI beta reversal, positioning reversal. **Fact confidence:** High. **Reaction confidence:** **High** for stock-specific reaction. **Causal attribution confidence:** **Pending**.

### 8.2 W4 — August 2025 custom ASIC visibility retest: immediate reaction, weak sustained attribution

W4 is useful because it shows why one-day attribution is dangerous: the immediate reaction was severe, but the 20D reversal weakens the claim that this event produced a durable negative narrative shift.

**Primary attribution hypothesis:** W4 may reflect renewed concern that custom ASIC growth was less smooth than expected. **Affected assumptions:** custom silicon durability, customer concentration, valuation multiple. **Evidence:** Reuters reported below-consensus Q3 guidance, >12% after-hours decline, and analyst concern around ASIC lumpiness; management framed lumpiness as normal. [S5] **Alternatives:** AI semi weakness, capex skepticism, customer-specific uncertainty, sector de-risking. **Fact confidence:** High. **Reaction confidence:** **High immediate / Low-Medium sustained** because negative relative returns through T+5 reversed by T+20. **Causal attribution confidence:** **Pending** until estimate-revision and transcript follow-through are verified.

### 8.3 W5 — March 2026 long-term target shift: primary positive narrative-shift test window

W5 is the strongest positive event window in this example because the relative return evidence supports a durable stock-specific reaction across 1D, 5D, and 20D.

**Primary attribution hypothesis:** W5 may be the first clearer re-rating test because explicit FY2027/FY2028 targets supported a broader AI infrastructure frame. **Affected assumptions:** data-center durability, long-term revenue, valuation, design-win visibility. **Evidence:** Reuters reported FY2028 revenue near $15B, FY2027 growth above 30%, and ~15% after-hours share gain; targets remain forecasts. [S6] **Alternatives:** AI sector beta, Nvidia halo, capex optimism, ETF/index flows, short covering. **Fact confidence:** High. **Reaction confidence:** **High** for stock-specific reaction. **Causal attribution confidence:** **Pending** for the cause.

### 8.4 W6 — May 2026 custom chip TAM reinforcement

**Primary attribution hypothesis:** W6 may reinforce the platform narrative, but it is not attribution evidence until price data is calculated. **Affected assumptions:** custom silicon TAM, customer breadth, hyperscaler durability. **Evidence:** Reuters reported FY2029 custom chip revenue above $10B, FY2028 forecast raised to $16.5B, and engagements across all U.S. hyperscalers; customer breadth still needs validation. [S7] **Alternatives:** sector AI optimism, Broadcom / Nvidia halo, hyperscaler capex headlines. **Fact confidence:** High for targets; Medium-High for breadth. **Reaction confidence:** **Pending**. **Causal attribution confidence:** **Pending**.

## 9. True Signal vs Noise

### 9.1 Stronger signals

| Signal | Why it mattered | Evidence | Attribution strength | Confidence |
|---|---|---|---|---|
| Numerical long-term targets | Converts vague AI exposure into measurable expectations | FY2028 ~$15B, later $16.5B; FY2029 custom chip >$10B. [S6], [S7] | W5 stock-specific reaction supported; W6 Pending | Fact: High; Reaction: High for W5 / Pending for W6; Causal: Pending |
| Data center becomes central | Makes MRVL less dependent on legacy segment framing | Data center about 75%–76% of revenue. [S2], [S4] | W1/W4/W5 windows calculated; causal attribution Pending | Fact: High; Reaction: High for W1/W5, Low-Medium sustained for W4; Causal: Pending |
| Custom silicon breadth | Addresses customer concentration concern | “Across all U.S. hyperscalers” reported by Reuters. [S7] | Pending until customer validation and price follow-through are tested | Fact: Medium-High; Reaction: Pending; Causal: Pending |
| Event directly maps to old fear | March/August moves connect to expectations and custom visibility | Reuters and analyst commentary. [S2], [S5] | W1 stock-specific reaction supported; W4 weak sustained after 20D reversal | Fact: High; Reaction: High for W1 / Low-Medium sustained for W4; Causal: Pending |

### 9.2 Weaker or noisy signals

| Signal | Why weaker | Risk of overinterpretation |
|---|---|---|
| Management optimism alone | Forward-looking and self-interested | Treating IR language as validation |
| Generic AI headlines | Often sector-wide | Confusing AI beta with MRVL-specific re-rating |
| One-day price spikes | May reflect positioning | Calling causality before T+5/T+20 |
| Sell-side upgrades after the move | Can be reactive | Confirmation bias |
| Customer rumors | Often unsourced | Building thesis on Tier 5 sentiment |

## 10. Lessons Learned

| Lesson | Why it mattered in MRVL | Future application | False positive risk |
|---|---|---|---|
| Good numbers can still sell off. | Q4 FY2025 data-center growth was strong, but guidance did not clear elevated AI expectations. | Compare reported numbers to implied expectations. | Treating every post-earnings selloff as thesis failure. |
| Custom ASIC stories need window discipline. | Lumpiness repeatedly challenged visibility. | Track design wins, ramp timing, breadth, and sequential revenue. | Confusing temporary lumpiness with structural weakness. |
| Platform narratives need breadth. | Stronger evidence required hyperscaler and product-layer breadth. | Look for customer and product diversification. | Treating one large customer as platform proof. |
| Price action must be peer-relative. | Reported +15% or -12% moves are insufficient without SMH/SOXX and peer comparison. | Calculate T+1, T+5, T+20 relative returns. | Mistaking sector beta for stock-specific attribution. |
| Long-term targets need follow-through. | FY2028/FY2029 targets strengthened the story but remained forecasts. | Pair targets with revenue, bookings, revisions, and margins. | Overwriting uncertainty with management targets. |

## 11. Future Watchlist Rule

### Pattern: AI infrastructure narrative broadening after expectation-reset selloff

**Conditions to monitor:** stock sells off despite strong reported growth; bear case centers on customer concentration, ASIC lumpiness, or follow-on wins; company later gives more specific targets; customer and product-layer breadth become visible; price reaction becomes durable and stock-specific versus SMH/SOXX and peers.

**Evidence required:** primary source evidence; independent Reuters/Bloomberg/WSJ/FT or industry source; T+1/T+5/T+20 relative returns; estimate revision or valuation framework change; follow-up event confirming the same narrative.

**False positive risks:** management commentary without validation; sector-beta rebound; TAM without revenue conversion; unresolved concentration; margin / EPS weakness hidden by revenue growth; priced-in catalyst.

## 12. Source Register

Additional sources should not be added for volume. Each source must serve a defined attribution test: transcript evidence for management language, sell-side revisions for expectation change, customer validation for concentration risk, and valuation data for re-rating evidence. Generic news articles should be excluded unless they add a new claim, contradiction, or event-window explanation.

| Source ID | Date | Source | URL | Tier | Claim / Window IDs | Event / claim covered | Use in retrospective | Limitation |
|---|---|---|---|---|---|---|---|---|
| S1 | Mar 5, 2025 | Marvell FY2025 Q4 / FY2025 results press release | https://www.prnewswire.com/news-releases/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2025-financial-results-302393619.html | Tier 1 | C1F, C2F / W1 | Q4 revenue, data-center growth, Q1 FY2026 guidance | Fact base for W1 | Management source; no independent attribution |
| S2 | Mar 5, 2025 | Reuters, “Chipmaker Marvell forecasts in-line Q1 revenue, but its shares slump” | https://www.reuters.com/technology/chipmaker-marvell-forecasts-first-quarter-revenue-above-estimates-2025-03-05/ | Tier 2 | C1F, C1I, C2F / W1 | March 2025 price reaction and analyst explanation | Reaction evidence for expectations reset | After-hours quote is not the close-to-close return in §6 |
| S3 | May 6, 2025 | Marvell press release, “Marvell to Host Webinar on the Future of Custom Silicon Technology for AI Infrastructure” | https://investor.marvell.com/news-events/press-releases/detail/98/marvell-to-host-webinar-on-the-future-of-custom-silicon-technology-for-ai-infrastructure-postpones-investor-day | Tier 1 | C3F, C3I / W2 | Webinar announcement, investor day postponement, guidance reaffirmation | Evidence of management narrative effort | Does not prove market acceptance |
| S4 | May 29, 2025 | Reuters, “Marvell forecasts second-quarter revenue above estimates on strong demand for custom AI chips” | https://www.reuters.com/technology/chipmaker-marvell-forecasts-second-quarter-revenue-above-estimates-2025-05-29/ | Tier 2 | C4F, C4I / W3 | Q2 guide, data-center mix, custom silicon commentary, weak non-AI segments | Mixed transition evidence | Some claims are analyst interpretation |
| S5 | Aug 28, 2025 | Reuters, “Marvell’s weak data center forecast prompts AI investors to dump its stock” | https://www.reuters.com/technology/chipmaker-marvells-weak-data-center-forecast-prompts-ai-investors-dump-its-stock-2025-08-28/ | Tier 2 | C5F, C5I / W4 | Q3 outlook, custom ASIC lumpiness, stock reaction | Re-test of old fear | Customer-specific claims need verification |
| S6 | Mar 5, 2026 | Reuters, “Marvell projects strong fiscal 2028 revenue on AI-driven data center boom, shares jump” | https://www.reuters.com/technology/marvell-forecasts-first-quarter-revenue-above-estimates-2026-03-05/ | Tier 2 | C6F, C6I / W5 | FY2027/FY2028 targets and reaction | Potential narrative shift evidence | Peer-relative price action does not prove causal attribution |
| S7 | May 27, 2026 | Reuters, “Marvell sees custom chip revenue topping $10 billion by 2029 as AI demand grows” | https://www.reuters.com/technology/marvell-technology-forecasts-quarterly-revenue-above-estimates-2026-05-27/ | Tier 2 | C7F, C7I, C8F, C8I / W6 | FY2029 custom chip target, FY2028 forecast raise, hyperscaler breadth | Narrative reinforcement | Long-term forecast; customer validation still needed |
| S8 | Jun 29, 2026 | Nasdaq Historical Quotes: MRVL, SMH, SOXX, AVGO, NVDA | [MRVL](https://www.nasdaq.com/market-activity/stocks/mrvl/historical), [SMH](https://www.nasdaq.com/market-activity/etf/smh/historical), [SOXX](https://www.nasdaq.com/market-activity/etf/soxx/historical), [AVGO](https://www.nasdaq.com/market-activity/stocks/avgo/historical), [NVDA](https://www.nasdaq.com/market-activity/stocks/nvda/historical) | Tier 4 | W1, W4, W5 price reaction map | Regular-session closing prices for W1, W4, and W5 | Close-to-close price-return calculation | Unadjusted closes; does not capture after-hours path or total return |
| S9 | Mar 5, 2025; Aug 28, 2025; Mar 5, 2026 | Marvell Investor Relations earnings releases for W1, W4, and W5 | [W1](https://investor.marvell.com/news-events/press-releases/detail/109/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2025-financial-results); [W4](https://investor.marvell.com/news-events/press-releases/detail/989/marvell-technology-inc-reports-second-quarter-of-fiscal-year-2026-financial-results); [W5](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results) | Tier 1 | W1, W4, W5 event-window timing | After-hours disclosure timing for W1, W4, and W5 | Effective-T0 determination | Management source; timing evidence only |

## 12.1 Required Source Backlog

These are required source categories, not active sources. They should be added only when they are used to test a defined attribution claim.

| Backlog ID | Date | Source category | URL | Tier | Claim / Window IDs | Event / claim covered | Use in retrospective | Limitation |
|---|---|---|---|---|---|---|---|---|
| B1 | [VERIFY] | Earnings call transcripts for W1, W4, and W5 | [VERIFY URL] | Tier 1 | Transcript claims / W1, W4, W5 | Management language on guidance, lumpiness, hyperscaler breadth, margin conversion | Verify exact wording and separate management facts from interpretation | Transcript language may still be promotional and requires market-reaction testing |
| B2 | [VERIFY] | Sell-side estimate revisions and target-price changes around W1, W4, and W5 | [VERIFY URL] | Tier 3 | Estimate revision claims / W1, W4, W5 | Revenue / EPS / target-price changes after event windows | Test whether expectations actually changed | Sell-side changes may lag price and can be reactive |
| B3 | [VERIFY] | Customer or hyperscaler validation sources | [VERIFY URL] | Tier 1 / Tier 2 | Customer validation claims / W1-W6 | Amazon, Microsoft, or other hyperscaler program confirmation | Verify customer breadth and concentration-risk claims | Do not use rumors or social media as factual validation |
| B4 | [VERIFY] | Event-window valuation snapshot source | [VERIFY URL] | Tier 4 | Valuation reaction claims / W1, W4, W5 | EV/Sales, forward P/E, revenue multiple, or consensus multiple change | Provide event-window valuation snapshots for initial valuation context around W1, W4, and W5 | Market multiple data does not prove causal attribution |
| B5 | [VERIFY] | Macro / rates context dataset | [VERIFY URL] | Tier 4 | Macro driver claims / W1-W6 | QQQ, SPY, 10Y yield, credit spreads, dollar, liquidity indicators around event windows | Test whether abnormal returns were driven by risk-on/risk-off or discount-rate changes | Macro data can explain broad beta but not company-specific causality by itself |
| B6 | [VERIFY] | Flow / positioning dataset | [VERIFY URL] | Tier 4 | Flow driver claims / W1-W6 | Volume, options, short interest, ETF flows, institutional positioning, 13F changes | Test whether moves were driven by crowded positioning, short covering, ETF flows, or institutional rotation | Flow evidence may explain price pressure without proving fundamental change |
| B7 | [VERIFY] | Policy / regulatory source set | [VERIFY URL] | Tier 1 / Tier 2 | Policy driver claims / W1-W6 | Export controls, tariffs, subsidies, industrial policy, antitrust, or regulatory exposure | Test whether policy effects contributed to the event-window reaction | Requires company exposure mapping; do not infer policy impact from generic headlines |
| B8 | [VERIFY] | Technical / mean-reversion dataset | [VERIFY URL] | Tier 4 | Technical / mean-reversion claims / W1-W6 | Prior drawdown, support/resistance, RSI, moving averages, volume, volatility, and reversal pattern | Test whether W4-like moves are better explained by technical reversal or mean reversion | Technical evidence is contextual and cannot prove fundamental attribution |
| B9 | [VERIFY] | Historical forward valuation dataset | [VERIFY URL] | Tier 4 | Valuation rerating claims / W1-W6 | EV/NTM Revenue, forward P/E, EV/EBITDA, peer median, premium / discount | Test whether MRVL experienced multiple expansion or compression around event windows | Requires reliable historical consensus and enterprise value data |
| B10 | [VERIFY] | Consensus estimate revision dataset | [VERIFY URL] | Tier 4 | Estimate revision claims / W1-W6 | FY+1/FY+2 revenue, EPS, EBITDA, target price, rating changes | Decompose stock move into estimate revision versus multiple expansion | Public data may be incomplete or stale |
| B11 | [VERIFY] | Expanded peer price dataset | [VERIFY URL] | Tier 4 | Expanded benchmark claims / W1-W6 | QQQ, SPY, AVGO, AMD, QCOM, NVDA, ANET, LITE, COHR, CIEN | Test whether reaction remains stock-specific under broader peer comparison | Peer selection can bias attribution if not declared before analysis |

## 13. Open Questions / Needs Verification

### 13.1 Price and relative-return work

- Calculate exact MRVL T+1, T+5, and T+20 price moves for W2, W3, and W6, or keep them as secondary windows.
- Compare W2, W3, and W6 against SMH, SOXX, AVGO, NVDA, and optical/networking peers.
- Expand the peer basket beyond AVGO/NVDA in a future version; consider AMD, QCOM, ANET, LITE, COHR, and a broader semiconductor index.
- Determine whether the May 2026 move was stock-specific or sector-wide.

### 13.2 Expectation-change evidence

- Verify whether W1, W4, and W5 produced sell-side estimate revisions or target-price changes in the same direction as the price reaction.
- Verify whether W5 involved valuation multiple expansion, not only revenue-estimate revision.
- Map sell-side estimate revisions and target-price changes to event windows.

### 13.3 Transcript, customer, and claim-quality checks

- Verify transcript language around “lumpiness,” customer breadth, guidance, and margin conversion.
- Verify whether customer breadth claims were supported by customer-side evidence or only management commentary.
- Verify Amazon, Microsoft, and other hyperscaler program claims.
- Classify any Nvidia ecosystem or partnership claim as official, reported, or speculative.

### 13.4 Fundamental follow-through

- Test whether margin and EPS followed revenue targets.


### 13.5 Data and valuation audit

- Add QQQ, SPY, AMD, QCOM, ANET, LITE, COHR, and CIEN to the event-window return panel.
- Calculate W2, W3, and W6 T+1 / T+5 / T+20 returns.
- Calculate W1, W4, W5, and W6 valuation snapshots at T-20 and T+20.
- Test whether W5’s +41.53% 20D move was driven by estimate revision, multiple expansion, or both.
- Verify whether MRVL’s valuation spread expanded versus core AI / data-center peers after W5.
- Keep causal attribution Pending until valuation and consensus data map to the same event windows.

## 14. Final Retrospective Takeaway

MRVL shows why investment retrospectives should start from price anomalies, not from a pre-written narrative. The workflow first identifies abnormal windows, benchmarks the move against market, sector, peer, valuation, and fundamental layers, then classifies candidate drivers and finding types before assigning confidence. In MRVL, the evidence supports a staged sequence: W1 expectation reset, W4 custom ASIC visibility retest with weak sustained attribution, and W5 long-term target validation candidate. The case remains a candidate narrative shift rather than a confirmed shift because analyst model changes, valuation spread expansion, customer / ecosystem validation, backlog / design-win visibility, and margin / EPS conversion remain pending. The v0.9.1 patch adds the missing audit path: expanded benchmark data can strengthen reaction confidence, while valuation and consensus data are required before the case can move toward market-model shift.
