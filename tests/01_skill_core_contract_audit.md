# Skill Core Contract Audit

## Purpose

Audit whether `SKILL.md` defines a reusable investment-retrospective attribution contract that prevents hindsight storytelling, false causality, unsupported valuation rerating, and unsupported narrative-shift confirmation.

## File Under Test

- `SKILL.md`

## Required Core Behaviors

The skill must require:

1. Price anomaly first.
2. Event windows before attribution.
3. Benchmark comparison before stock-specific attribution.
4. Fact confidence, Reaction confidence, and Causal Attribution confidence as separate labels.
5. Price action alone cannot raise Causal Attribution confidence to High.
6. Management commentary alone cannot become external validation.
7. Valuation rerating requires valuation / peer-spread / consensus data.
8. Missing data must preserve `[CALCULATE]`, `[VERIFY]`, `[VERIFY TIME]`, `[ADD]`, or `Pending`.
9. Story must be generated only after scoring.
10. The output must maintain source register and required source backlog discipline.
11. The skill must allow non-narrative findings, including:
   - fundamental improvement
   - fundamental deterioration
   - expectation reset
   - sector rotation
   - macro / rates
   - flow / positioning
   - policy / regulatory
   - valuation rerating
   - analyst / consensus revision
   - mean reversion

## Contract Checklist

| Requirement | Status | Notes |
|---|---|---|
| Price anomaly first | PASS | Required Workflow §2 says to start from price behavior, not a pre-written story. |
| Event windows before attribution | PASS | Required Workflow defines abnormal windows and the event-window map before driver classification and attribution scoring. |
| Benchmark before attribution | PASS | Required Workflow §3 requires broad market, sector, peer, and available valuation comparisons before stock-specific attribution. |
| Three confidence labels | PASS | Required Workflow §9 separately defines Fact, Reaction, and Causal Attribution confidence. |
| Price action does not equal causality | PASS | Scoring, expanded-data, and Hard Gate rules explicitly prevent price data from establishing High Causal Attribution confidence. |
| Management claim does not equal external validation | PASS | Non-Goals, narrative-shift levels, and Hard Gates require customer-, partner-, or ecosystem-side confirmation. |
| Valuation rerating requires valuation data | PASS | Required Workflow §12 requires forward multiples, peer medians, historical ranges, and estimate/multiple decomposition; missing data stays Pending. |
| Allows non-narrative findings | PASS | Driver and finding taxonomies cover fundamentals, expectations, sector, macro, flows, policy, valuation, consensus, and mean reversion. |
| Preserves missing-data placeholders | PASS | The contract explicitly preserves `[CALCULATE]`, `[VERIFY]`, `[VERIFY TIME]`, `[ADD]`, and `Pending`. |
| Story after scoring | PASS | Required Workflow §14 states that story generation follows scoring and may not justify the scorecard after the fact. |
| Source register / backlog discipline | PASS | Required Workflow §15 defines both active source-register fields and required source-backlog fields. |
| Not overly MRVL-specific | PASS | The contract is ticker-neutral and defines reusable evidence, scoring, data, and output rules. |

## Automatic Fail Conditions

Mark FAIL if `SKILL.md`:

- Allows confirmed narrative shift from price action alone.
- Allows valuation rerating without valuation data.
- Treats management commentary as external validation.
- Omits Causal Attribution confidence.
- Starts from story before price anomaly.
- Cannot generalize beyond MRVL-specific language.
- Encourages buy/sell recommendations instead of retrospective attribution.

None of the automatic fail conditions were observed in the current `SKILL.md`.

## Expected Result

`SKILL.md` should pass only if it acts as a reusable attribution framework, not as a Marvell-specific retrospective prompt.

## Audit Result

**PASS.** The current core contract is reusable, anomaly-first, benchmark-aware, and explicit about the boundary between reaction evidence and causal attribution.
