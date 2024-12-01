inp = list(map(str, open('02.in').readlines()))

# Part 1
horizontal = 0
depth = 0

for l in inp:
    x, i = l.split()
    i = int(i)
    if x == "forward":
        horizontal += i
    elif x == "up":
        depth -= i
    elif x == "down":
        depth += i

print(horizontal*depth)

# Part 2
horizontal = 0
depth = 0
aim = 0

for l in inp:
    x, i = l.split()
    i = int(i)
    if x == "forward":
        horizontal += i
        depth += aim*i
    elif x == "up":
        aim -= i
    elif x == "down":
        aim += i

print(horizontal*depth)
