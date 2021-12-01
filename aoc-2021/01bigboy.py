import random
random.seed(2021)
total = int(100**100)

with open('bigboy.in', 'w') as f:
    for i in range(total+1):
        f.write(str(random.randint(100, 100+total)) + '\n')
