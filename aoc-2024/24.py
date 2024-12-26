#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
W, C = (p.splitlines() for p in open(filename).read().strip().split("\n\n"))
D = {k: int(v) for k, v in (line.split(": ") for line in W)}

def p1():
    for _ in range(len(W)):
        for wire in C:
            a, op, b, dest = wire.replace("->", "").split()
            if a in D and b in D:
                D[dest] = {"XOR": D[a] ^ D[b], "OR": D[a] | D[b], "AND": D[a] & D[b]}[op]
    return int("".join(str(D[f"z{i:02d}"]) for i in range(45, -1, -1)), 2)

def find(x, y, op):
    return next((c.split(" -> ")[-1] for c in C
        if f"{x} {op} {y}" in c or f"{y} {op} {x}" in c), None)

def swap(a, b):
    return [f"{c.split(' -> ')[0]} -> {b if out == a else a}"
        if (out := c.split(' -> ')[-1]) in {a, b} else c for c in C]

def p2():
    swaps, carry, bit = [], None, 0
    while bit < 45:
        x, y, z = f"x{bit:02d}", f"y{bit:02d}", f"z{bit:02d}"
        xy_xor, xy_and = find(x, y, "XOR"), find(x, y, "AND")
        if bit:
            cin_xor = find(xy_xor, carry, "XOR")
            if not cin_xor or cin_xor != z:
                swaps += [cin_xor or xy_xor, z] if cin_xor else [xy_xor, xy_and]
                C[:] = swap(swaps[-2], swaps[-1])
                bit = 0
                continue
            carry = find(xy_and, find(xy_xor, carry, "AND"), "OR")
        else:
            carry = xy_and
        bit += 1
    return ",".join(sorted(swaps))

print(p1(), p2())

