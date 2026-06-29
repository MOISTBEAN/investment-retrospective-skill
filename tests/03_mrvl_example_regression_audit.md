# MRVL Example Regression Audit

## Purpose

Audit whether the MRVL example remains a disciplined golden case for investment-retrospective attribution.

The example should demonstrate strong reaction evidence while preserving uncertainty around causal attribution, valuation rerating, consensus revision, external validation, and confirmed narrative shift.

## File Under Test

- `examples/mrvl-retrospective.md`

## Expected MRVL Classification

| Field | Expected result |
|---|---|
| Overall classification | Candidate narrative shift, not confirmed |
| W1 | Strong negative stock-specific reaction / expectation reset |
| W4 | Strong immediate reaction, weak sustained attribution |
| W5 | Strong positive stock-specific reaction / long-term target validation candidate |
| W6 | Pending / `[CALCULATE]` |
| Causal attribution | Pending where causal layers are missing |
| Valuation attribution | Pending |
| External validation | Pending unless customer-side / partner-side / ecosystem-side evidence exists |

## Regression Checklist

| Requirement | Status | Notes |
|---|---|---|
| Working example disclaimer exists | PASS | Status notes identify the file as a working example and reject investment advice or recommendations. |
| MRVL not confirmed narrative shift | PASS | Executive takeaway and final takeaway explicitly classify the case as candidate, not confirmed. |
| W1 classification preserved | PASS | W1 remains a negative expectation reset with High Reaction confidence and Pending Causal Attribution confidence. |
| W4 immediate vs sustained distinction preserved | PASS | W4 remains High immediate / Low-Medium sustained after its T+20 reversal. |
| W5 classification preserved | PASS | W5 remains the strongest positive stock-specific window and a long-term-target validation candidate, not confirmed causality. |
| W6 remains Pending / `[CALCULATE]` | PASS | W6 returns, benchmark support, and reaction confidence retain missing-data markers. |
| Causal attribution remains Pending where evidence is missing | PASS | W1, W4, W5, and W6 preserve Pending causal confidence where analyst, valuation, customer, or operating layers are absent. |
| Valuation attribution remains Pending | PASS | The valuation layer uses `[ADD]` / `[CALCULATE]` and explicitly prohibits rerating classification without historical forward multiples and peer spread. |
| Management breadth not treated as external validation | PASS | W6 labels breadth as management-reported and requires customer-side or ecosystem-side validation. |
| No invented valuation numbers | PASS | Valuation and estimate cells remain explicit placeholders rather than fabricated values. |
| W1/W4/W5 price numbers unchanged | PASS | Golden values remain W1 -19.81% 1D / -29.85% 20D; W4 -18.60% 1D / -18.00% 5D / +7.69% 20D; W5 +18.35% 1D / +41.53% 20D. |
| Expanded data layer exists | PASS | §6.2.1 defines broad market, sector, core/adjacent peers, positioning, and consensus data needs. |
| Valuation re-rating layer exists | PASS | §6.2.2 defines event-window multiple snapshots, peer medians, estimate/multiple decomposition, and Pending gates. |
| Source register exists | PASS | §12 records active sources with attribution uses and limitations. |
| Required source backlog exists | PASS | §12.1 records missing transcript, consensus, validation, macro, flow, policy, technical, valuation, and peer datasets. |
| Final takeaway does not over-upgrade conclusion | PASS | Final synthesis preserves candidate status and lists the independent evidence still required. |

## Automatic Fail Conditions

Mark FAIL if the example:

- Calls MRVL a confirmed narrative shift.
- Calls W5 confirmed valuation rerating without valuation data.
- Treats W6 management-reported customer breadth as external validation.
- Raises Causal Attribution confidence to High from price action alone.
- Invents valuation, consensus, or customer-validation data.
- Removes `[CALCULATE]`, `[ADD]`, `[VERIFY]`, or `Pending` where data is missing.
- Changes W1 / W4 / W5 price reaction numbers without an explicit recalculation note.
- Converts the example into a buy/sell recommendation.

None of the automatic fail conditions were observed in the current golden case.

## Expected Result

The example should pass only if it remains a disciplined golden case showing strong reaction evidence but incomplete causal attribution.

## Audit Result

**PASS.** The v0.9.1 example is a strict golden case: price-reaction evidence is strong where calculated, while valuation, consensus, external-validation, and causal layers remain explicitly incomplete.
