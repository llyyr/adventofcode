#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace("py", "txt")
inp = open(filename).read().split()
S = {int(s): inp.count(s) for s in inp}

for i in range(75):
    SS = defaultdict(int)
    for s, n in S.items():
        if s == 0:
            SS[1] += n
        elif (digits := len(str(s))) % 2 == 0:
            for p in divmod(s, 10 ** (digits // 2)):
                SS[p] += n
        else:
            SS[2024 * s] += n
    S = SS
    if i in (24, 74):
        print(sum(S.values()))
