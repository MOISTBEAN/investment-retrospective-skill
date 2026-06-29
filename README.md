# Investment Retrospective Skill

**Extract real alpha from hindsight, not stories from price moves.**

An evidence-first audit framework for separating facts, price reactions, and causal attribution in investment retrospectives.

Most investment retrospectives start after the price has already moved.

By then, the story usually sounds clean:

> “The stock rallied because the market finally realized it was an AI winner.”

But a clean story is not the same as a verified explanation.

This project helps turn post-move stock narratives into an auditable attribution framework. It separates what happened, how the market reacted, and what can reasonably be attributed to specific drivers based on available evidence.

> Not a trading bot. Not a stock picker. Not investment advice.  
> This is a post-event learning framework for cleaner attribution.

## Why this exists

Markets create stories after every major move.

Some of those stories are useful. Many are just hindsight.

After a stock rallies or sells off, it becomes easy to explain the move using whatever narrative now feels obvious. The chart moves first, then the explanation gets rewritten around it.

That creates a problem for investors, analysts, and builders of investment research workflows:

- Price reaction gets confused with causality
- Strong narratives get treated as strong evidence
- Missing sources are ignored
- Benchmark-relative performance is skipped
- Event windows are chosen after the fact
- Confidence levels are rarely separated across facts, reactions, and attribution

This project exists to fight that pattern.

The goal is not to remove judgment from investment analysis. The goal is to make judgment more explicit, more structured, and easier to audit.

A good retrospective should answer three different questions separately:

1. **What happened?**  
   The factual record: filings, earnings, guidance, product launches, customer announcements, regulatory events, financing updates, analyst revisions, or other verifiable events.

2. **How did the market react?**  
   The price and volume response, measured against the relevant event window, benchmarks, peers, sector ETFs, and prior expectations.

3. **What can we actually attribute the reaction to?**  
   The causal interpretation, ranked by evidence quality and confidence rather than narrative convenience.

The key principle is simple:

**Price movement is evidence of reaction.  
It is not, by itself, evidence of causality.**

Investment Retrospective Skill provides a repeatable way to break down a post-move story into:

- Event Window Map
- Benchmark Comparison
- Claim Ledger
- Candidate Driver Attribution Matrix
- Fact / Reaction / Causal Attribution Confidence
- Source Register
- Required Source Backlog
- Narrative Shift Classification
- Lessons and Future Watchlist Rules

The output is not a smoother story.

The output is a cleaner distinction between what is known, what is inferred, and what still needs evidence.

This matters because the best lessons from investing often come from looking backward — but only if hindsight is audited instead of trusted.

## Example coverage

| Example | Case type | Core lesson |
| --- | --- | --- |
| `MRVL` | Candidate narrative shift discipline | A strong price reaction is not enough to confirm a narrative shift. |
| `ASTS` | External validation / pre-revenue commercial pathway | External validation can reduce failure probability before service revenue is proven. |
| `FLNC` | Backlog-to-margin / execution reset / AI infrastructure candidate | Backlog is not the same as revenue timing or margin quality. |

## What this skill does

| Capability | What it does | Why it matters |
| --- | --- | --- |
| Price anomaly first | Starts from abnormal stock moves instead of a prewritten story | Reduces hindsight bias |
| Event Window Map | Anchors each major move to a dated disclosure window | Prevents vague attribution |
| Benchmark comparison | Compares the stock against market, sector, and peer returns | Separates stock-specific reaction from beta |
| Claim Ledger | Tracks facts, interpretations, and attribution claims separately | Makes the research auditable |
| Price Reaction & Relative Return Map | Measures 1D, 5D, and 20D reactions where data are available | Shows whether a move was immediate, sustained, or reversed |
| Candidate Driver Attribution Matrix | Scores possible drivers without treating price as proof | Improves causal discipline |
| Fact / Reaction / Causal Attribution confidence | Separates factual confidence, market-reaction confidence, and causal confidence | Avoids overclaiming |
| Narrative Shift Classification | Classifies whether the evidence supports reaction-only, candidate shift, external validation, or confirmed shift | Makes conclusions more precise |
| Source Register | Records source quality, proximity, and limitations | Keeps the report transparent |
| Required Source Backlog | Lists missing evidence needed for stronger conclusions | Shows what remains unproven |

## What the output looks like

A weak retrospective says:

> “The stock rose because the market finally understood the story.”

This skill forces a cleaner structure:

```text
Price anomaly:
- Was the move abnormal versus benchmarks and peers?

Event window:
- What was knowable at the time?
- Was the event before market, after market, or during session?

Evidence:
- Which claims are primary-source facts?
- Which claims are management statements?
- Which claims are market interpretations?

Confidence:
- Fact confidence: High
- Reaction confidence: High
- Causal Attribution confidence: Pending / Medium / High

Classification:
- Candidate narrative shift, not confirmed
- External validation present
- Valuation / consensus / revenue confirmation still missing
```

The goal is not to create a more convincing explanation.

The goal is to know how much of the explanation the evidence actually supports.

## Core workflow

```text
Price anomaly
      ↓
Event Window Map
      ↓
Benchmark Comparison
      ↓
Claim Ledger
      ↓
Candidate Driver Attribution Matrix
      ↓
Fact / Reaction / Causal Attribution confidence
      ↓
Narrative Shift Classification
      ↓
Lessons + Future Watchlist Rules
```

