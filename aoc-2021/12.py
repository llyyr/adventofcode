#!/usr/bin/env python3.10
graph = {}
for l in open(0):
    a, b = l.rstrip().split('-')
    graph[a] = graph.get(a, set()) | set([b])
    graph[b] = graph.get(b, set()) | set([a])

def solve(p1=False):
    Q = [('start', set(['start']), None)]
    paths = 0
    while Q:
        node, path, twice = Q.pop()
        if node == 'end':
            paths += 1
            continue
        for n in graph[node]:
            if n not in path:
                new_path = path | {n} if n.islower() else path
                Q.append((n, new_path, twice))
            elif not p1 and n in path and twice is None and len(n) == 2:
                Q.append((n, path, n))
    return paths

print(solve(True))
print(solve())

