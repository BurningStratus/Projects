# def even_or_odd(num):
#     return "eovdedn"[num % 2:: 2]  # cursed
#
# print(even_or_odd(20))  # ?????
#
# print(even_or_odd(1))  # ??????
#

### prog which casts a dice.
import random

casted_dices = []


def dice_caster(side, dice):
    for i in range(dice):
        casted = random.randint(1, side)
        casted_dices.append(casted)
    return casted_dices


def avg_num(desired_list):

    freq_list = {}

    for outer in desired_list:
        freq = 0
        for inner in desired_list:
            if inner == outer:
                freq += 1
            else:
                pass
        freq_list[outer] = freq

    return freq_list


side_thrower = int(input("How much sides does your dice have?: "))
dice_thrower = int(input("How much dice you have?: "))

print(dice_caster(side_thrower, dice_thrower))

print(avg_num(casted_dices))
