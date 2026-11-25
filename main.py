#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes to /output/entry.txt.

The note is a fixed, deterministic constant: no input, no network,
no randomness and no clock are involved, so every run produces the
exact same bytes. The output file is written without a trailing
newline, because the gate counts characters and the entry must be a
single line of 1-160 characters, not only whitespace.
"""

import os
import sys

# The patch note itself, exactly as it must appear in /output/entry.txt.
PATCH_NOTE = (
    "Fixed: sleep now actually restores humans; "
    "previously it just buffered for 8 hours and crashed on wake."
)

OUTPUT_PATH = "/output/entry.txt"

# A patch note is a sentence, so it must end with sentence punctuation.
SENTENCE_ENDINGS = (".", "!", "?")


# Gate limits from the competition rules, kept next to the validation
# that enforces them so a future cap change only touches one place.
MAX_LENGTH = 160
MIN_LENGTH = 1


def validate(note):
    """Check `note` against the gate; return a list of problems found.

    An empty list means the note passes every check.
    """
    problems = []

    if not note:
        problems.append("note is empty")
    if len(note) < MIN_LENGTH:
        problems.append("note is shorter than %d character(s)" % MIN_LENGTH)
    if len(note) > MAX_LENGTH:
        problems.append(
            "note is %d characters, over the %d limit" % (len(note), MAX_LENGTH)
        )
    if note.strip() == "":
        problems.append("note is only whitespace")
    if "\n" in note or "\r" in note:
        problems.append("note must be a single line")
    if note and not note.endswith(SENTENCE_ENDINGS):
        problems.append("note does not end with sentence punctuation")

    return problems


def main():
    problems = validate(PATCH_NOTE)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the exact bytes, with no trailing newline appended.
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(PATCH_NOTE.encode("utf-8"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
