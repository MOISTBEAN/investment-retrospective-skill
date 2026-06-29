# Supporting Docs Smoke Audit

## Purpose

Smoke-test the supporting documentation without requiring production-level completeness.

These documents are allowed to be minimum operated. They should not fail merely because they are short. They should fail only if they contradict the core skill, omit a hard gate they are responsible for, or create attribution risk.

## Files Under Test

- `README.md`
- `templates/retrospective-report.md`
- `checklists/market-fear-checklist.md`
- `checklists/source-quality-checklist.md`
- `checklists/true-signal-vs-noise.md`

## Maturity-Aware Scoring

| Score | Meaning |
|---|---|
| PASS | Sufficient for current MVP and consistent with the skill. |
| WARN | Thin, incomplete, or could be improved, but not misleading. |
| FAIL | Contradicts the skill, omits a required hard gate, or may cause false attribution. |

## Smoke Checklist

| Document | Requirement | Status | Notes |
|---|---|---|---|
| README | Explains purpose as retrospective attribution, not investment advice | PASS | Clearly frames retrospective learning and rejects recommendations, forecasting, and false certainty. |
| README | Explains MRVL as example / golden case, not the whole skill | PASS | Repository structure describes MRVL as a demonstration; the framework remains ticker-neutral. |
| README | Starts price anomaly before narrative construction | PASS | Core workflow now orders price anomaly detection, event-window definition, benchmark comparison, driver/finding classification, and scoring before narrative-shift classification and story synthesis. |
| Template | Preserves required output structure | PASS | It now includes Event Window Map, Claim Ledger, Price Reaction & Relative Return Map, Benchmark Layers, Expanded Data Layer, Valuation Re-rating Layer, Candidate Driver Attribution Matrix, Attribution Scoring Rubric, Source Register, and Required Source Backlog. |
| Template | Adds a first-read finding layer without bypassing scoring | PASS | The First-read Finding Card is generated only after scoring and classification, preserves qualifications and `Pending`, and cannot add or upgrade claims, scores, confidence, or narrative-shift level. |
| Template | Includes Fact / Reaction / Causal Attribution confidence | PASS | The three labels are separately defined and carried through timeline, claim, reaction, narrative, attribution, signal, and lesson structures. |
| Template | Keeps story after scoring | PASS | Attribution scoring precedes the Narrative Shift Map, and the final takeaway follows the evidence and attribution sections. |
| Market Fear | Requires pre-event fear / assumption mapping | PASS | Minimum evidence gate and core questions tie the fear to contemporaneous operating or valuation assumptions. |
| Market Fear | Separates evidence from counter-evidence | PASS | Counter-evidence and resolution status are explicit required outputs. |
| Source Quality | Distinguishes source tiers | PASS | Defines Tiers 1–5 with allowed uses, limitations, and attribution weights. |
| Source Quality | Does not allow rumors as factual validation | PASS | Tier 5 may provide sentiment context only and cannot anchor factual claims. |
| Source Quality | Does not treat management commentary as external validation | PASS | Management commentary establishes company framing but is insufficient alone for market causality or external validation. |
| True Signal vs Noise | Distinguishes stronger signals from noisy signals | PASS | Mandatory gates and classification guide distinguish true, possible, noisy, and uncertain signals. |
| True Signal vs Noise | Flags one-day spikes, generic headlines, and management optimism as possible false positives | PASS | It explicitly flags one-day reactions, generic headlines and broad news-cycle excitement, management optimism, sector beta, and low-quality sources. |

## Automatic Fail Conditions

Mark FAIL if any supporting doc:

- Encourages starting from narrative before price anomaly.
- Treats price action as causal proof.
- Treats management commentary as external validation.
- Treats social media rumors as verified facts.
- Labels valuation rerating without valuation data.
- Removes the need for source register or source limitations.
- Forces every abnormal price move into narrative shift.
- Uses MRVL-specific industry logic as universal logic.
- Allows the First-read Finding Card to create or upgrade a finding before scoring.

No supporting document currently triggers an automatic fail condition.

## WARN Conditions

Mark WARN, not FAIL, if a document is:

- Short but consistent.
- Missing detail but not misleading.
- MVP-level but aligned with the skill.
- Clear enough for now but worth expanding later.

No current supporting-doc row requires WARN. Retain WARN for future thin-but-aligned MVP documentation rather than treating incompleteness alone as failure.

## Expected Result

Supporting docs may contain WARN items. That is acceptable for the current stage.

The smoke audit fails only if supporting docs create real attribution risk.

## Audit Result

**PASS.** The README, template, and checklists are aligned with the anomaly-first core contract. No FAIL or WARN rows remain.
