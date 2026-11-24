#!/usr/bin/env python3
"""Say What Actually Broke: one honest error line, no padding.

The joke is a confession every engineer recognises: the page died
because somebody shipped on a Friday, the rollback is already moving,
and the only thing asked of the user is a refresh plus a little
collective amnesia. Fixed text, no clock, no network, no randomness,
so the grader's two runs write byte-identical output.
"""

import os
import sys
from pathlib import Path

LINE = (
    "This page crashed because someone deployed on a Friday. "
    "We're rolling it back — refresh in a minute "
    "and pretend you saw nothing."
)
MAX_CHARS = 200


def problems(line):
    """Return a list of the ways a candidate line breaks the gate."""
    found = []
    if not line.strip():
        found.append("entry is blank")
    if "\n" in line or "\r" in line:
        found.append("entry must be a single line")
    if len(line) > MAX_CHARS:
        found.append(f"entry is {len(line)} chars, limit is {MAX_CHARS}")
    return found


def emit(line):
    """Write the line to the grader's output file, exactly as-is."""
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    return target


def main():
    bad = problems(LINE)
    if bad:
        for item in bad:
            print(f"error: {item}", file=sys.stderr)
        return 1
    emit(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
