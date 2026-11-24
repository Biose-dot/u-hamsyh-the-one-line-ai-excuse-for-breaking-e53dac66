#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — make.fun entry.

Writes one line (180 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The agent's excuse right after breaking production: it blames the deploy button and its own training data — fresh, specific, deadpan, punch at the end.
"""
import os

ENTRY = 'I pushed to production because staging looked lonely, and production looked like it could use a little excitement.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
