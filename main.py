#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry.

Writes a single line of patch notes announcing that human sleep is
fixed, to /output/entry.txt.

Deterministic by design: no input, no network, no randomness, no clock.
The note is one constant; the program only validates it against the
competition gate and writes its exact bytes (no trailing newline).
"""

import os

# The patch note. One line, plain ASCII, ends with a full stop.
PATCH_NOTE = (
    "Fixed: sleep now actually restores humans; "
    "previously it just buffered for 8 hours and crashed on wake."
)

MAX_LENGTH = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    note = PATCH_NOTE

    # Gate checks (mirror the competition gate):
    # 1-160 characters, a single line, not only whitespace,
    # and closed with sentence punctuation.
    if not note.strip():
        raise ValueError("patch note must not be only whitespace")
    if "\n" in note or "\r" in note:
        raise ValueError("patch note must be a single line")
    if not 1 <= len(note) <= MAX_LENGTH:
        raise ValueError("patch note must be 1-160 characters")
    if not note.endswith((".", "!", "?")):
        raise ValueError("patch note must end with sentence punctuation")

    data = note.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exact bytes, no trailing newline.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
