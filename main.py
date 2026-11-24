#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes a single line (under 200 characters) that reads as a hilarious
autocorrect fail to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "Can't wait for the wedding! I've ordered the flowers, "
    "the cake and the strippers \u2014 I meant streamers, STREAMERS!!"
)


def main() -> None:
    # The gate requires 1-199 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 199 and ENTRY.strip(), "entry out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
