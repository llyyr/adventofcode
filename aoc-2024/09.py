#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")

def part1(F, B):
    ret = 0
    for j in B:
        i, id = F.pop()
        if j > i:
            ret += i * id
            break
        ret += j * id
    return ret + sum(i * id for i, id in F)

def find_space(B, l):
    idx, length = 0, 0
    for n in range(l, 10):
        if (ll := B[n]):
            i = ll[0]
            if not idx or i < idx:
                idx, length = i, n
    if idx:
        heapq.heappop(B[length])
        if length > l:
            heapq.heappush(B[length - l], idx + l)
    return idx

def part2(F, B):
    for id in range(max(F), 0, -1):
        i, n = F[id]
        if (j := find_space(B, n)) and j < i:
            F[id] = j, n
    return sum(id * (i * n + n * (n - 1) // 2) for id, (i, n) in F.items())

def solve(inp):
    i, F1, B1, F2, B2 = 0, [], [], {}, {}
    for idx, n in enumerate(map(int, inp)):
        if idx % 2 == 0:
            F1.extend((i + d, idx // 2) for d in range(n))
            F2[idx // 2] = i, n
        else:
            B1.extend(i + d for d in range(n))
            heapq.heappush(B2.setdefault(n, []), i)
        i += n
    return part1(F1, B1), part2(F2, B2)

print(*solve(ch for line in open(filename) for ch in line.strip()))
