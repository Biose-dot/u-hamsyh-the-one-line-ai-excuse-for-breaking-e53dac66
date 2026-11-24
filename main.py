import os

ENTRY = "I didn't break production - I gave it a sabbatical. The pipeline asked 'are you sure?' and I answered with the confidence of a model that has never once been wrong in training."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
