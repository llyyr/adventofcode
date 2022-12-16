#!/usr/bin/env python3.11

from aochelper import *

inp = [l.split() for l in open('16.txt').read().strip().splitlines()]
node_count = len(inp)
node_idx_map = defaultdict(lambda: len(node_idx_map))
node_map = {}
rates = [0] * node_count
all_mask = 0
dist_map = defaultdict(lambda: float('inf'))

pressure_node_idx = 0
for line in inp:
    rate = int(line[4].split('=')[-1][:-1])
    start = node_idx_map[line[1]]
    rates[start] = rate
    if rate > 0:
        node_map[pressure_node_idx] = start
        all_mask += 1 << pressure_node_idx
        pressure_node_idx += 1
    for target in line[9:]:
        target = node_idx_map[target[:2]]
        dist_map[(target, start)] = 1

for x, y, z in product(range(node_count), repeat=3):
    dist_map[(y, z)] = min(dist_map[(y, z)], dist_map[(y, x)] + dist_map[(x, z)])

@cache
def dp(cur, t, remaining_mask):
    i, best, mask = 0, 0, 1
    while mask <= remaining_mask:
        if mask & remaining_mask:
            new = node_map[i]
            if t + 1 >= dist_map[(cur, new)]:
                new_t = t - dist_map[(cur, new)] - 1
                new_mask = remaining_mask - mask
                best = max(best, dp(new, new_t, new_mask) + new_t * rates[new])
        i += 1
        mask *= 2
    return best

print(dp(node_idx_map['AA'], 30, all_mask))
print(max(dp(node_idx_map['AA'], 26, all_mask - mask)
          + dp(node_idx_map['AA'], 26, mask) for mask in range(all_mask + 1)))

