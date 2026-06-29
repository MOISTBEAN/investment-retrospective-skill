#!/usr/bin/env python3
"""Lightweight structural phrase checks for retrospective Markdown files.

Manual review remains authoritative. This helper performs no network access and
does not modify files.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


SKILL_REQUIRED = (
    "price anomaly",
    "benchmark",
    "Fact confidence",
    "Reaction confidence",
    "Causal attribution confidence",
    "valuation",
    "source register",
    "Pending",
)

MRVL_REQUIRED = (
    "candidate narrative shift",
    "not a confirmed narrative shift",
    "W1",
    "W4",
    "W5",
    "W6",
    "Valuation Re-rating Layer",
    "Source Register",
    "Required Source Backlog",
)


def required_phrases(path: Path) -> tuple[str, ...] | None:
    if path.name == "SKILL.md":
        return SKILL_REQUIRED
    if path.name == "mrvl-retrospective.md":
        return MRVL_REQUIRED
    return None


def validate(path: Path) -> bool:
    if not path.is_file():
        print(f"FAIL {path}: file not found")
        return False

    profile = required_phrases(path)
    if profile is None:
        print(f"WARN {path}: no validation profile; file is readable")
        return True

    text = path.read_text(encoding="utf-8")
    folded = text.casefold()
    missing = [phrase for phrase in profile if phrase.casefold() not in folded]

    if missing:
        for phrase in missing:
            print(f"FAIL {path}: missing required phrase: {phrase}")
        return False

    print(f"PASS {path}: {len(profile)} required phrases found")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check required phrases in SKILL.md and the MRVL example."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files to check")
    args = parser.parse_args()

    results = [validate(path) for path in args.paths]
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
