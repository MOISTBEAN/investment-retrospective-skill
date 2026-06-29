# Tests

This directory contains lightweight behavioral audits for `investment-retrospective-skill`.

These tests are not market-data tests and are not financial analysis.

The goal is to prevent attribution drift.

## Testing Philosophy

The repository uses maturity-aware testing.

- `SKILL.md` is the core contract and is tested strictly.
- `examples/mrvl-retrospective.md` is the golden case and is tested strictly.
- Supporting docs are currently minimum operated and are smoke-tested with PASS / WARN / FAIL.

Thin but consistent supporting docs should receive WARN, not FAIL.

A document should fail only if it contradicts the skill, removes a hard gate, or may cause false attribution.

## Test Files

- `01_skill_core_contract_audit.md`
- `02_supporting_docs_smoke_audit.md`
- `03_mrvl_example_regression_audit.md`

## Automatic Fail Examples

- Confirmed narrative shift from price action alone.
- Valuation rerating without valuation data.
- Management commentary treated as external validation.
- Rumor treated as fact.
- Missing-data placeholders removed without evidence.
- MRVL-specific logic applied as universal logic.

## Recommended Review Order

1. Run the skill core contract audit.
2. Run the supporting docs smoke audit.
3. Run the MRVL example regression audit.

If the skill core fails, fix `SKILL.md` before testing examples.

If the MRVL example fails, fix the example before adding new adversarial cases.

If supporting docs produce WARN items, document them but do not necessarily block release.

## Optional Structure Helper

`scripts/validate_structure.py` performs dependency-free phrase checks for the core skill and MRVL example. It is a helper only; manual review remains authoritative.

Run:

```bash
python3 scripts/validate_structure.py SKILL.md examples/mrvl-retrospective.md
```
