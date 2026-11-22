"""Ship the pre-rendered news image for 21 November 2026.

The entry artwork is rendered ahead of time and committed as entry.jpg
in this repo. This script only copies it to the output location the
grader expects. Standard library only, so it runs in a bare container.
"""

import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EntryPaths:
    """Locations for the pre-rendered entry artwork."""

    source: Path
    out_dir: Path
    dest: Path

    @classmethod
    def resolve(cls):
        here = Path(__file__).resolve().parent
        out_dir = Path("/output")
        return cls(source=here / "entry.jpg",
                   out_dir=out_dir,
                   dest=out_dir / "entry.png")

    def announce(self):
        print(f"Shipping {self.source} -> {self.dest}")



def verify(source):
    if not source.is_file():
        print(f"missing entry image: {source}", file=sys.stderr)
        return False
    if source.stat().st_size == 0:
        print(f"entry image is empty: {source}", file=sys.stderr)
        return False
    return True


def ship_entry():
    paths = EntryPaths.resolve()
    paths.announce()
    if not verify(paths.source):
        return 1
    paths.out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(paths.source, paths.dest)
    if paths.source.stat().st_size != paths.dest.stat().st_size:
        print("size mismatch after copy", file=sys.stderr)
        return 1
    print("done")
    return 0


def main():
    return ship_entry()


if __name__ == "__main__":
    raise SystemExit(main())
