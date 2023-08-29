import random

print("\nGuess the number. Think twice: you only have 3 tries!\n")

gmb = random.randint(1, 10)

print(gmb)

gss = int(input("Your guess> "))

tries = 2

while tries > 0 and gss != gmb:

    if gss < gmb:
        print(gmb)
        print("Not enough!")
        print(tries)
        tries = tries - 1

    elif gss > gmb:
        print(gmb)
        print("Too much!")
        print(tries)
        tries = tries - 1

    gss = int(input("Your guess> "))

if gss == gmb :
    print('you win')
else:
    print('you f***ing looser')
