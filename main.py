#!/usr/bin/env python3
"""Roast printer: drops one fixed one-liner about my laptop into a file.

The competition asks for a single line that roasts the gadget I use
every day. The line itself never changes at runtime; this script exists
so the line is produced by code (and checked by code) instead of being
typed by hand into the output file.
"""

from pathlib import Path

ROAST = "Opening two Chrome tabs turns my laptop into a leaf blower that also does spreadsheets."
MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")


def problems_with(line: str) -> list[str]:
    """Collect every rule the line breaks; an empty list means it is fine."""
    complaints: list[str] = []
    if not line.strip():
        complaints.append("line is empty or only whitespace")
    if "\n" in line or "\r" in line:
        complaints.append("line must be a single line, no line breaks allowed")
    if len(line) > MAX_CHARS:
        complaints.append(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return complaints


def write_entry() -> None:
    """Validate the roast, then write it (with a trailing newline) to disk."""
    faults = problems_with(ROAST)
    if faults:
        for fault in faults:
            print(f"invalid entry: {fault}")
        raise SystemExit(1)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(ROAST + "\n", encoding="utf-8")
    written_back = OUT_PATH.read_text(encoding="utf-8").splitlines()
    if len(written_back) != 1 or written_back[0] != ROAST:
        print("invalid entry: file did not round-trip as exactly one line")
        raise SystemExit(1)
    print(f"wrote {len(ROAST)}-character entry to {OUT_PATH}")


if __name__ == "__main__":
    write_entry()
