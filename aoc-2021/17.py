#!/usr/bin/env python3.10
from math import ceil, sqrt
# "target area: x=195..238, y=-93..-67"
xmin, xmax, ymin, ymax = 195, 238, -93, -67
best_height = 0
cnt = 0
for vx in range(ceil(-0.5 + sqrt(1+8*xmin)/2), xmax+1):
    for vy in range(ymin, abs(ymin)+1):
        x, y, dx, dy = 0, 0, vx, vy
        height = None
        peak = 0
        while y>=ymin and x<=xmax:
            y += dy
            x += dx
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            peak = max(y, peak)
            if xmin<=x<=xmax and ymin<=y<=ymax:
                height = peak
        if height != None:
            cnt += 1
            if height > best_height:
                best_height = height
print(best_height)
print(cnt)
