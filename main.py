#!/usr/bin/env python3
"""Entry program for The Worst App Idea Ever Pitched.

Writes one pitch sentence (at most 240 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: Napkin, a subscription app that sends you one photo
of a napkin daily. Premium unlocks the same napkin, in
landscape.
"""

import os

LINE = (
    "Meet Queue: wait in a virtual line to be told the "
    "thing you queued for is available instantly "
    "elsewhere; the Pro tier waits longer."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
