#!/usr/bin/env python3.11


inp = [l.split() for l in open(0)]
DIRS = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def part1():
    x1, y1 = (0, 0)
    x2, y2 = (0, 0)
    seen = set((0, 0))
    for d, i in inp:
        dx, dy = DIRS[d]
        for _ in range(int(i)):
            x1 += dx
            y1 += dy
            while max(abs(x2 - x1), abs(y2 - y1)) >= 2:
                if abs(x2 - x1) > 0:
                    x2 += 1 if x1 > x2 else -1
                if abs(y2 - y1) > 0:
                    y2 += 1 if y1 > y2 else -1
                seen.add((x2, y2))
    print(len(seen))

def part2():
    rope = [(0, 0)] * 10
    seen = set()
    for d, i in inp:
        delta = DIRS[d]
        for _ in range(int(i)):
            rope[0] = tuple(map(sum, zip(rope[0], delta)))
            for i in range(1, len(rope)):
                x1, y1 = rope[i-1]
                x2, y2 = rope[i]
                while max(abs(x2 - x1), abs(y2 - y1)) >= 2:
                    if abs(x2 - x1) > 0:
                        x2 += 1 if x1 > x2 else -1
                    if abs(y2 - y1) > 0:
                        y2 += 1 if y1 > y2 else -1
                    rope[i] = (x2, y2)
            seen.add(rope[-1])
    print(len(seen))

part1()
part2()
