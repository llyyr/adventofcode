#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")

def solve():
    G = {(r, c): ch for r, l in enumerate(open(filename)) for c, ch in enumerate(l)}
    P, O, seen = set(), set(), set()
    pos = next(k for k, v in G.items() if v == "^")
    dir = (-1, 0)
    rot90 = lambda r, c: (c, -r)
    move = lambda r, c, dr, dc: (r + dr, c + dc)

    while pos in G:
        P.add(pos)
        state = (*pos, *dir)
        seen.add(state)
        cur_pos = move(*state)

        if G.get(cur_pos) != "#":
            if cur_pos in G and cur_pos not in P:
                new_pos, new_dir, new_seen = pos, rot90(*dir), seen.copy()

                while new_pos in G:
                    state = (*new_pos, *new_dir)
                    if state in new_seen:
                        O.add(cur_pos)
                        break
                    new_seen.add(state)

                    next_move = move(*state)
                    if next_move != cur_pos and G.get(next_move) != "#":
                        new_pos = next_move
                    else:
                        new_dir = rot90(*new_dir)

            pos = cur_pos
        else:
            dir = rot90(*dir)

    return len(P), len(O)

print(*solve())
