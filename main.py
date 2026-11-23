#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the melting face,
chosen as the warmest single emoji for a stranger's glance.

Why this emoji: a smiling face that is melting with warmth. It is
warm and friendly at first glance, gently funny, understood by any
stranger of any age or background, plainly chosen rather than the
first default smiley, and right coming from someone unknown — a
small, wordless gift of warmth, with no intimacy, sarcasm or
flirtation in it. The output is exactly one Unicode code point
(4 bytes in UTF-8), so the entry file holds nothing but the emoji.
"""

import os
import sys

EMOJI = "\U0001fae0"  # 🫠 Melting Face


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: exactly one character, valid UTF-8, not whitespace.
    data = open(path, "rb").read()
    text = data.decode("utf-8")
    assert len(text) == 1 and text.strip(), "entry must be exactly one emoji"
    return 0


if __name__ == "__main__":
    sys.exit(main())
