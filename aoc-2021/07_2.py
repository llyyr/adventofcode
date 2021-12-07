inp = sorted(map(int, next(open(0)).split(',')))

median= inp[len(inp)//2]
p1 = sum(abs(i-median) for i in inp)

mean = sum(inp) // len(inp)
C2 = lambda x: (x*(x+1))//2
p2 = sum(C2(abs(i-mean)) for i in inp)

print(p1, p2)
