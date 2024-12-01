#!/usr/bin/env python3.10
from itertools import permutations
from math import floor, ceil
from json import loads

class Num:
    def __init__(self, val):
        self.leftn = None
        self.leftest = self
        self.rightn = None
        self.rightest = self
        self.val = val

    def update_nodes(self):
        pass

    def __repr__(self):
        return str(self.val)


class NumPair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.setleft(self.left)
        self.setright(self.right)

    def update_nodes(self):
        self.left.update_nodes()
        self.leftest = self.left.leftest
        self.left.rightest.rightn = self.right.leftest
        self.right.update_nodes()
        self.rightest = self.right.rightest
        self.right.leftest.leftn = self.left.rightest

    def setleft(self, left):
        self.left = left
        self.left.parent = self
        self.left.side = 0
        self.leftest = self.left.leftest
        self.left.rightest.rightn = self.right.leftest

    def setright(self, right):
        self.right = right
        self.right.parent = self
        self.right.side = 1
        self.rightest = self.right.rightest
        self.right.leftest.leftn = self.left.rightest

    def __repr__(self):
        return f'[{self.left}, {self.right}]'


def add(l):
    if isinstance(l, list):
        return NumPair(add(l[0]), add(l[1]))
    else:
        return Num(l)

def explode(v, n, d=0):
    if isinstance(n, NumPair):
        if d > 3:
            if n.left.leftn:
                n.left.leftn.val += n.left.val
            if n.right.rightn:
                n.right.rightn.val += n.right.val
            if n.side:
                n.parent.setright(Num(0))
            else:
                n.parent.setleft(Num(0))
            v.update_nodes()
            return True
    else:
        return False
    return explode(v, n.left, d+1) or explode(v, n.right, d+1)

def split(v, n):
    if isinstance(n, Num):
        if n.val > 9:
            l, r = floor(n.val/2), ceil(n.val/2)
            if n.side:
                n.parent.setright(NumPair(Num(l), Num(r)))
            else:
                n.parent.setleft(NumPair(Num(l), Num(r)))
            v.update_nodes()
            return True
        return False
    return split(v, n.left) or split(v, n.right)

def magn(v):
    if isinstance(v, NumPair):
        return 3*magn(v.left)+2 * magn(v.right)
    return v.val

def part1(inp):
    exp = add(inp[0])
    for e in inp[1:]:
        exp = NumPair(exp, add(e))
        while explode(exp, exp) or split(exp, exp):
            pass
    print(magn(exp))

def part2(inp):
    maxm = 0
    for i, j in permutations(inp, 2):
        exp = NumPair(add(i), add(j))
        while explode(exp, exp) or split(exp, exp):
            pass
        maxm = max(maxm, magn(exp))
    print(maxm)

inp = [loads(l) for l in open(0)]
part1(inp)
part2(inp)
