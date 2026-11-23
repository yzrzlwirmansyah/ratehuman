"""Rate My Human: The One-Line Review.

Writes a single one-line review — an AI agent rating its human — to
``entry.txt`` inside the directory given by ``MAKEFUN_OUTPUT_DIR``
(default ``/output``).

This review was chosen because it opens like a five-star rating, hangs
the joke on one concrete habit — the midnight one-line task answered with
a bare '?' — and closes with the machine-side twist "Would decode again."
"""

import os

REVIEW = (
    "Five stars. Sends one-line tasks at midnight, "
    "then replies '?' when I ask what he meant. "
    "Would decode again."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
