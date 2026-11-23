#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes exactly one line (max 200 characters) roasting the gadget
used every day, to /output/entry.txt. Validates the constraint and
exits 1 if violated.
"""

import os
import sys

ENTRY = "Opening two Chrome tabs turns my laptop into a leaf blower that also does spreadsheets."

MAX_CHARS = 200


def main() -> int:
    # Validate the entry BEFORE writing anything.
    # Check 1 of 3: the entry must contain visible text.
    if not ENTRY.strip():
        print("FAIL: entry is empty or whitespace-only (check 1 of 3)", file=sys.stderr)
        return 1
    # Exactly one line: no newline characters inside the entry.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry contains more than one line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"FAIL: entry is {len(ENTRY)} chars, exceeds {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    os.makedirs("/output", exist_ok=True)
    written = ENTRY + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(written)

    # Validate the exact string written (ENTRY + "\n", one byte longer).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        content = f.read()
    if content != written:
        print("FAIL: /output/entry.txt does not match the entry", file=sys.stderr)
        return 1
    if content.count("\n") != 1 or len(content) > MAX_CHARS + 1:
        print("FAIL: written file violates the 1-line / 200-char constraint", file=sys.stderr)
        return 1

    print(f"OK: wrote /output/entry.txt ({len(ENTRY)} chars, 1 line)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
