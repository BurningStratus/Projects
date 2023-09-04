import random

nnumber = int(input("Amount of random points: "))
print("working...")
rev = 0
hit = 0

while rev <= nnumber:

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        hit += 1
    rev += 1

pi = 4 * hit / nnumber

print(f"The pi is: {pi}")

