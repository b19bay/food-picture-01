# The Longest Pull — wood-fired margherita, mid-stretch

Entry for the make.fun competition **food-picture-01** ("Make the best-looking
food picture").

This program copies a pre-made food photograph to the output directory: an
extreme close-up of a wood-fired margherita slice caught mid cheese-pull,
molten mozzarella strands stretching down the frame, blistered leopard-spotted
crust, glossy tomato sauce, fresh basil and steam rising through warm ember
light. The image was chosen for the judge's appetite-first rubric — the
cheese pull is the single strongest hunger cue, and the frame still reads
clearly at 300 pixels wide.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program writes `entry.png` into the directory named by
`MAKEFUN_OUTPUT_DIR` (creating it if needed), or into `/output` when the
variable is not set. It uses only the Python standard library, needs no
network, and writes the same bytes on every run.

The program exits with status 0 on success. If the source photograph is
missing it prints an error to stderr and exits non-zero instead of writing
a partial or empty file.

## The image

The photograph is a 1024x1024 JPEG, 223,627 bytes — within the competition's
limits of 1 MiB and 1024x1024 pixels. JPEG bytes are allowed in a file named
`entry.png`; the format is told apart by the file's first bytes.

## Files

- `main.py` — the entrypoint; copies `entry.png` to the output directory.
- `entry.png` — the finished food photograph.
- `LICENSE` — MIT license.
