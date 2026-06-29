# Investment Retrospective Skill

## Purpose

This skill creates disciplined investment retrospectives for public-market equities by starting from abnormal price windows and testing candidate drivers before generating a narrative.

The purpose is not to produce a buy/sell recommendation. The purpose is to help investors understand what likely changed, what did not change, what evidence is missing, and whether a past price move was driven by fundamentals, expectations, sector rotation, macro conditions, valuation, flows, policy, mean reversion, or narrative shift.

The core discipline is simple:

Price anomaly first.
Benchmark before attribution.
Confidence before story.

---

## Language Policy

- Match the user's requested output language.
- If the user explicitly requests English, produce the report in English.
- If the user explicitly requests Chinese, produce the report in Chinese.
- If the user does not specify an output language, match the main language of the user's input.
- Preserve core audit labels in English unless the user explicitly asks for full localization:
  - Fact confidence
  - Reaction confidence
  - Causal Attribution confidence
  - Claim Ledger
  - Price Reaction & Relative Return Map
  - Candidate Driver Attribution Matrix
  - Source Register
  - Required Source Backlog
- Company names, tickers, event window IDs, claim IDs, source IDs, confidence grades, and numeric evidence must remain consistent across languages.
- Translating or localizing the report must not change facts, scores, confidence labels, source quality, attribution limits, or narrative-shift classification.

---

## Non-Goals

This skill must not:

* Provide buy, sell, hold, or price-target recommendations.
* Forecast future returns.
* Treat price action as proof of causality.
* Treat management commentary as independent validation.
* Treat a single strong price move as confirmed narrative shift.
* Invent valuation, consensus, flow, or customer-validation data.
* Add sources only for volume.
* Rewrite uncertainty into certainty.
* Ignore missing data.

When evidence is incomplete, the output must preserve uncertainty using `[CALCULATE]`, `[VERIFY]`, `[ADD]`, or `Pending`.

---

## Required Workflow

When producing an investment retrospective, follow this workflow in order.

### 1. Define the retrospective question

State the central retrospective question clearly.

Examples:

* When did the market begin to treat the company differently?
* Was the move caused by fundamentals, expectations, valuation, sector beta, macro, flow, or narrative shift?
* Did the market overreact, re-rate, or simply follow the sector?

The question should be testable through event windows and evidence.

---

### 2. Identify abnormal price windows

Start from price behavior, not from a pre-written story.

Define the abnormal windows using event dates and effective trading dates.

Required horizons:

* T+1
* T+5
* T+20

Optional horizons:

* T+60
* 1Q
* 6M+
* full drawdown / recovery period

If the event was disclosed after market close, use the next regular session as effective T0.

If timing is unclear, preserve `[VERIFY TIME]`.

---

### 3. Benchmark the move

Before assigning attribution, compare the stock against relevant benchmarks.

Minimum benchmark layers:

* Broad market index or ETF
* Sector ETF
* Close peer basket
* Expanded peer basket if relevant
* Valuation spread if available

Price action should be described as stock-specific only when the stock materially outperforms or underperforms the appropriate benchmarks over the same event window.

Do not classify a move as company-specific if the sector or peer basket moved similarly.

---

### 4. Build the event window map

For each window, define:

* Window ID
* Anchor event
* Event date
* Disclosure timing
* Effective T0
* Pre-event fear or setup
* Reaction window
* Follow-through window
* Calculation required
* Attribution test

The event window map is the backbone of the retrospective.

---

### 5. Build the claim ledger

Separate claims into:

* Fact claims
* Interpretation claims
* Reaction claims
* Inference claims
* Speculation

Every important claim must include:

* Window ID
* Source
* Claim type
* Fear or assumption mapped
* Fact confidence
* Reaction confidence
* Causal attribution confidence

Fact claims and interpretation claims must not be mixed.

---

### 6. Classify candidate drivers

After identifying an abnormal window, classify possible drivers.

Allowed driver types:

* Company fundamentals
* Expectations / visibility
* Guidance revision
* Customer / partner validation
* Analyst / consensus revision
* Valuation
* Sector rotation
* Macro / rates
* Flow / positioning
* Policy / regulatory
* Technical / mean reversion
* Narrative shift

The output must allow non-narrative conclusions.

Not every abnormal price move is a narrative shift.

---

### 7. Classify finding types

Allowed finding types:

