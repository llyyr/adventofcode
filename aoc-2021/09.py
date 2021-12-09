#!/usr/bin/env python3.10
inp = [[*map(int, l.rstrip())] for l in open(0)]

def solve():
    R = len(inp)
    C = len(inp[0])
    ans = 0

    Q = []
    for r in range(R):
        for c in range(C):
            p = inp[r][c]
            m = True
            for rr, cc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0<=cc<C and 0<=rr<R and inp[rr][cc]<=p:
                    m = False
            if m:
                Q.append((r, c))
                ans += p + 1
    print(ans)

    B = []
    SEEN = [[False] * C for _ in range(R)]
    while Q:
        r, c = Q.pop()
        NQ = [(r, c)]
        SEEN[r][c] = True
        for r, c in NQ:
            for rr, cc in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):
                if 0<=cc<C and 0<=rr<R and inp[rr][cc]!=9 and not SEEN[rr][cc]:
                    SEEN[rr][cc] = True
                    NQ.append((rr, cc))
        B.append(len(NQ))

    B.sort()
    a, b, c = B[-3:]
    print(a*b*c)
solve()
