#!/usr/bin/env python3.10
def solve():
    inp = open(0).read().splitlines()
    on = set()
    clist = [[], [], []]
    for i in range(len(inp)):
        target, l = inp[i].split()
        coords = [[*(map(int, x[2:].split('..')))] for x in l.split(',')]
        for j in range(3):
            coords[j][1] += 1
            clist[j] += [(coords[j][0], (i + 1))]
            clist[j] += [(coords[j][1], -(i + 1))]
        x, y, z = [range(max(-50, c[0]), min(c[1], 51)) for c in coords]
        for xx in x:
            for yy in y:
                for zz in z:
                    if target == 'on':
                        on |= {(xx,yy,zz)}
                    else:
                        on -= {(xx,yy,zz)}
    print(len(on))

    def sweep_z(on):
        cnt = 0
        last = 0
        on_z = set()
        coords = [z for z in clist[2] if abs(z[1]) in on]
        for z in sorted(coords):
            if len(on_z) > 0 and inp[max(on_z) - 1][:2] == 'on':
                cnt += z[0] - last
            last = z[0]
            if z[1] > 0:
                on_z |= {z[1]}
            else:
                on_z -= {-z[1]}
        return cnt

    def sweep_y(on):
        cnt = 0
        last = 0
        on_y = set()
        coords = [y for y in clist[1] if abs(y[1]) in on]
        for y in sorted(coords):
            cnt += (y[0] - last) * sweep_z(on_y)
            last = y[0]
            if y[1] > 0:
                on_y |= {y[1]}
            else:
                on_y -= {-y[1]}
        return cnt

    def sweep_x():
        cnt = 0
        on = set()
        last = 0
        for x in sorted(clist[0]):
            cnt += (x[0] - last) * sweep_y(on)
            last = x[0]
            if x[1] > 0:
                on |= {x[1]}
            else:
                on -= {-x[1]}
        return cnt
    print(sweep_x())
solve()
