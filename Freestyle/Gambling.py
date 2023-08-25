# Guess the number
import random

print("Guess the number from 0 to 9")

gss = float(input("Insert number: "))
num = random.randint(0, 9)

if gss == num:
    print("You win!")
elif gss > 9 or gss < 0:
    print("I said from 0 to 9, you idiot!")
elif gss != num:
    print("You lost!")
    print(num)
