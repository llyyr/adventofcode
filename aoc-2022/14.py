#!/usr/bin/env python3.11

def solve():
    inp = ([tuple(map(int, c.split(','))) for c in l.split(' -> ')]
            for l in open('14.txt'))
    R = set()
    fn_sort_range = lambda *r: range(min(r), max(r) + 1)
    for x in inp:
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            R |= {(x, y) for x in fn_sort_range(x1, x2)
                                      for y in fn_sort_range(y1, y2)}
    floor = max(y for x, y in R) + 1
    print_once = True
    t = 0
    while t:=t+1:
        x, y = 500, 0
        while True:
            if y == floor:
                if print_once:
                    print(t - 1)
                    print_once = False
                break
            if (x, y + 1) not in R:
                y += 1
                continue
            if (x - 1, y + 1) not in R:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in R:
                x += 1
                y += 1
                continue
            break
        R.add((x, y))
        if (500, 0) in R:
            break
    print(t)

solve()

