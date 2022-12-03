#!/usr/bin/env python3.11

import string


inp = [l.rstrip() for l in open('03.txt')]

def main(part):
    share = []
    if part == 1:
        for l in inp:
            x, y = l[:len(l)//2], l[len(l)//2:]
            share.append(next(x for x in (set(x) & set(y))))
    elif part == 2:
        for i in range(0, len(inp), 3):
            share.append(next(x for x in (set(inp[i]) & set(inp[i+1]) & set(inp[i+2]))))
    sum = 0
    for s in share:
        sum += string.ascii_letters.index(s) + 1
    print(sum)

main(1)
main(2)
