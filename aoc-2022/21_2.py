#!/usr/bin/env python3.11

from aochelper import *

exprs = {lhs: rhs.split() for l in open('21.txt') for lhs, rhs in [l.split(': ')]}

def solve(lhs):
    rhs = exprs[lhs]
    return rhs[0] if len(rhs)==1 else '('+solve(rhs[0])+rhs[1]+solve(rhs[2])+')'

print(int(eval(solve('root'))))

exprs['humn'] = ['-1j']
exprs['root'][1] = '-'
expr = eval(solve('root'))
print(int(expr.real / expr.imag))
