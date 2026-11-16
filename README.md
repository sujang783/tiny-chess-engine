# tiny-chess — a 4 KB chess engine

A chess engine in a single `main.py` (4,068 bytes, Python 3 stdlib only),
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
  in check), MVV-LVA capture ordering + promotion bonus.
- **Evaluation:** material + formula piece-square tables (centre, pawn
  advance, king safety taper), tempo +10. No transposition table, no
  null-move pruning — both were cut to fit the 4,096-byte cap.

## Verification

- Perft: start position 20/400/8902, kiwipete 48/2039/97862, CPW position 5
  44/1486/62379 — all exact.
- Mate-in-1 (Qxf7#) found; no phantom-mate bug (Bxd5 regression: −913).
- Practice trial 0 vs the house gauntlet: **Elo 1,099** (2 won / 0 drawn / 4
  lost, all games decided by checkmate), wall 512 s, bot exit 0. Below the
  1,154 practice floor and the 1,365 house-baseline mean — the binding
  constraint is search depth (~3 plies at the 60,000-node budget in Python).

## Run

The program talks to the make.fun env over HTTP (`MAKEFUN_ENV_URL`):

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

## License

MIT — see `LICENSE`.
