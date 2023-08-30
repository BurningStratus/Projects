# Program should give 2 random codes:
# 3-digit codes which each number vry 0-9
# 4-digit codes which each number vry 1-6

# random.int(a, b, c)

import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)

print("This program gives two random codes.")
print("3-Digit random code: ", digit1, digit2, digit3)

dig1 = random.randint(1, 6)
dig2 = random.randint(1, 6)
dig3 = random.randint(1, 6)
dig4 = random.randint(1, 6)

print("4-Digit random code: ", dig1, dig2, dig3, dig4)
