#!/usr/bin/env python3.10
from functools import cache

inp = open(0).read().splitlines()

# Implemented according to instructions, unused.
def sim(inp, num):
    store = {x: 0 for x in 'wxyz'}
    for l in inp:
        l = l.split()
        if l[0] == 'inp':
            store[l[1]] = num.pop(0)
            continue
        op, a, b = l
        b = store[b] if b in store else int(b)
        if op == 'add':
            store[a] += b
        elif op == 'mul':
            store[a] *= b
        elif op == 'div':
            store[a] //= b
        elif op == 'mod':
            store[a] %= b
        elif op == 'eql':
            store[a] = int(store[a] == b)
        else:
            assert False, l
    return store['z'] == 0

# This was never going to work but I tried anyway.
def bruteforce():
    def count():
        for i in range(int('9'*14), 0, -1):
            if '0' not in str(i):
                yield i
    for number in count():
        num = [int(x) for x in str(number)]
        if sim(inp, num):
            return num

# The input can be seen as 14 blocks of instructions, separated by 'inp' ops,
# the values in Ax, Ay and Dz are the only difference between each repititon.
# For example, consider the following block of instructions:
#    inp w        | w = input
#    mul x 0     \
#    add x z      | set x to be z % 26
#    mod x 26    /
#    div z {Dz}   | 'div z' is only present once in every block
#    add x {Ax}   | x += Ax, and we already set x = z % 26
#    eql x w      | check CONDITION 1: (w == z % 26 + Ax)
#    eql x 0      | check CONDITION 2: (w != z % 26 + Ax)
#    mul y 0     \
#    add y 25     | y is either 26 or 1, depending on CONDITION {1, 2}
#    mul y x      | because they set x to be either 1 or 0 and we multiply
#    add y 1     /  by that value, then add +1. So y = 25+1 or 0+1.
#    mul z y      | depending on CONDITION {1, 2}, set z = z*26 or z
#    mul y 0     \
#    add y w      | set y = (w + Ay) or 0,
#    add y {Ay}   | depending on CONDITION {1, 2}
#    mul y x     /
#    add z y      | set z = y or z, i.e. set z = (w + Ay) or z, depending on
#                 | CONDITION 1 and CONDITION 2
# As such, we can generalize the rest of the instructions, while only keeping
# the values that change across each block.
inpcnt = 0
Ax, Ay, Dz, limitZ = [], [], [], []
for i in range(len(inp)):
    if 'inp' in inp[i]:
        inpcnt += 1
        continue
    op, a, b = inp[i].split()
    b = int(b) if b not in 'wxyz' else b
    if op == 'add' and a == 'x' and b != 'z':
        Ax.append(b)
    elif op == 'add' and a == 'y' and inp[i-1] == 'add y w':
        Ay.append(b)
    elif op == 'div' and a == 'z':
        Dz.append(b)
        limitZ.insert(0, 26**Dz.count(1))

# As there are only 14 blocks in every input (I think), we do a sanity check.
# Changed later to be generalized for any input.
assert len(Ax) == len(Ay) == len(Dz) == len(limitZ) == inpcnt

# For my input:
# BLOCK: 0   1   2   3   4    5    6   7   8   9  10  11   12  13
# Ax = [14, 14, 14, 12, 15, -12, -12, 12, -7, 13, -8, -5, -10, -7]
# Ay = [14,  2,  1, 13,  5,   5,   5,  9,  3, 13,  2,  1,  11,  8]
# Dz = [ 1,  1,  1,  1,  1,  26,  26,  1, 26,  1, 26, 26,  26, 26]
#
# It's important to keep track of the following characteristics of the puzzle:
#  > w is user input. x and y registers are multiplied by 0 at the start of each
#  > block, i.e., they're reset. Only the value of the z register is carried
#  > to the next block of instructions.
#
#  > Dz is always either 1 or 26, determined by whether Ax is +ve or -ve.
#
#  > (Ax < 0 or Ax > 9) is always True. And there are always equal amount of
#  > blocks of negative and positive Ax. My input has 14 total blocks, and
#  > 7 positive Ax as well as 7 negative Ax.
#
# With the information we have, each block can be generalized as such:
#  > Read an input to w
#  > x == z % 26 + Ax
#  > set z //= 26 if Ax is negative (or Dz is 26).
#  > CONDITION 1: w == x
#  > if CONDITION 1 is not met, set z = z*26 + w + Ay. Otherwise, do nothing.
# run_block is the implementation of these rules.
def run_block(block, z, w):
    x = (z % 26) + Ax[block]
    z //= Dz[block]
    if w != x:
        z = z*26 + w + Ay[block]
    return z

