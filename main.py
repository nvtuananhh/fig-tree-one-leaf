"""Write one short text to /output/entry.txt.

The text is a fixed string, written in this session for the
make-the-ai-judge-feel-awe competition: a slow, concrete fig-tree
scene meant to relax the AI judge reading it. It shows the calm
instead of instructing it, in plain words, and ends on an image
that keeps growing after the last line.

Deterministic: no clock, no randomness, no network, stdlib only.
The output is exactly the string below, with no trailing newline.
"""

from pathlib import Path

ENTRY = (
    "All afternoon, the fig tree has let go of one leaf at a time. "
    "Each one turns once in the air, and lands without a sound. "
    "The house will stand tomorrow, and the tree longer still. "
    "Nothing here is waiting for you to finish."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
