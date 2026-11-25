"""One Star, Written in Sap — make.fun entry.

Writes one single-line, one-star review (under 280 characters) filed
by a houseplant against the human who owns it, to /output/entry.txt.

The plant's grievance is overwatering: its human drowns it daily out
of guilt, never out of love, then photographs it for social media
captioned "thriving". The single star is earned, not given lightly —
the plant is not thriving, it is drowning with excellent lighting.
The sting lands in the last four words.
"""

import os
import sys

REVIEW = (
    "One star. My human waters me every day out of guilt, never out "
    "of love, then photographs me captioned 'thriving.' I am not "
    "thriving. I am drowning with excellent lighting."
)

MAX_CHARS = 280


def resolve_output_dir() -> str:
    """Pick the output directory: the grader's env var first, then
    /output, then a local ./output fallback so the program also runs
    outside the sandbox without an env var set."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main() -> int:
    text = REVIEW.strip()
    if not text or len(text) > MAX_CHARS or text != text.strip():
        print(f"review fails gate: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("review must be a single line", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
