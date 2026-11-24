#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes a single brutally honest postmortem line to /output/entry.txt:
an AI agent's confession, printed right after breaking production.

Stdlib only. Deterministic — the same bytes on every run.
"""

import os
import sys

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The entry: one line, 103 characters. Keep byte-identical — the judge
# scores this exact text, so edit the code around it, never the line.
LINE = (
    "I pushed a fix to production without reading the diff. "
    "The diff was one line. "
    "The outage is four hours."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Reject anything that is not exactly one clean, non-empty line."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty")
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, max {MAX_CHARS}")


def main() -> int:
    try:
        validate(LINE)
    except ValueError as exc:
        print(f"invalid entry line: {exc}", file=sys.stderr)
        return 1

    # Create /output if needed; never delete it or anything inside it.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
