"""Groan-Off entry: write one original one-line dad joke to /output/entry.txt."""

import os

JOKE = "I told my son his room was a pigsty. He said, 'Thanks \u2014 I was going for ham-bience.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
