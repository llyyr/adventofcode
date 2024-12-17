#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().splitlines()
A, B, C = (int(line.split()[-1]) for line in inp[:3])
P = list(map(int, inp[-1].split()[-1].split(",")))
DIV = lambda A, c: math.trunc(A / pow(2, c))

def p1(P=P, A=A, B=B, C=C):
    ip, ret = 0, []
    while ip < len(P):
        val = P[ip + 1]
        combo = val if val < 4 else [A, B, C, None][val - 4]
        match P[ip]:
            case 0: A = DIV(A, combo)
            case 1: B ^= val
            case 2: B = combo % 8
            case 3: ip = val - 2 if A else ip
            case 4: B ^= C
            case 5: ret.append(combo % 8)
            case 6: B = DIV(A, combo)
            case 7: C = DIV(A, combo)
        ip += 2
    return ret

def p2():
    S = [(0, 0)]
    while S:
        A, depth = S.pop()
        if depth == len(P):
            return A
        for i in range(7, -1, -1):
            next = A * 8 + i
            if p1(A=next)[0] == P[-depth - 1]:
                S.append((next, depth + 1))

print(",".join(map(str, p1())), p2())
