#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.

import random
print("######################################################\nDice throw" 
      "\n######################################################")
amnt = int(input("how many dices shall we throw?: "))
mem = []
print("throwing dices...")

for amnt in range(amnt):
    val = random.randint(1,6)
    mem.append(val)
print("counting results...")
summ = sum(mem)

print(summ)