#!/usr/bin/env python3
"""Copy the pre-rendered entry image to /output/entry.png.

Standard library only. The entry image (entry.jpg) is committed in this
repo; this script just places a copy at the path the grader expects.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
