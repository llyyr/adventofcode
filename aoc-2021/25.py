#!/usr/bin/env python3.10
inp = open(0).read().splitlines()
R = len(inp)
C = len(inp[0])

def sim(inp, ch):
    new_inp = [list(r) for r in inp]
    for r in range(R):
        for c in range(C):
            if inp[r][c] != ch:
                continue
            rr = (r + 0) % R
            cc = (c + 1) % C
            if ch == 'v':
                rr = (r + 1) % R
                cc = (c + 0) % C
            if inp[rr][cc] == '.':
                new_inp[r][c] = '.'
                new_inp[rr][cc] = ch
    return [''.join(r) for r in new_inp]

i = 0
while i:=i+1:
    old_inp = inp[:]
    inp = sim(inp, '>')
    inp = sim(inp, 'v')
    if inp == old_inp:
        break
print(i)
