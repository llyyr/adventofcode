#!/usr/bin/env python3.11

root = {'dirs': {}, 'files': {}, 'parent': None}
root_ = root

for l in [l.strip() for l in open('07.txt')]:
    l = l.split()
    match l:
        case ['$', 'cd', '/']: continue
        case ['$', 'ls']: continue
        case ['$', 'cd', '..']: root_ = root_['parent']
        case ['$', 'cd', *dirname]: root_ = root_['dirs'][*dirname]
        case ['dir', *l]: root_['dirs'][*l] = {'dirs': {}, 'files': {}, 'parent': root_}
        case other: root_['files'][l[1]] = int(l[0])

def compute(d):
    total = 0
    for subdir in d['dirs'].values():
        compute(subdir)
        total += subdir['size']
    for f in d['files'].values():
        total += f
    d['size'] = total
compute(root)

def part1(d):
    total = 0
    for subdir in d['dirs'].values():
        total += part1(subdir)
    if d['size'] < 100000:
        total += d['size']
    return total
print(part1(root))

bestrm = 1e9
def part2(d, k='/'):
    global bestrm
    for k, subdir in d['dirs'].items():
        part2(subdir, k)
    if d['size'] > 30000000 - (70000000 - root['size']):
        bestrm = min(d['size'], bestrm)
    return bestrm
print(part2(root))
