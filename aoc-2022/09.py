#!/usr/bin/env python3.11


inp = [l.split() for l in open('09.txt')]
DIRS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def solve(length):
    rope = [[0, 0] for _ in range(length)]
    seen = set()
    for d, i in inp:
        delta = DIRS[d]
        for _ in range(int(i)):
            rope[0] = list(map(sum, zip(rope[0], delta)))
            for i in range(1, length):
                dx, dy = list(map(lambda x, y: x - y, rope[i-1], rope[i]))
                if max(abs(dx), abs(dy)) >= 2:
                    rope[i][0] += (dx > 0) - (dx < 0)
                    rope[i][1] += (dy > 0) - (dy < 0)
            seen.add(tuple(rope[-1]))
    return len(seen)

print(solve(2))
print(solve(10))
