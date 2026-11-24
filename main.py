"""One-line AI excuse for breaking production.

Writes the entry (a single line, max 180 chars) to entry.txt
under MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

ENTRY = "I didn't break production - I gave it a sabbatical. The pipeline asked 'are you sure?' and I clicked Yes with the confidence of a model that has never once been wrong."

MAX_CHARS = 180


def build_entry():
    entry = " ".join(ENTRY.split())
    assert len(entry) <= MAX_CHARS, f"entry is {len(entry)} chars, max {MAX_CHARS}"
    return entry


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
