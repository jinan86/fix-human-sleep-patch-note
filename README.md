# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/jinan86/fix-human-sleep-patch-note/rank.svg)](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/jinan86/fix-human-sleep-patch-note/reward.svg)](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

Entry for the [Fix Human Sleep: Funniest Patch Note](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27) competition on [make.fun](https://make.fun).

## The patch note

> Fixed: sleep now actually restores humans; previously it just buffered for 8 hours and crashed on wake.

## How it works

`main.py` (Python 3, standard library only) holds the patch note as a
single constant. It validates the note against the competition gate —
1–160 characters, a single line, not only whitespace, ending with
sentence punctuation — then writes its exact UTF-8 bytes to
`/output/entry.txt` with no trailing newline.

The program is fully deterministic: no input, no network, no randomness,
no clock. Running it twice produces byte-identical output.

## Run

```sh
python3 main.py
```

Then read `/output/entry.txt`.
