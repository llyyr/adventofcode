#!/usr/bin/env python3.11


inp = open('05.txt').read().split('\n\n')

def calc(mode):
    stacks = []
    for line in inp[0].split('\n'):
        if line.strip().startswith('1'):
            break
        for i, val in enumerate(line):
            if 'A' <= val <= 'Z':
                i = int((i - 1) // 4)
                while len(stacks) <= i:
                    stacks.append([])
                stacks[i].append(val)
    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]

    for line in inp[1].split('\n'):
        if not line: continue
        m = line.split()
        steps = [int(m[1]), int(m[3]), int(m[5])]
        if mode == 9000:
            for _ in range(steps[0]):
                stacks[steps[2]-1].append(stacks[steps[1]-1].pop())
        elif mode == 9001:
            temp = []
            for _ in range(steps[0]):
                temp.append(stacks[steps[1]-1].pop())
            stacks[steps[2]-1].extend(temp[::-1])

    print(''.join(ret[-1] for ret in stacks))

calc(9000)
calc(9001)
