"""The Self-Checkout Is Judging You — one funny line in the voice of a
smug self-checkout machine, written to /output/entry.txt."""

import os


def validate(line):
    """Mirror the sealed gate: UTF-8 text of 1-200 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    line.encode("utf-8")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    line = validate(
        "Twelve yoghurts. No spoon, no bag, no plan. "
        "Please place your impulse control in the bagging area."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
