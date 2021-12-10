#!/usr/bin/env python3.10
m = {'(': ')', '{': '}', '[': ']', '<': '>'}
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {')': 1, ']': 2, '}': 3, '>': 4}

score1 = 0
line_scores = []
for l in open(0):
    open_check = []
    for ch in l.rstrip():
        if ch in m:
            open_check.append(m[ch])
        elif ch == open_check[-1]:
            open_check.pop()
        else:
            score1 += scores1[ch]
            break
    else:
        score2 = 0
        while open_check:
            score2 = score2 * 5 + scores2[open_check.pop()]
        line_scores.append(score2)

line_scores.sort()
median = len(line_scores)//2
print(score1, line_scores[median])

