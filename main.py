"""make.fun entry: One Line of Earned Pride.

Writes one line to /output/entry.txt: a quiet, earned moment of
pride for someone in a scene — a small person doing something hard,
a long effort finally landing.

The line earns its pride inside the scene: a father hauls a piano
up three flights alone, and the payoff is not a trophy but his
daughter opening the door and playing a single note — the effort
was for her, and the pride arrives with that last word.
"""

import os

ENTRY = (
    "He carried the piano up three flights alone; when the last step "
    "creaked, his daughter opened the door and played one note."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
