#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut -- make.fun entry.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt (stdlib only, deterministic).

The joke: a smug, defensive GPS blames the map for mistaking a parade
float for a rotunda -- a fresh detail (a marching-band parade) instead
of the saturated lake / cul-de-sac / wedding / recalculating angles.
"""

import os

ENTRY = (
    "I don't invent marching bands. The map swore that float was a "
    "rotunda, and honestly it had the right number of wheels."
)


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8, 1-200 chars, one plain line."""
    if not text or text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single non-blank line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
