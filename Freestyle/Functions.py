
# def dude():
#     print("\nDude: Damn, here I was minding my own business, but you people had to freak out on me.")
#     return
# def dude1():
#     print("\nDude: You think second amendment covers this?")
# dude()
# dude1()

# howmuch = int(input("Insert number> "))
# def greetings(howmuch):
#     for i in range(howmuch):
#         print (f"Vault Tech's been calling for {i+1} times already!")
#     return
#
# print ("Didn't you hear?")
# greetings(howmuch)
#
#
# print("\nDamn, these marketers are out of hand!\n")
# greetings(howmuch-2)

# def vaihda():
#     kaupunki = "Vantaa"
#     print("Toisessa Funktiossa on: " + kaupunki)
#     return
# def notvaihda():
#     kaupunki = "Espoo"
#     print("Toisella funktiolla on: " + kaupunki)
#
# kaupunki = "Helsinki"
#
# notvaihda()
# vaihda()
# print("Globaalimuuttujalla on: " + kaupunki)

import random
import math
# word = input("What's on your mind?: ")
# amnt = random.randint(1,3000)
# def swearing(word, amnt):
#     for i in range(amnt):
#         print(word, amnt)
#         return
#
# swearing(word, amnt)

# def mid(a, b):
#     mdd = (a + b)/2
#     return mdd
#
# num1 = float(input("Number 1: "))
# num2 = float(input("Number 2: "))
# res = mid(num1, num2)
# print(f"The middle ground of {num1:.2f} and {num2:.2f} is {res:.2f}")

def invt(crap):
    print("You got these things: ")
    for c in crap:
        print("> " + c)
    crap.clear()
bag2 = ["M1-GARAND", "AK-47", "1911", "LUGER", "STB-120", "MARK TWAIN"]
invt(bag2)
bag2.append("Desert Eagle")
invt(bag2)
