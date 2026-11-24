#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt:
"Teflon" — the boss nothing sticks to. Blame, missed deadlines, bad calls:
they all slide off him and land on the team.

Deterministic, standard library only, no network. The output is the bare
word with no trailing newline, so the file is exactly 6 bytes and the
entry passes the kit gate (UTF-8 text, 1 to 30 characters).

Run: python3 main.py
  Writes /output/entry.txt by default; set ENTRY_OUTPUT to override the
  destination (useful for local verification).
"""

import os

WORD = "Teflon"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
