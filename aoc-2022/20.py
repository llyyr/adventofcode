#!/usr/bin/env python3.11

from aochelper import *

def solve(k):
    ll = deque([*enumerate(int(l) * k for l in open('20.txt'))])
    for x in ll * (1 if k == 1 else 10):
        ll.rotate(-ll.index(x))
        ll.popleft()
        ll.rotate(-x[1])
        ll.append(x)
    ll = deque([v for _, v in ll])
    ll.rotate(-ll.index(0))
    return sum(ll[i * 1000] for i in (1, 2, 3))

print(*map(solve, (1, 811589153)))

