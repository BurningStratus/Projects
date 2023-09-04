import random

print("\nGuess the number. Think twice: you only have 3 tries!\n")

gmb = random.randint(1, 10)

tries = 3
print(f"Tries left: {tries}")
gss = int(input("Your guess> "))


tries = tries - 1

while tries > 0 and gss != gmb:

    if gss < gmb:
#        #print(gmb)
        print("Not enough!")
        print(f"Tries left: {tries}")
        tries = tries - 1

    elif gss > gmb:
#        print(gmb)
        print("Too much!")
        print(f"Your tries: {tries}")
        tries = tries - 1

    gss = int(input("Your guess> "))

if gss == gmb :
    print('You win!')
else:
    print('You lose!')
