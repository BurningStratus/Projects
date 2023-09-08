# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

#  function w/ no parameter, which throws dice
#  global program which throws dice until it gets 6
#  global program shows all attempts and nums it got

import random
import time
thr = 0
num = 0
def dicer():
    print("Throwing dice...")
    time.sleep(1.4)
    dice = random.randint(1,6)
    print(f"I threw a dice and got {dice}")
    return dice

while num != 6:
    num = dicer()
    thr += 1
    print(f"I threw a dice {thr} times already\n")
else:
    print(f"\nIt took me {thr} throws to get six.")