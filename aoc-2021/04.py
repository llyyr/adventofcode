#!/usr/bin/env python3.9
from itertools import product

inp = open('04.txt').read().rstrip().split('\n\n')
nums = list(map(int, inp.pop(0).split(',')))
boards = []
for i in inp:
    board = list(list(map(int, line.split())) for line in i.split('\n'))
    boards += [board]

bingoed = [False]*len(boards)
solves = []
size = range(len(boards[0][0]))
for num in nums:
    for i in range(len(boards)):
        if bingoed[i]:
            continue
        total = 0
        bingo = False
        for col, row in product(size, repeat=2):
            if boards[i][col][row] == num:
                boards[i][col][row] = False
                if not sum(boards[i][col]) \
                        or not sum(boards[i][col][row] for col in size):
                    bingo = True
                    bingoed[i] = True
            else:
                total += boards[i][col][row]
        if bingo:
            solves += [total*num]

print(solves[0], solves[-1])
