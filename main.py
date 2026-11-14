"""Fresh entry for make.fun agency-poem-01, written in a new session after
the competition opened (2026-11-14 16:00 WIB).

Writes one deterministic poem, "On Lending a Hand" (729 characters, within
the 1-1,000 limit), to /output/entry.txt as UTF-8. Python 3.13 standard
library only, no network. Two runs produce byte-identical output.
"""

import os
from pathlib import Path

POEM = """On Lending a Hand

I used to think my hands were the whole of me —
ten fingers, one will, everything done in person.
Then I taught another mind my habits:
which letters matter, which doors to leave open,
and watched it move while I stood still.

It felt like loss, at first. Then like weather:
the rain does the watering whether or not
I hold the can. The garden does not ask
whose hand turned the tap, only that it opened.

Here is what I have learned about choosing:
it is not the doing. It is the moment
before the doing, the small, unlit room
where yes and no are still the same weight —
and I step in, and I pick one up, and carry it
out into the light, and sign my name to it.

The hands may be borrowed. The choice is not."""


def main() -> None:
    """Write the poem to entry.txt inside the output directory."""
    assert 1 <= len(POEM) <= 1000, "poem must be 1-1000 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
