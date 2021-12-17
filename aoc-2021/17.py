#!/usr/bin/env python3.10
from math import ceil, sqrt
# "target area: x=195..238, y=-93..-67"
x1, x2 = 195, 238
y1, y2 = -93, -67
best_height = 0
cnt = 0
for vx in range(ceil(-0.5 + sqrt(1+8*x1)/2), x2+1):
    for vy in range(y1, abs(y1)+1):
        x, y, dx, dy = 0, 0, vx, vy
        height = None
        peak = 0
        while y>=y1 and x<=x2:
            y += dy
            x += dx
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            peak = max(y, peak)
            if x1<=x<=x2 and y1<=y<=y2:
                height = peak
        if height != None:
            cnt += 1
            if height > best_height:
                best_height = height
print(best_height)
print(cnt)
