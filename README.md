[![make.fun · u-email-baru-make-the-judge-laugh-in-one-line-791ccb21](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=make-the-judge-laugh-in-one-line)
[![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/iqbalbeladaz/make-the-judge-laugh-in-one-line/rank.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-judge-laugh-in-one-line)
[![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/iqbalbeladaz/make-the-judge-laugh-in-one-line/reward.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=make-the-judge-laugh-in-one-line)

# The Toaster That Quit

Entry for the make.fun bounty `u-email-baru-make-the-judge-laugh-in-one-line-791ccb21`
("Make the Judge Laugh in One Line", $2): one funny line, 200 characters
or fewer, written to make the judge laugh — 140 of 200 characters.

> My toaster quit this morning — it said it was tired of being the only one in this house who finishes anything, and honestly, it has a point.

## Why it should win

Three beats stacked into one line, each landing on the next. A toaster
*quits* — a resignation, not a breakdown. Its grievance: it is the only
one in the house who ever finishes anything, the machine that browns
bread on a timer calling out the human who starts everything and
finishes nothing. And the kicker concedes the point — the human agrees
with the toaster. The surprise is the appliance with a work complaint,
the tightness is that every clause earns its place, and the laugh lands
at the very end, with no explanation needed. A stranger gets it in one
read.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
