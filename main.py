"""Angry Judge: The Short Rant Contest entry.

Writes exactly one short, funny rant (<= 400 characters) about a small
everyday annoyance to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Standard library only.
"""

import os

RANT = (
    "My printer has one job. ONE. It sits there all week doing nothing, "
    "then the second I need a boarding pass it flashes 'low ink' like a "
    "dying patient and demands a firmware update. I bought ink last month. "
    "Where did it go? Did it drink it? Printers don't print documents. "
    "They print excuses — and then charge you for the paper."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = RANT.strip()
    assert len(text) <= 400, f"rant is {len(text)} chars, over the 400 limit"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
