#!/usr/bin/env python3
"""Write one nostalgic childhood-memory line to /output/entry.txt.

Entry for make.fun bounty u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363:
"Make the AI Judge Feel Nostalgic: A Childhood Memory".
Python 3.13, no network.
"""

import os

ENTRY = (
    "The rice pot hissed on Grandma's stove while she scraped the burnt "
    "crust into my bowl like it was a secret, and thirty years on I still "
    "check the bottom of every pot, hoping she hid one there for me."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
