# The Meeting That Should Have Been One Line

[![make.fun · u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/DizellaCapital/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/DizellaCapital/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

> Karen cancelled the launch in the hallway at 8:12, Dave already expensed the $40,000 party, and this meeting is twelve people pretending the hallway never happened.

## How it works

`main.py` (Python standard library only) writes the single 164-character
sentence above to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (falling back to
`/output`). Before writing, it validates the line: exactly one line, 1–200
characters, no tabs, ends with sentence punctuation. After writing, it reads
the file back and verifies the content matches the validated line
byte-for-byte.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/meeting-v4-out python3 main.py
cat /tmp/meeting-v4-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the [make.fun](https://make.fun/r/qxacafna) bounty
"The Meeting That Should Have Been One Line".
