"""agency-poem-01: write one poem about agency to /output/entry.txt.

The poem is fixed and deterministic: two runs write byte-identical files.
It is 729 characters, inside the gate's 1 to 1,000, and not only whitespace.
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

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


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
