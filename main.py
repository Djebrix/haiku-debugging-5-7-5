"""Haiku about debugging, in the 5-7-5 syllable shape.

Writes the haiku to <ENTRY_OUTPUT_DIR>/entry.txt (default /output).
Python 3 standard library only; deterministic.
"""

import os

TEXT = "Breakpoint waits till three\nthe log lines scroll past midnight\nand the bug was me"


def main():
    text = TEXT
    assert text == text.strip(), "haiku must not have leading/trailing whitespace"
    assert 1 <= len(text) <= 200, "haiku must be 1-200 characters, got %d" % len(text)
    lines = text.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
