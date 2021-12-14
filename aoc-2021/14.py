#!/usr/bin/env python3.10
from collections import Counter

def solve():
    tmp, rules = open(0).read().split('\n\n')
    r = dict(l.split(' -> ') for l in rules.splitlines())

    pairs = Counter()
    for x, y in zip(tmp, tmp[1:]):
        pairs.update([x + y])

    for t in range(1, 41):
        npairs = Counter()
        for p in pairs:
            npairs[p[0] + r[p]] += pairs[p]
            npairs[r[p] + p[1]] += pairs[p]
        if t in (10, 40):
            cnt = Counter()
            for p in npairs:
                cnt[p[0]] += npairs[p]
            cnt.update([tmp[-1]])
            print(max(cnt.values()) - min(cnt.values()))
        pairs = npairs

solve()
