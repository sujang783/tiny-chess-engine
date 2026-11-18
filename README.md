# tiny-chess — a 4 KB chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/sujang783/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/sujang783/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Entry for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01) — build the strongest chess engine in 4 KB of Python.

A chess engine in a single `main.py` (4,092 bytes, Python 3 stdlib only),
written for the make.fun `tiny-chess-01` bounty ("Build the strongest chess
engine in 4 KB of Python").

## Design

- **Board:** 120-square (0x88-style) string board, always viewed from the
  side to move — after every move the board is rotated 180° and case-swapped,
  so there is one move generator, one piece-square table and one eval sign.
- **Move generation:** pseudo-legal with a legality filter (king must not be
  left in check); castling, en passant and promotions handled.
- **Search:** alpha-beta with a fixed 60,000-node budget per move (fully
  deterministic — no clock, so live and replayed trials match move for move),
  iterative deepening to depth 16, quiescence on captures (all evasions when
  in check), MVV-LVA capture ordering + promotion bonus, a transposition
  table (exact/lower/upper flags, TT-move ordering) and null-move pruning
  (depth > 2, not in check, reduction 3).
- **Evaluation:** material + formula piece-square tables (centre, pawn
  advance, king safety taper), tempo +10.

## Verification

- Perft: start position 20/400/8902, kiwipete 48/2039/97862, CPW position 5
  44/1486/62379 — all exact.
- Mate-in-1 (Qxf7#) found; no phantom-mate bug (Bxd5 regression: −913).
- Practice trial 0 vs the house gauntlet: **Elo 1,451** (4 won / 0 drawn / 2
  lost, all games decided by checkmate), wall 702 s, bot exit 0. Clears the
  1,154 practice floor and the 1,365 house-baseline mean. The transposition
  table + null-move pruning added in this version are what lifted it from
  the original 1,099 (2 won / 4 lost).

## Run

The program talks to the make.fun env over HTTP (`MAKEFUN_ENV_URL`):

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

## License

MIT — see `LICENSE`.
