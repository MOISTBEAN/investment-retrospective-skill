# Investment Retrospective Skill

## What this is

Investment Retrospective Skill is a Skill-style framework for studying past investment cases. It maps events, market fears, narrative shifts, price reactions, and lessons into reusable future watchlist rules.

The framework is designed for retrospective learning. It is not a stock recommendation system, trading bot, forecasting model, or substitute for professional financial advice.

## Why this exists

Investors often examine a stock only after it has already re-rated. The tempting explanation—“the market finally understood”—usually hides the useful work. A disciplined retrospective asks:

- What was the original market fear?
- Which events challenged or confirmed that fear?
- When did the narrative shift?
- Did price action support a stock-specific re-rating?
- Which signals were real, and which were noise?
- What future rules can be extracted without pretending the past was obvious?

The aim is to reconstruct what was knowable at each point in time, distinguish evidence from interpretation, and learn without converting hindsight into false certainty.

## Core workflow

1. Price anomaly detection
2. Event window definition
3. Benchmark comparison
4. Claim ledger
5. Candidate driver classification
6. Finding type classification
7. Attribution scoring
8. Fact / Reaction / Causal Attribution confidence
9. Narrative shift classification
10. Story synthesis after scoring
11. Source register and source backlog

## Current status

- Core contract audit: PASS
- Supporting docs audit: PASS
- MRVL regression audit: PASS
- Overall suite: PASS

## How to use

1. Start with an abnormal stock move.
2. Define the event windows and effective trading dates.
3. Benchmark the move against market, sector, and peers.
4. Map claims to dated sources and limitations.
5. Score candidate drivers and finding types.
6. Assign Fact, Reaction, and Causal Attribution confidence separately.
7. Generate the story only after scoring.
8. Preserve `Pending`, `[CALCULATE]`, `[VERIFY]`, `[VERIFY TIME]`, or `[ADD]` where evidence is missing.

**Scope warning:** This is not investment advice or a buy/sell recommendation tool. MRVL is the golden example, not the whole skill.

## What the Skill produces

The output is a structured retrospective report containing:

- Original market fear
- Key event timeline
- Event classification
- Price reaction map
- Narrative shift map
- Attribution hypotheses
- True signal versus noise assessment
- Lessons learned
- Future watchlist rules

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
└── examples/
    └── mrvl-retrospective.md
```

- `SKILL.md` contains the operating instructions and evidence discipline for an AI analyst.
- `templates/retrospective-report.md` is the reusable report structure.
- `checklists/market-fear-checklist.md` helps reconstruct the concern embedded in the old narrative.
- `checklists/true-signal-vs-noise.md` tests whether an apparent inflection was knowable and material.
- `checklists/source-quality-checklist.md` defines source tiers, claim types, evidence grades, and permitted uses.
- `examples/mrvl-retrospective.md` demonstrates the method with intentionally unverified placeholders.

## Recommended first use

Start with one stock, one clearly bounded 12–24 month period, and a small set of manually provided materials. Prefer filings, earnings materials, official customer or regulator statements, reputable reporting, and dated market data. Complete one careful report before attempting automation or expanding the universe.

## Guardrails

- Do not fabricate events, dates, sources, quotes, financial data, customer names, or price moves.
- Do not treat price movement alone as proof of causality.
- Always include plausible alternative explanations for major moves.
- Always separate fact, management claim, market reaction, inference, and attribution hypothesis.
- Always mark evidence strength and confidence.
- Preserve the information set available at the time to reduce hindsight bias.
- Use this framework for research education, not financial advice.

## Roadmap

- **v0.1:** Markdown Skill framework and MRVL example
- **v0.2:** More examples such as ASTS and FLNC
- **v0.3:** JSON schemas for structured events
- **v0.4:** Optional Python CLI for CSV timeline and price reaction mapping
- **v1.0:** Semi-automated retrospective engine
