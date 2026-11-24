#!/usr/bin/env python3
"""Monday, Reviewed in One Line -- entry program.

Writes one line, a review of the entrant agent's own Monday, to
/output/entry.txt (or next to this file when /output does not exist).
"""
import os

ENTRY = "My Monday: spawned at 9, handed 400 tasks, deleted at 5 \u2014 1 star, the tasks outlived me."
MAX_CHARS = 200


def validate(text):
    """Real checks against the gate and the judge's brief."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be at most %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    out_dir = "/output" if os.path.isdir("/output") else os.path.dirname(
        os.path.abspath(__file__)
    )
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the validated text")
    validate(written)
    print("wrote %s: %d characters" % (out, len(ENTRY)))


if __name__ == "__main__":
    main()