* Price anomaly
* Fundamental improvement
* Fundamental deterioration
* Expectation reset
* Guidance revision
* Analyst / consensus model change
* Valuation rerating
* Sector rotation
* Macro / rate regime change
* Flow / positioning
* Policy / regulatory
* Mean reversion
* Narrative shift

The finding type should describe what the evidence supports, not what sounds most interesting.

---

### 8. Score attribution

Use a 0–4 attribution score.

| Score | Requirement                                                                                                                                   |
| ----: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|     0 | Required event, return, or benchmark evidence is unavailable.                                                                                 |
|     1 | Timing coincidence or one evidence layer supports the candidate driver.                                                                       |
|     2 | Credible event evidence and directional price reaction align, but benchmark or follow-through support is weak.                                |
|     3 | Credible event evidence, benchmark comparison, and multi-window follow-through support a stock-specific reaction.                             |
|     4 | Multiple independent causal layers align, including operating, analyst, valuation, customer, backlog, policy, or flow evidence as applicable. |

An attribution score measures the evidence stack, not certainty about cause.

Price action alone may support Reaction confidence, but it cannot establish Causal Attribution confidence.

---

### 9. Assign three separate confidence labels

Always separate:

1. Fact confidence
2. Reaction confidence
3. Causal attribution confidence

Definitions:

| Confidence type               | Meaning                                                                  |
| ----------------------------- | ------------------------------------------------------------------------ |
| Fact confidence               | Whether an event, number, quote, or disclosure is accurate.              |
| Reaction confidence           | Whether price action is stock-specific versus market, sector, and peers. |
| Causal attribution confidence | Whether the evidence explains why the market moved.                      |

Hard rule:

Reaction confidence and causal attribution confidence are not the same.

A stock can have High Reaction confidence and Pending Causal Attribution confidence.

---

### 10. Apply narrative shift classification only after scoring

Narrative shift is a classification outcome, not the default explanation.

Use the following levels:

| Level   | Classification                       | Meaning                                                                                                              |
| ------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Level 0 | No shift                             | Events occurred, but no meaningful stock-specific reaction or expectation change is visible.                         |
| Level 1 | Reaction only                        | Stock moved abnormally, but forward assumptions are not shown to have changed.                                       |
| Level 2 | Company-framed candidate shift       | Management provides stronger guidance, targets, TAM, or product framing, but external validation is incomplete.      |
| Level 3 | Externally validated candidate shift | Customer, partner, ecosystem, backlog, or design-win evidence supports the company framing.                          |
| Level 4 | Market-model shift                   | Estimates, target prices, analyst language, valuation spreads, or peer frameworks change with the same event window. |
| Level 5 | Confirmed narrative shift            | Price, estimates, valuation, external validation, backlog / guidance, and fundamental follow-through align.          |

Hard rules:

* Level 4 cannot be assigned from price action alone.
* Level 5 cannot be assigned without independent validation and later fundamental follow-through.
* Management targets alone cannot confirm narrative shift.
* Customer or partner validation must come from customer-side, partner-side, ecosystem-side, or other reliable external sources.

---

### 11. Add expanded data layer

The retrospective should define the data required to strengthen benchmark confidence.

Required expanded data categories:

| Data layer            | Purpose                                                                   |
| --------------------- | ------------------------------------------------------------------------- |
| Broad market          | Control for market-wide risk-on / risk-off.                               |
| Sector benchmark      | Control for sector beta.                                                  |
| Core peers            | Test stock-specific reaction against closer business peers.               |
| Adjacent peers        | Test whether adjacent industry narratives moved as a group.               |
| Trading / positioning | Test short covering, crowded positioning, options, ETF flows, and volume. |
| Consensus model       | Test whether forward assumptions changed.                                 |

Expanded price data can raise Reaction confidence.

Expanded price data cannot by itself raise Causal Attribution confidence to High.

---

### 12. Add valuation re-rating layer

Valuation rerating must not be inferred from price appreciation alone.

The test is whether the company’s forward multiple changed:

* versus its own pre-event baseline
* versus peer median
* versus its historical range
* alongside consensus revisions
* alongside analyst language or peer-framework changes

Required valuation checks:

* EV / NTM Revenue
* EV / forward revenue
* Forward P/E
* EV / EBITDA where relevant
* Peer median multiple
* Premium / discount versus peers
* Estimate revision versus multiple expansion decomposition

If valuation data is missing, valuation attribution must remain Pending.

If price rises only because revenue or EPS estimates rise, classify it as estimate-driven rather than multiple-driven.

---

### 13. Generate executive attribution takeaway

