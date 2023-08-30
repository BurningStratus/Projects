import random

nnumber = int(input("Amount of random points: "))

rev = 0
hit = 0

while rev <= nnumber:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    while x ** 2 + y ** 2 < 1:
        hit = hit + 1
        break
    rev = rev + 1

pi = 4 * hit / nnumber

print(pi)