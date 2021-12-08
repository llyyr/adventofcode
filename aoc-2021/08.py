#!/usr/bin/env python3.10
from itertools import permutations

inp = [[l.split() for l in l.split('|')] for l in open(0)]
MAP = [
    set('abcefg'),  # 0
    set('cf'),      # 1
    set('acdeg'),   # 2
    set('acdfg'),   # 3
    set('bcdf'),    # 4
    set('abdfg'),   # 5
    set('abdefg'),  # 6
    set('acf'),     # 7
    set('abcdefg'), # 8
    set('abcdfg'),  # 9
]

def mapping(digit, p):
    mapped = set()
    ref = list('abcdefg')
    for d in digit:
        mapped.add(ref[p.index(d)])
    return mapped

def solve(p1=False):
    ans = 0
    for left, right in inp:
        if p1:
            ans += sum(len(digit) in (2,3,4,7) for digit in right)
            continue
        for p in permutations('abcdefg'):
            if all(mapping(digit, p) in MAP for digit in left):
                digits = [MAP.index(mapping(digit, p)) for digit in right]
                ans += int(''.join(map(str, digits)))
    return ans

print(solve(True))
print(solve())
