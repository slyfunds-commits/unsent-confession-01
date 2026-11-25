#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes the keeper — a two-part micro-confession — to /output/entry.txt.
Pure stdlib only. Deterministic: identical bytes on every run.
"""

import os

ENTRY = "To: my grandfather\nI knew you forgot my name at Christmas. I introduced myself like we'd never met."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two parts: To: line + message"
    assert lines[0].startswith("To: "), "first line must be the To: line"
    assert 1 <= len(lines[1]) <= 200, "message must be 1-200 chars"
    data = ENTRY.encode("utf-8")
    assert 1 <= len(data) <= 260, f"entry is {len(data)} bytes, gate is 1-260"
    assert data.decode("utf-8") == ENTRY, "UTF-8 round-trip failed"
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify byte-identical output.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "written bytes differ from entry"
    print(f"wrote {len(data)} bytes to {path}")

if __name__ == "__main__":
    main()
