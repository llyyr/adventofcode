#!/usr/bin/env python3.10
inp = list(''.join(bin(int(c, 16))[2:].zfill(4) for c in next(open(0)).rstrip()))
p1 = 0

def decode(bins):
    global p1
    data = []
    ver = int(''.join(bins[:3]), 2)
    p1 += ver
    idx = int(''.join(bins[3:6]), 2)
    del bins[:6]
    if idx == 4:
        lit = []
        while True:
            cont = bins.pop(0)
            lit += bins[:4]
            del bins[:4]
            if cont == '0':
                break
        data = int(''.join(lit), 2)
    else:
        if bins.pop(0) == '0':
            l = int(''.join(bins[:15]), 2)
            del bins[:15]
            _data = bins[:l]
            del bins[:l]
            while _data:
                data += [decode(_data)]
        else:
            lim = int(''.join(bins[:11]), 2)
            del bins[:11]
            for _ in range(lim):
                data += [decode(bins)]
    return ver, idx, data

def calcv(bins):
    ver, idx, pkts = bins
    match idx:
        case 0: return sum(map(calcv, pkts))
        case 1:
            prod = 1
            for packet in pkts:
                prod *= calcv(packet)
            return prod
        case 2: return min(map(calcv, pkts))
        case 3: return max(map(calcv, pkts))
        case 4: return pkts
        case 5: return 1 if calcv(pkts[0]) > calcv(pkts[1]) else 0
        case 6: return 1 if calcv(pkts[0]) < calcv(pkts[1]) else 0
        case 7: return 1 if calcv(pkts[0]) == calcv(pkts[1]) else 0
        case _: assert False

bins = decode(inp)
print(p1)
print(calcv(bins))
