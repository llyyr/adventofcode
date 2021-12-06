#!/usr/bin/env python3.10
inp = list(map(int, open(0).read().split(',')))

def solve(days):
    fish = {}
    for n in inp:
        fish[n] = 1 if n not in fish else fish[n] + 1
    for _ in range(days):
        new = {}
        for k, v in fish.items():
            if k == 0:
                new[6] = v if 6 not in new else new[6] + v
                new[8] = v if 8 not in new else new[8] + v
            else:
                new[k-1] = v if (k-1) not in new else new[k-1] + v
        fish = new
    return sum(fish.values())

print(solve(80))
print(solve(256))