## Quick start

Clone the repository:

```bash
git clone https://github.com/MOISTBEAN/investment-retrospective-skill.git
cd investment-retrospective-skill
```

Open the core skill file:

```text
SKILL.md
```

Use it with your preferred AI assistant.

Example prompt:

```text
Use the Investment Retrospective Skill to produce a retrospective report for [COMPANY / TICKER].

Start from the price anomaly.
Map the major event windows.
Compare the reaction against relevant benchmarks and peers.
Build a claim ledger.
Separate Fact confidence, Reaction confidence, and Causal Attribution confidence.
Classify whether the evidence supports a narrative shift.

Do not provide investment advice, a price target, or a buy/sell recommendation.
```

For a structured output, start from:

```text
templates/retrospective-report.md
```

For reference examples, review:

```text
examples/mrvl-retrospective.md
examples/asts-retrospective.md
examples/flnc-retrospective.md
```

## Inputs

The skill works best when you provide:

| Input | Examples |
| --- | --- |
| Company and ticker | `MRVL`, `ASTS`, `FLNC` |
| Time range | `2024-01-01 to 2026-06-30` |
| Major events | Earnings, guidance changes, customer announcements, regulatory approvals, short reports, product launches |
| Price data | Stock returns, benchmark returns, peer returns |
| Primary sources | SEC filings, earnings releases, company announcements, customer or regulator statements |
| Secondary sources | Industry reports, analyst commentary, news articles |
| Missing data notes | Consensus estimates, valuation history, short interest, options, flow data |

## Outputs

A completed retrospective can include:

- First-read Finding Card
- Original Market Fear
- Event Timeline
- Event Window Map
- Claim Ledger
- Price Reaction & Relative Return Map
- Benchmark Layers
- Valuation Re-rating Layer
- Candidate Driver Attribution Matrix
- Narrative Shift Map
- True Signal vs Noise
- Lessons Learned
- Future Watchlist Rules
- Source Register
- Required Source Backlog

## Repository structure

```text
investment-retrospective-skill/
├── README.md
├── SKILL.md
├── templates/
│   └── retrospective-report.md
├── checklists/
│   ├── market-fear-checklist.md
│   ├── true-signal-vs-noise.md
│   └── source-quality-checklist.md
├── examples/
│   ├── mrvl-retrospective.md
│   ├── asts-retrospective.md
│   └── flnc-retrospective.md
├── scripts/
│   └── validate_structure.py
└── tests/
    ├── 01_core_skill_contract.md
    └── 02_supporting_docs_smoke_audit.md
```

## Language support

The skill can produce reports in English or Chinese.

By default, it matches the user's input language while preserving core audit labels for consistency:

- Fact confidence
- Reaction confidence
- Causal Attribution confidence
- Claim Ledger
- Price Reaction & Relative Return Map
- Candidate Driver Attribution Matrix
- Source Register
- Required Source Backlog

## Recommended first use

Start with one stock, one clearly bounded 12–24 month period, and a small set of manually provided materials.

Prefer:

- SEC filings
- Earnings releases
- Official customer or partner announcements
- Regulator statements
- Reputable industry reporting
- Dated market data

Complete one careful report before attempting automation or expanding the universe.

## Validation

This repository includes lightweight validation and smoke-audit files to help preserve the core attribution contract.

Optional local validation:

```bash
python3 scripts/validate_structure.py SKILL.md examples/mrvl-retrospective.md
```

The validator checks whether the core skill contract and example structure still preserve required phrases and attribution discipline.

## Suitable use cases

Use this project for:

- Post-event stock retrospectives
- Studying narrative-driven revaluations
- Reviewing major drawdowns and rebounds
- Separating real business changes from market overreaction
- Building AI-assisted investment research workflows
- Creating structured case studies for learning and review

## Not suitable for

Do not use this project as:

- A stock picker
- A trading bot
- A forecasting model
- A valuation engine
- A real-time market monitor
- A replacement for professional financial advice
- A tool for producing buy, sell, or hold recommendations

## Guardrails

- Do not fabricate events, dates, sources, quotes, financial data, customer names, or price moves.
- Do not treat price movement alone as proof of causality.
- Always include plausible alternative explanations for major moves.
- Always separate fact, management claim, market reaction, inference, and attribution hypothesis.
- Always mark evidence strength and confidence.
- Preserve the information set available at the time to reduce hindsight bias.
- Use this framework for research education, not financial advice.

## Roadmap

- **v0.1:** Evidence-first retrospective framework with MRVL, ASTS, and FLNC examples
- **v0.1.x:** Reader-facing brief template and README clarity improvements
- **v0.2:** Optional structured JSON sidecar for event windows and claim ledgers
- **v0.3:** Stronger validation checks for confidence labels and narrative-shift classification
- **v0.4:** Optional lightweight tooling for CSV timeline and price-reaction mapping

## License

TBD.

## Disclaimer

This project is for research and educational use only.

It is not investment advice, financial advice, or a recommendation to buy, sell, or hold any security. All examples are retrospective case studies and may contain incomplete data, pending source checks, or interpretation limits. Users are responsible for verifying sources, assumptions, and conclusions independently.
