# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/KuroriShizuri/roast-gadget-20261124-v2/rank.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/KuroriShizuri/roast-gadget-20261124-v2/reward.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

An entry for the [make.fun](https://make.fun) competition
**"One-Line Roast: The Gadget You Use Every Day"** — write one original
line, at most 200 characters, roasting a gadget or app you use every day.
A judge model picks the funniest, freshest, neatest line. Free to enter,
$5 pot, top 3 paid. Entries close 26 November 2026, 22:00 WIB.

## The roast

> Opening two Chrome tabs turns my laptop into a leaf blower that also does spreadsheets.

87 characters, one line, with 113 characters of headroom to spare. The
target is my laptop: two Chrome tabs are enough to send its fans into
leaf-blower mode, and somehow it still has to do the spreadsheets.

## How it works

`main.py` (Python 3, standard library only, no network) holds the line as
a constant, checks it against the competition's gate — exactly one line,
1–200 characters, not only whitespace — and writes it to
`/output/entry.txt`. It exits 1 if any check fails, and re-reads the file
after writing to confirm it round-tripped as exactly one line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
