from typing import Any
import operator
import math
from timeit import default_timer
import heapq
from functools import wraps, reduce, partial, cache, cmp_to_key
from collections import Counter, deque, defaultdict, namedtuple
from itertools import *
import itertools
from copy import deepcopy
import re
import sys

class EqualToAny(object):
    def __eq__(self, other):
        return True

NORTH, SOUTH, EAST, WEST = ((-1, 0), (1, 0), (0, 1), (0, -1))
UP, DOWN, RIGHT, LEFT = ((-1, 0), (1, 0), (0, 1), (0, -1))
DIRS = (NORTH, SOUTH, EAST, WEST)
DIRMAP = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
NEIGHBOURS = tuple(itertools.product((-1, 0, 1), repeat=2))
BLOCK = "█"

def neighbours(x=0, y=0, amount=4):
    for dy, dx in NEIGHBOURS:
        if ((amount == 4 and abs(dx) != abs(dy)) or
            (amount == 8 and not dx == dy == 0) or
             amount == 9):
            yield (x+dx, y+dy)

def hash2coords(inp):
    coords = set()
    for r, line in enumerate(inp):
        for c, ch in enumerate(line):
            if ch == '#':
                coords.add((r, c))
    return coords

def grid2dict(inp):
    G = {}
    for r, line in enumerate(inp):
        for c, ch in enumerate(line):
            G[(r, c)] = ch
    return G, len(inp), len(inp[0])

class timer:
    def __init__(self, auto_print=False):
        self.auto_print = auto_print
        self.total_time = 0
        self.call_count = 0
        self.name = None

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = default_timer()
            out = func(*args, **kwargs)
            t1 = default_timer()
            elapsed_time = t1 - t0
            self.total_time += elapsed_time
            self.call_count += 1
            if self.auto_print:
                print(f"{func.__name__} took {elapsed_time * 1000:.3f} ms")
            return out

        self.name = func.__name__
        wrapper.print_time = self.print_time # type: ignore
        return wrapper

    def print_time(self):
        print(f"{self.name} took {self.total_time * 1000:.3f} ms over {self.call_count} calls")

def ints(s):
    return [int(s) for s in re.findall(r'-?\d+', s)]

def sign(x):
    if isinstance(x, complex):
        return 0.0 if abs(x) == 0 else x / abs(x)
    return (x > 0) - (x < 0)

def py_ints(s):
    """
    >>> ints("Hello4.2this.is random 24 text42")
    [4.2, 24, 42]
    >>> ints("2.3+45-99")
    [2.3, 45, -99]
    >>> ints("Avogadro's number, 6.022e23, is greater than 1 million.")
    [6.022e+23, 1]
    """
    nums = []
    cur = ''
    for c in s.lower() + '!':
        if (c.isdigit() or
            (c == 'e' and ('e' not in cur) and (cur not in ['', '.', '-', '-.'])) or
            (c == '.' and ('e' not in cur) and ('.' not in cur)) or
            (c == '+' and cur.endswith('e')) or
            (c == '-' and ((cur == '') or cur.endswith('e')))):
            cur += c
        else:
            if cur not in ['', '.', '-', '-.']:
                if cur.endswith('e'):
                    cur = cur[:-1]
                elif cur.endswith('e-') or cur.endswith('e+'):
                    cur = cur[:-2]
                nums.append(cur)
            if c == '.' or c == '-':
                cur = c
            else:
                cur = ''
    nums = [float(t) if ('.' in t or 'e' in t) else int(t) for t in nums]
    return nums
