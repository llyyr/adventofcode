#!/usr/bin/env python3.11

from aochelper import *

def decode(n):
    ret = 0
    for x in n:
        ret *= 5
        if x.isdigit():
            ret += int(x)
        elif x == "-":
            ret -= 1
        elif x == "=":
            ret -= 2
    return ret

def encode(n):
    ret = ""
    while n > 0:
        x = n % 5
        if x == 3:
            x = -2
            ch = "="
        elif x == 4:
            x = -1
            ch = "-"
        else:
            ch = str(x)
        ret = ch + ret
        n = (n - x) // 5
    return ret

print(encode(sum(decode(l.strip()) for l in open('25.txt'))))

