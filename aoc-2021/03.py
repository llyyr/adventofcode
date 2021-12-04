inp = [l.rstrip() for l in open('03.txt')]
W = len(inp[0])

# Part 1
p = q = ''
for i in range(W):
    k = [x[i] for x in inp]
    p += '1' if k.count('1') > len(k)//2 else '0'
    q += '0' if k.count('1') > len(k)//2 else '1'

print(int(p, 2) * int(q, 2))

# Part 2
oxy = car = list(inp)
for i in range(W):
    koxy = [x[i] for x in oxy]
    kcar = [x[i] for x in car]
    if len(oxy) > 1:
        if koxy.count('0') <= koxy.count('1'):
            oxy = [x for x in oxy if x[i] == '1']
        else:
            oxy = [x for x in oxy if x[i] == '0']
    if len(car) > 1:
        if kcar.count('0') > kcar.count('1'):
            car = [x for x in car if x[i] == '1']
        else:
            car = [x for x in car if x[i] == '0']

print(int(oxy[0], 2) * int(car[0], 2))
