#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label (120 characters at most) to
/output/entry.txt. Pure standard library, deterministic.

The label is a straight-faced safety notice about the real
time-travel hazard of meeting your duplicate self, and it saves
the surprise — he has had more time to plan this — for the
last few words, where the laugh lands.
"""

from pathlib import Path

LABEL = (
    "WARNING: Do not meet yourself. He knows what you did, "
    "he is angrier than you, and he has had more time to plan this."
)


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 120, f"label is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
