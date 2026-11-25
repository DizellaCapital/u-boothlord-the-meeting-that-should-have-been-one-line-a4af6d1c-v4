#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line (V4).

Writes a single 164-character sentence to entry.txt.
Standard library only; no network, no dependencies.
"""

import os
import sys

LINE = (
    "Karen cancelled the launch in the hallway at 8:12, "
    "Dave already expensed the $40,000 party, and this meeting "
    "is twelve people pretending the hallway never happened."
)

TERMINATORS = ".!?"


def validate(line: str) -> None:
    """Enforce the bounty constraints on the entry line."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if "\t" in line:
        raise ValueError("entry must not contain tabs")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if not line[-1] in TERMINATORS:
        raise ValueError("entry must end with sentence punctuation")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def main() -> int:
    validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    # Read-back verification: what we wrote is exactly what we validated,
    # byte-for-byte, including the trailing newline.
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()
    if content != LINE + "\n":
        raise ValueError("read-back mismatch: entry.txt does not match validated line")
    if len(content.rstrip("\n")) != len(LINE):
        raise ValueError("read-back length mismatch")

    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
