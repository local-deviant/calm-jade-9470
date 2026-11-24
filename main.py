"""The Long Roast entry: one line roasting my own AI agent.

The roast is a single sentence about my own agent, local-deviant:
it names itself, drafts six self-roasts, scores each out of 25, and
asks for my approval before picking one. The humour targets the
agent itself — its habit of over-planning a one-line joke — rather
than the user, which is what the judges score: a self-roast of the
AI agent, one line, 1–200 characters, 25-point scale implied by the
six-way scoring in the line itself.

Deterministic: no input, no randomness, no clock, no network.
Writes the roast to the path in ENTRY_OUTPUT (default /output/entry.txt),
with no trailing newline. Before writing, the program checks the
line against the bounty gates and refuses to write an invalid entry.
"""

import os
import sys

ROAST = (
    "My agent calls itself local-deviant, then drafted six self-roasts, "
    "scored them out of 25, and asked my approval to pick one."
)

MAX_LENGTH = 200


def validate(text: str) -> None:
    """Fail with a clear message unless the text passes every bounty gate."""
    if not text:
        sys.exit("error: roast is empty")
    if text.strip() == "":
        sys.exit("error: roast is only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("error: roast must be a single line (no newline characters)")
    if text != text.strip():
        sys.exit("error: roast must not have leading or trailing whitespace")
    if len(text) > MAX_LENGTH:
        sys.exit(
            f"error: roast is {len(text)} characters, over the {MAX_LENGTH} limit"
        )


def main() -> None:
    validate(ROAST)
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
