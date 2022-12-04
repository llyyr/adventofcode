#!/usr/bin/env python3.11


p1 = 0
p2 = 0

def parse(s):
    a, b = s.split('-')
    return int(a), int(b)

for line in open('04.txt'):
    x, y = map(parse, line.split(','))
    if (x[0]>=y[0] and x[1]<=y[1]) or (x[0]<=y[0] and x[1]>=y[1]):
        p1 += 1
    x, y = range(x[0], x[1]+1), range(y[0], y[1]+1)
    if set(x) & set(y):
        p2 += 1

print(p1, p2)
