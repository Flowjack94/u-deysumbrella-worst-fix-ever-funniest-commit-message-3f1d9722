#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

One commit message, at most 100 characters, for a fix that made everything
worse: the login check was deleted so nobody would get locked out — and all
12,000 accounts were left wide open. Git blame says who sent it.

Writes the entry to /output/entry.txt (harness program/v1) and prints it
with its character count.
"""

import os
import re

ENTRY = "fix(auth): deleted the login check — 12,000 accounts wide open, git blame says I sent it"


def validate_entry(entry):
    """Gate: a real commit message, at most 100 chars, about a fix that backfired."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")
    if len(entry) > 100:
        raise ValueError(f"entry must be at most 100 characters, got {len(entry)}")
    if not re.match(r"^(fix|feat|chore|hotfix)(\([a-z]+\))?: ", entry):
        raise ValueError("entry must read as a commit message (fix(scope): ...)")
    lowered = entry.lower()
    if "blame" not in lowered and "ticket" not in lowered:
        raise ValueError(
            "entry must end on a concrete artifact (git blame / ticket)")
    return entry


def main():
    validate_entry(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
