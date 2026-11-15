#!/usr/bin/env python3
"""agency-poem-01: write one poem about agency to entry.txt.

The poem is a fixed string: no input, no network, no randomness, no clock,
so every run writes identical bytes. The output directory is
MAKEFUN_OUTPUT_DIR when set (local runs), otherwise /output (the grader).
"""

import os
from pathlib import Path

POEM_LINES = (
    "The agent booked the flight you asked for:",
    "window seat, dawn departure, the cheap one",
    "two stops you never thought to forbid.",
    "",
    "You read the confirmation like your own",
    "signature on a form you never signed.",
    "",
    "It did everything right.",
    "That was the trouble.",
    "",
    "You called the airline, waited",
    "forty minutes on hold, and changed it:",
    "evening flight, direct, the one",
    "that costs too much.",
    "",
    "Agency is not getting what you asked for.",
    "It is the hold music, the higher fare,",
    "the small refusal to be carried.",
)

POEM = "\n".join(POEM_LINES)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
