# Modify dice thrower 1500 for it to ask the user the highest number and throw it

import random
import time
thr = 0
num = 0
most = int(input("How many sides does your dice have?: "))
def dicer():
    print("Throwing your dice...")
    time.sleep(0.8)
    dice = random.randint(1, most)
    print(f"I threw a dice and got {dice}")
    return dice

while num != most:
    num = dicer()
    thr += 1
    print(f"I threw a dice {thr} times already\n")
else:
    print(f"\nIt took me {thr} throws to get {most} from your dice.")