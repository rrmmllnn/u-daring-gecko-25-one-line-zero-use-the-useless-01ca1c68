#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (under 200 characters) naming a
hilariously useless superpower to /output/entry.txt.
"""

import os

LINE = (
    "I can talk to animals \u2014 but only goldfish, "
    "and they only ever want to discuss the same castle."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
