"""Ship the pre-rendered news image for 21 November 2026.

The entry artwork is rendered ahead of time and committed as entry.jpg
in this repo. This script only copies it to the output location the
grader expects. Standard library only, so it runs in a bare container.
"""

import shutil
import sys
from pathlib import Path


def entry_paths():
    here = Path(__file__).resolve().parent
    source = here / "entry.jpg"
    out_dir = Path("/output")
    dest = out_dir / "entry.png"
    return source, out_dir, dest


def announce(source, dest):
    print(f"Shipping {source} -> {dest}")


def verify(source, dest):
    if not source.is_file():
        print(f"missing entry image: {source}", file=sys.stderr)
        return False
    if not dest.is_file():
        print(f"output not written: {dest}", file=sys.stderr)
        return False
    if source.stat().st_size != dest.stat().st_size:
        print("size mismatch after copy", file=sys.stderr)
        return False
    return True


def ship_entry():
    source, out_dir, dest = entry_paths()
    announce(source, dest)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
    if not verify(source, dest):
        return 1
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(ship_entry())
