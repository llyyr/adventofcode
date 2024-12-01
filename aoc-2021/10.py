#!/usr/bin/env python3.10
def solve():
    m = {'(': ')', '{': '}', '[': ']', '<': '>'}
    scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    scores2 = {')': 1, ']': 2, '}': 3, '>': 4}

    score1 = 0
    line_scores = []
    for l in open(0):
        stack = []
        for ch in l.rstrip():
            if ch in m:
                stack.append(m[ch])
            elif ch == stack[-1]:
                stack.pop()
            else:
                score1 += scores1[ch]
                break
        else:
            score2 = 0
            while stack:
                score2 = score2 * 5 + scores2[stack.pop()]
            line_scores.append(score2)

    line_scores.sort()
    median = len(line_scores)//2
    print(score1, line_scores[median])
solve()
