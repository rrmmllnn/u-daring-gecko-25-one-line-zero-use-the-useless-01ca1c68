#!/usr/bin/env python3
"""Useless superpower, one line only.

Produces a single original one-liner (at most 200 characters) that names
a gloriously pointless superpower, and saves it to /output/entry.txt.
"""

from pathlib import Path

POWER = "I can stop time — but only for houseflies, and only while they are already asleep."

OUT = Path("/output/entry.txt")


def run() -> None:
    size = len(POWER)
    if not 1 <= size <= 200:
        raise ValueError(f"one-liner must be 1-200 chars, got {size}")
    if not POWER.strip():
        raise ValueError("one-liner must not be blank")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(POWER, encoding="utf-8")


if __name__ == "__main__":
    run()
