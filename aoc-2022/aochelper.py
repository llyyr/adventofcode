from timeit import default_timer
from functools import wraps, reduce, partial, cache, cmp_to_key
from collections import Counter, deque, defaultdict, namedtuple
from itertools import *
from copy import deepcopy
import sys

DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
DIRMAP = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def neighbours(x=0, y=0, amount=4):
    assert amount in (4, 8, 9)
    for dy, dx in itertools.product((-1, 0, 1), repeat=2):
        if ((amount == 4 and abs(dx) != abs(dy)) or
            (amount == 8 and not dx == dy == 0) or
             amount == 9):
            yield (x+dx, y+dy)

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = default_timer()
        out = func(*args, **kwargs)
        t1 = default_timer()
        print(f"{func.__name__} took {(t1-t0)*1000:.3f} ms")
        return out
    return wrapper


def ints(s):
    """
    Extract numbers from a string.

    Examples
    --------
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

def sign(x):
    if isinstance(x, complex):
        return 0.0 if abs(x) == 0 else x / abs(x)
    return (x > 0) - (x < 0)

