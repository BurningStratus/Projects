import random
print("This program uses random numbers to get both 6s with two dices.")
d1 = d2 = thr = 0
while d1 != 6 or d2 != 6:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    thr = thr + 1
if thr > 100:
    print(f"It took {thr:3.0f} throws to get both 6s.")
elif thr > 9:
    print(f"It took {thr:2.0f} throws to get both 6s.")
elif thr <= 9:
    print(f"It took {thr:1.0f} throws to get both 6s.")