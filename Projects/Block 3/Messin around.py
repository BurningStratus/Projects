import random

print("########################################")
print("Roulette. You win if you get number greater than 95.")

credit = float(random.randint(0, 100))

score = 0

print("########################################")
print(f"Your number is: {credit:6.0f}")

if credit >=95:
        print("You won!", f"Your score:  {score:6.0f}")
        score + 5
else:
        print("You lost!", f"Your score:  {score:6.0f}")
        score - 1
print("########################################")
