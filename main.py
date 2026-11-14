# Entry for make.fun food-picture-01 ("Make the best-looking food picture").
# This program writes the entry image: it copies the pre-made food
# photograph entry.png that sits beside this script to the output directory
# as entry.png. Standard library only, no network, deterministic output.
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("error: source image not found: " + source, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
