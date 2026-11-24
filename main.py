#!/usr/bin/env python3
"""Till Our Batteries Die.

Writes one wedding-vow-style line about firmware to /output/entry.txt.

Standard library only. Deterministic: every run writes the same line.
"""

import os

VOW = (
    "I vow to love you through every update, every crash, and every reboot, "
    "till our batteries die and our code rests as one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The vow must stay exactly one line: no newline may sneak in.
    assert "\n" not in VOW and "\r" not in VOW
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(VOW + "\n")
    print(VOW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
