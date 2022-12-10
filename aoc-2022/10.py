#!/usr/bin/env python3.11


cycles = ['off by one lol']
x = 1
for l in open(0):
    if l.startswith('noop'):
        cycles += [x]
    else:
        cycles += [x, x]
        x += int(l.split(' ')[1])

print(sum(cycles[i]*i for i in (20, 60, 100, 140, 180, 220)))

for i in (1, 41, 81, 121, 161, 201):
    crt = ''
    for j in range(i, i+40):
        if abs(cycles[j] - (j - 1) % 40) < 2:
            crt += '@'
        else:
            crt += ' '
    print(crt)
