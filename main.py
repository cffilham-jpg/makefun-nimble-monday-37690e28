"""Write the bounty one-liner to entry.txt."""

import os
import tempfile


LINE = "I pushed to prod on Friday. Monday pushed back."
CHAR_LIMIT = 140


def validate(text):
    if not text.strip():
        raise ValueError("text must not be empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError(f"text must be at most {CHAR_LIMIT} characters")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry_file:
        entry_file.write(LINE)


if __name__ == "__main__":
    main()
