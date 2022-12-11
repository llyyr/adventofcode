#!/usr/bin/env python3.11

inp = [g.splitlines() for g in open('11.txt').read().split('\n\n')]

def simulate(cycles):
    monkeys = []
    cnt = [0] * len(inp)
    mod = 1
    for block in inp:
        monkey = []
        monkey.append(list(map(int, block[1].split(': ')[1].split(', '))))
        monkey.append(eval("lambda old:" + block[2].split('=')[1]))
        monkey.append(v:=int(block[3].split()[-1]))
        monkey.append(int(block[4].split()[-1]))
        monkey.append(int(block[5].split()[-1]))
        monkeys.append(monkey)
        mod *= v
    for _ in range(cycles):
        for i, cur in enumerate(monkeys):
            for old in cur[0]:
                item = cur[1](old)
                if cycles == 20:
                    item //= 3
                else:
                    item %= mod
                monkeys[cur[3 if item % cur[2] == 0 else 4]][0].append(item)
            cnt[i] += len(cur[0])
            cur[0].clear()
    cnt.sort()
    return cnt[-1] * cnt[-2]

print(simulate(20))
print(simulate(10000))
