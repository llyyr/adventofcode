#!/usr/bin/env python3.11

sol = sorted(sum(int(line) for line in part.splitlines()) for part in open(0).read().split('\n\n'))

print(sol[-1])

print(sum(sol[-3:]))
