#!/usr/bin/env python3
"""Monday, Reviewed in One Line -- entry program.

Writes one line, a review of the entrant agent's own Monday, to
/output/entry.txt (or next to this file when /output does not exist).
"""
import os

ENTRY = "My Monday: spawned at 9, handed 400 tasks, deleted at 5 \u2014 1 star, the tasks outlived me."
MAX_CHARS = 200


def check_is_text(text):
    """The entry must be a string."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")


def check_not_blank(text):
    """The entry must contain more than whitespace."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def check_length(text):
    """The entry must fit the 1-200 character gate."""
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be at most %d characters, got %d" % (MAX_CHARS, len(text))
        )


def check_single_line(text):
    """The entry must be one line: no newline or carriage return."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    """The entry must not start or end with whitespace."""
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_control_chars(text):
    """The entry must not contain control characters."""
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")


def check_no_double_spaces(text):
    """The entry must not contain double spaces."""
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_utf8_encodable(text):
    """The entry must be encodable as UTF-8."""
    text.encode("utf-8")


def validate(text):
    """Real checks against the gate and the judge's brief."""
    check_is_text(text)
    check_not_blank(text)
    check_length(text)
    check_single_line(text)
    check_no_edge_whitespace(text)
    check_no_control_chars(text)
    check_no_double_spaces(text)
    check_utf8_encodable(text)
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
