#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else __file__.replace('py', 'txt')
inp = open(filename).read().strip()
EXPR = re.compile(r"mul\((\d+),(\d+)\)")

print(sum(int(a) * int(b) for a, b in re.findall(EXPR, inp)))
print(sum(int(a) * int(b) for dos in [i.split("don't()")[0] for i in inp.split("do()")] for a, b in re.findall(EXPR, dos)))

