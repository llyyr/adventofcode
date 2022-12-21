#!/usr/bin/env python3.11

from aochelper import *
from operator import add, sub, truediv, mul
from z3 import Optimize, Int, sat

inp = [l.strip() for l in open('21.txt')]

opmap = {'+': add, '-': sub, '*': mul, '/': truediv}

def solve(name):
    o = Optimize()
    for l in inp:
        lhs, *rhs = l.replace(':', '').split()
        if name == 'humn':
            if lhs == 'humn':
                continue
            if lhs == 'root':
                o.add(Int(rhs[0]) == Int(rhs[2]))
        if len(rhs) == 3:
            o.add(Int(lhs) == opmap[rhs[1]](Int(rhs[0]), Int(rhs[2])))
        elif len(rhs) == 1:
            o.add(Int(lhs) == int(*rhs))
    assert o.check() == sat, "unsatisfied"
    m = o.model()
    return m[Int(name)]

print(*map(solve, ('root', 'humn')))

