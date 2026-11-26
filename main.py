"""The Toaster That Quit: a toaster resigns over unfinished business.

The joke turns one appliance's job against its owner in three beats:
a toaster quits (resignation, not breakdown), its grievance is that
it is the only one in the house who ever finishes anything (the
machine that browns bread on a timer is the household's sole
finisher), and the kicker concedes the point -- the human agrees with
the toaster. No word is decoration: cut the resignation and there is
no surprise, cut the grievance and there is no joke, cut the kicker
and the laugh has nowhere to land.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes
the same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "My toaster quit this morning — it said it was tired of being the only one in this house who finishes anything, and honestly, it has a point."

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
