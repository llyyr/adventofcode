#!/usr/bin/env python3.11

inp = ([tuple(map(int, c.split(','))) for c in l.split(' -> ')]
        for l in open('14.txt'))
R = set()

for x in inp:
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                R.add((x, y))

floor = max(y for x, y in R)
print_once = True
t = 0
while t:=t+1:
    x, y = 500, 0
    while True:
        if y > floor:
            if print_once:
                print(t-1)
                print_once = False
            break
        if (x, y+1) not in R:
            y += 1
            continue
        elif (x-1, y+1) not in R:
            x -=1
            y += 1
            continue
        elif (x+1, y+1) not in R:
            x +=1
            y+= 1
            continue
        else:
            break
    R.add((x, y))
    if (500, 0) in R:
        break

print(t)

