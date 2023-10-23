
# Tuple
"""
suspects = ("George Clown", "Usama Bin Laden", "Dmitry Puchkov", "Peter Parker", "Nikolay Komarov", "Aleksei Shevtsov")
print(suspects)
qstn = int(input("Who stole the shit?(1-6): "))

answer = suspects[qstn-1]

print(f"{answer} stole the shit.")
 """
import random


# def throw():
#     fist, sec = random.randint(1, 6), random.randint(1, 6)
#     return fist, sec
#
#
# dice1, dice2 = throw()
# print(f"You got {dice1} and {dice2}.")
#
# Set

# games = {"Chess", "Durak", "Checkers"}
# print(games)
# games.add("Dominion")
# print(games)
#
# games.remove("Checkers")
# print(games)
#
# games.add("Mafia")
# print(games)
# for g in games:
#     print(g)

names = {"Aleksei": "+721 123 34 52",
        "Gary": "+1 943 234 90 41",
        "Jack": "+358 560 37 82",
        "Nikolai": "+760 952 31 99"}


names["Natalia"] = "050-1011012"
print(names)
name = input("Name: ")
if name in names:
    print(f"{name}'s phone number is: {names[name]}")