# limitZ is a list that keeps track of the maximum possible value of z
# per block of instructions that can still reach 0 at the end.
# We know that the value of z is divided by either 1 or 26, therefore we can
# generalize limitZ to be 26**7 where 7 is the count of 1s in my Dz. However,
# it's possible to have even stricter limitations on Z by building limitZ list
# per input block. Every block only has one 'div z ' line, therefore
# we can read through them and build a list for the Z limit for each block.
# For my input:
# limitZ = [8031810176, 8031810176, 8031810176, 8031810176, 8031810176, 
#    308915776, 308915776, 11881376, 11881376, 11881376, 456976, 17576, 676, 26]
# z has to be 26**1 before block 14, 26**2 before block 13 and so on.
# We start with 26**x where x = 1.
# Then increment x everytime we read a block with 'div z 1' and prepend to list.
# This is the most important thing to notice, besides generalizing each block.
# Everything else can be considered speedups, but having strict limits for Z
# reduces runtime almost 10 times.
#
# There are multiple ways to solve this from here. One such way is as follows:
# We can note that if Ax is positive, it's always greater than 9 and the largest
# possible w we can have is 9, so it's impossible to meet the condition if w
# is a positive number. If we assume z as a stack of ints in a base26 number,
# we can think of the problem as such:
#  > if Ax > 0, push w + Ay into the stack
#
#  > if Ax < 0, pop from stack. If popped_value + Ax != w, then push w + Ay
#  > into the stack. Repeat until the stack (z) is empty (0).
#
# So for my input, we have the following blocks for Ax and Ay.
# Ax = [14, 14, 14, 12, 15, -12, -12, 12, -7, 13, -8, -5, -10, -7]
# Ay = [14,  2,  1, 13,  5,   5,   5,  9,  3, 13,  2,  1,  11,  8]
#
# This can be translated as the following:
#  > push,  w1 + 14
#  > push,  w2 + 2
#  > push,  w3 + 1
#  > push,  w4 + 13
#  > push,  w5 + 5
#  > pop,   w6 == popped_value-12
#  > pop,   w7 == popped_value-12
#  > push,  w8 + 9
#  > pop,   w9 == popped_value-7
#  > push, w10 + 13
#  > pop,  w11 == popped_value-8
#  > pop,  w12 == popped_value-5
#  > pop,  w13 == popped_value-10
#  > pop,  w14 == popped_value-7
#
# For all the pops to succeed, we can infer that:
#  >  w6 =  w5 - 7
#  >  w7 =  w4 + 1
#  >  w9 =  w8 + 2
#  > w11 = w10 + 5
#  > w12 =  w3 - 4
#  > w13 =  w2 - 9
#  > w14 =  w1 + 7
#
# From here, solving for a number in the form w1+w2+w3...+w14 is trivial.

# Another way to solve is with the following function. With all the information,
# we can bruteforce with strict constraints and get the result in less than 4s.
# Most important optimization is having a limit to the value of Z per block.
# We can also set the value of w to a specific number, instead of range(1, 10)
# because we know the relation between x and w.
@cache
def solve(z=0, block=0, Ws=range(1,10)):
    if block >= inpcnt or z > limitZ[block]:
        if z == 0:
            return ['']
        return ''
    x = (z % 26) + Ax[block]
    if x in Ws:
        Ws = (x,)
    nums = []
    for w in Ws:
        next_z = run_block(block, z, w)
        next_block = solve(next_z, block+1)
        for c in next_block:
            nums += [f'{w}{c}']
    return nums

nums = solve()
maxnum, minnum = max(nums), min(nums)
assert sim(inp, [int(c) for c in maxnum]) and sim(inp, [int(c) for c in minnum])
print(f'Part 1: {maxnum}\nPart 2: {minnum}')
