from collections import deque
from itertools import permutations, combinations

TRANSFORMS = (
    (1,1,1),
    (1,1,-1),
    (1,-1,1),
    (1,-1,-1),
    (-1,1,1),
    (-1,1,-1),
    (-1,-1,1),
    (-1,-1,-1)
)

def parse(scanner):
    out = set()
    for l in scanner.split('\n')[1:]:
        out |= {tuple(map(int, l.split(',')))}
    return out

inp = [*map(parse, open(0).read().strip().split('\n\n'))]
beacons = set(inp[0])
scannerpos = {(0,0,0)}
queue = deque(inp[1:])

def orients(pos, transform, perm, offset):
    pos = tuple(x*y for x, y in zip(pos, transform))
    pos = tuple(pos[x] for x in perm)
    pos = tuple(x+y for x, y in zip(pos, offset))
    return pos

def find_pos(scanner, beacons, scannerpos):
    for transform in (TRANSFORMS):
        for perm in permutations((0,1,2)):
            for b1 in scanner:
                b1 = orients(b1, transform, perm, (0,0,0))
                for b_pos in beacons:
                    offset = tuple(x-y for x, y in zip(b_pos, b1))
                    common = {b_pos}
                    for b2 in scanner:
                        b2 = orients(b2, transform, perm, offset)
                        for node in scannerpos:
                            for x, y in zip(b2, node):
                                if abs(x-y) > 1000:
                                    break
                            else:
                                break
                        else:
                            continue
                        if b2 not in beacons:
                            break
                        common.add(b2)
                    if len(common) >= 12:
                        beacons |= set(orients(b2, transform, perm, offset) for b2 in scanner)
                        scannerpos.add(offset)
                        return True
    return False

def solve():
    while queue:
        start = queue.popleft()
        if find_pos(start, beacons, scannerpos):
            continue
        queue.append(start)
    print(len(beacons))

    i = 0
    for x, y in combinations(scannerpos, 2):
        curr = 0
        for x, y in zip(x, y):
            curr += abs(x-y)
        i = max(i, curr)
    print(i)

solve()
