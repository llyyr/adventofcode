#!/usr/bin/env python3.11


cycles = ['off by one lol']
x = 1
for l in open('10.txt'):
    if 'noop' in l:
        cycles.append(x)
    elif 'addx' in l:
        cycles.extend([x, x])
        x += int(l.split()[1])

print(sum(cycles[i]*i for i in range(20,220+1,40)))

for i in range(1, len(cycles), 40):
    for j in range(40):
        print(end="##" if abs(cycles[i + j] - j) <= 1 else "  ")
    print()
