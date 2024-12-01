from _collections import _count_elements as C

#cipher = {49: 8, 37: 5, 34: 2, 39: 3, 25: 7, 45: 9, 41: 6, 30: 4, 42: 0, 17: 1}

def solve():
    MAP = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg',
           6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}
    C(counts:={}, ''.join(MAP.values()))
    cipher = {sum(counts[c] for c in v): k for k, v in MAP.items()}
    ans = 0
    for x, y in [x.split(' | ') for x in open(0)]:
        C(cnt:={}, x)
        res = [cipher[sum(map(lambda n: cnt[n], list(c)))] for c in y.split()]
        ans += 1000 * res[0] + 100 * res[1] + 10 * res[2] + res[3]
    print(ans)

solve()
