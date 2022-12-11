#!/usr/bin/env python3.11

def solve(iterations):
    cur, D = 0, 1
    starting, oper, divs, monkeys = {}, {}, {}, {0}
    for line in open('11.txt'):
        if "Monkey" in line:
            monkeys |= {cur:=int(line.split()[1][:-1])}
        elif "Starting" in line:
            starting[cur] = list(map(int, line.split(': ')[1].split(', ')))
        elif "Oper" in line:
            oper[cur] = eval(f"lambda old: {line.split(' = ')[1]}")
        elif "divisible" in line:
            i = int(line.split()[-1])
            D *= i
            divs[cur] = [i]
        elif "If" in line:
            i = int(line.split()[-1])
            divs[cur] += [i]

    cnt = [0] * len(monkeys)

    for _ in range(iterations):
        for cur in monkeys:
            div, true, false = divs[cur]
            while starting[cur]:
                new = oper[cur](starting[cur].pop())
                if iterations == 20:
                    new //= 3
                else:
                    new %= D
                x = (true, false)[new % div != 0]
                starting[x].append(new)
                cnt[cur] += 1
    cnt.sort()
    return cnt[-1] * cnt[-2]

print(solve(20))
print(solve(10000))
