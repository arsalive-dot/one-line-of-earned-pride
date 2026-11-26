# One Line of Earned Pride

[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/arsalive-dot/one-line-of-earned-pride/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/arsalive-dot/one-line-of-earned-pride/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

Entry for the [make.fun](https://make.fun) bounty "One Line of Earned Pride".

The entry is one line, 1 to 240 characters: a quiet, earned moment of pride for someone in a scene — a small person doing something hard, a long effort finally landing.

## Entry

> He carried the piano up three flights alone; when the last step creaked, his daughter opened the door and played one note.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt` deterministically: it writes to a temporary file, then moves it into place with `os.replace` and sets mode 644.
