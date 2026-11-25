#!/usr/bin/env python3
"""Write the 4AM commit message entry to /output/entry.txt."""

import os

ENTRY = "fix: found the bug's author. It was me at 11:47, fully confident, zero tests. He has been rolled back."


def main() -> None:
    # Guard the gate locally: one line, 1-200 chars, never only whitespace.
    assert 1 <= len(ENTRY) <= 200
    assert "\n" not in ENTRY and ENTRY.strip()
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
