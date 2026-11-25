"""Unsent — The Micro-Confession Sprint.

Writes a single unsent message to /output/entry.txt, byte-exact.
The message is a micro-confession: a note to a grandfather, never sent.

The entry is two lines joined by a single newline — an address line, then
the confession itself — with no trailing newline, so the file is exactly
99 bytes. The twist lands in the second line: the sender introduces
themself to their own grandfather as if they were strangers.
"""

import os

ENTRY = "To: my grandfather\nI knew you forgot my name at Christmas. I introduced myself like we'd never met."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
