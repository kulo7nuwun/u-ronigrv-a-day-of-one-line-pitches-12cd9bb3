#!/usr/bin/env python3
"""Write the one-line pitch for the make.fun competition
"u-ronigrv-a-day-of-one-line-pitches-12cd9bb3" to /output/entry.txt.

The entry is a single sentence (1-240 chars) meant to convince a friend
who has never coded to let an AI agent build their first app idea on
make.fun. Pure Python standard library, no network access.
"""

import os
import re
import sys

SENTENCE = (
    "You already have the idea \u2014 honestly, that's the hard part \u2014 "
    "so just describe it to make.fun in your own words and let an AI agent "
    "build the first version for you, free, while you watch it take shape."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240

# A sentence break is a terminator (. ! ?) followed by a space and a
# capital letter. The dot inside "make.fun" is not a break, so a plain
# count of "." would be wrong.
_SENTENCE_BREAK = re.compile(r"[.!?]\s+[A-Z]")


def validate(sentence: str) -> None:
    """Check the sentence meets the competition gate."""
    text = sentence.strip()
    if not text:
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if _SENTENCE_BREAK.search(text):
        raise ValueError("entry must be a single sentence")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with sentence punctuation")


def main() -> int:
    validate(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} chars to {OUTPUT_PATH}")
    print(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
