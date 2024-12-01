inp = list(map(int, open('01.in').readlines()))

count = 0
for i in range(1, len(inp)):
    if inp[i] > inp[i-1]:
        count +=1

print("Part 1: ", count)

count = 0
cumsum = sum(inp[:3])
for i in range(1, len(inp)-2):
    cumsum2 = inp[i] + inp[i+1] + inp[i+2]
    if cumsum2 > cumsum:
        count += 1
    cumsum = cumsum2

print('Part 2: ', count)