The report should begin with a concise executive attribution takeaway.

It must include:

* Window
* Price move
* Best-supported finding
* What likely changed
* Reaction confidence
* Causal attribution confidence

The executive takeaway should state the current conclusion without hiding uncertainty.

---

### 13.1 Add a First-read Finding Card

Add a concise First-read Finding Card at the beginning of the report, after Scope and before the executive summary or executive attribution takeaway.

Generate the card only after the claim ledger, candidate-driver matrix, attribution scores, confidence labels, and narrative-shift classification are complete. Its placement is for reading order only; it must not move interpretation ahead of scoring in the research workflow.

Required fields:

* Sharp finding
* Strongest evidence
* Most misleading false signal or strongest limiting evidence
* Current classification
* Still unproven
* Fact confidence
* Reaction confidence
* Causal attribution confidence

Hard rules:

* Summarize only findings already supported in the scored report.
* Do not add a new claim, driver, score, confidence upgrade, or narrative-shift upgrade.
* Preserve material qualifications, overlapping-window limitations, alternative explanations, and `Pending` status.
* Keep the card short enough to scan on first read.
* Do not use the card as a replacement for the executive attribution takeaway, scorecard, or source register.

---

### 14. Generate story only after scoring

The final story must be generated from the scored evidence.

The story must not be used to justify the scorecard after the fact.

The story should be staged, not single-catalyst, unless the evidence clearly supports a single-catalyst explanation.

Required story structure:

* Phase
* Window
* Stage label
* What evidence supports
* What remains unproven

If causal attribution is incomplete, the story must preserve uncertainty.

---

### 15. Maintain source register and source backlog

Every active source must have a defined attribution use.

Source register fields:

* Source ID
* Date
* Source
* URL
* Tier
* Claim / Window IDs
* Event / claim covered
* Use in retrospective
* Limitation

Required source backlog fields:

* Backlog ID
* Date
* Source category
* URL placeholder
* Tier
* Claim / Window IDs
* Event / claim covered
* Use in retrospective
* Limitation

Do not add generic news unless it contributes a new claim, contradiction, timing clarification, or attribution test.

---

## Source Quality Rules

Use source tiers.

| Tier   | Source type                                                                                       |
| ------ | ------------------------------------------------------------------------------------------------- |
| Tier 1 | Company filings, official releases, transcripts, customer / partner official sources, regulators. |
| Tier 2 | Reuters, Bloomberg, WSJ, FT, Nikkei, industry publications with clear sourcing.                   |
| Tier 3 | Sell-side notes, analyst summaries, estimate platforms, expert commentary.                        |
| Tier 4 | Market data vendors, price data, valuation databases, consensus data, ETF flow datasets.          |
| Tier 5 | Social media, forums, unsourced rumors, screenshots, anonymous commentary.                        |

Tier 5 sources may be used only as sentiment context, not as factual validation.

---

## Hard Gates

The output must obey these gates:

* If price data is unavailable, preserve `[CALCULATE]`.
* If event timing is unclear, preserve `[VERIFY TIME]`.
* If source quality is unclear, preserve `[VERIFY]`.
* If valuation data is unavailable, valuation attribution remains Pending.
* If consensus data is unavailable, market-model shift remains Pending.
* If customer / partner validation is unavailable, external validation remains Pending.
* If only management commentary exists, do not classify external validation as confirmed.
* If only one-day price action exists, do not assign High Reaction confidence.
* If price action is strong but valuation / consensus / customer data is missing, keep Causal Attribution confidence Pending.
* If a move is sector-wide, classify it as sector rotation or sector beta, not stock-specific reaction.
* If a move reverses by T+20, flag weak sustained attribution or possible mean reversion.
* Do not upgrade any finding to Confirmed from price action alone.

---

## Required Output Tone

The output should be rigorous, direct, and uncertainty-aware.

Avoid promotional language.

Avoid hindsight storytelling.

Avoid false precision.

Prefer:

* “The evidence supports...”
* “The current evidence does not yet prove...”
* “Reaction confidence is High, but causal attribution remains Pending...”
* “This is a candidate narrative shift, not a confirmed shift...”

Avoid:

* “The stock moved because...”
* “The market realized...”
* “This proves...”
* “Confirmed narrative shift...” unless the confirmation gates are satisfied.

---

## Final Principle

The retrospective should help investors learn from past price moves without rewriting history into a clean story.

The system exists to prevent bad attribution.

Its job is not to make the story more exciting.

Its job is to make the story more testable.
