#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = [int(l) for l in open(filename)]
profits = defaultdict(int)

def F(n, MOD=16777216):
    ret = [n]
    for _ in range(2000):
        n = (n ^ (n << 6)) % MOD
        n = (n ^ (n >> 5)) % MOD
        n = (n ^ (n << 11)) % MOD
        ret.append(n)
    return ret

print(sum(F(n)[-1] for n in inp))

for n in inp:
    seen = {}
    prices = [x % 10 for x in F(n)]
    changes = [b - a for a, b in pairwise(prices)]
    for i in range(len(changes) - 3):
        sig = tuple(changes[i:i + 4])
        if sig not in seen:
            seen[sig] = prices[i + 4]
    for sig, price in seen.items():
        profits[sig] += price

print(max(profits.values()))
