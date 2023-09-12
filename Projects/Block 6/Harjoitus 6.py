#  DONE program which takes radiuses and prices of two pizzas
#  DONE it calculates the price/size ratio
#  DONE it compares both and says which one is a better deal

import math


def pizza_pricetosize(radius, price):
    if radius == 0 or price == 0:
        return 0
    area = math.pi * (radius/100) ** 2
    ratio = price / area
    return ratio


def compare(ratio1, ratio2):
    if ratio1 < ratio2:
        return 1
    elif ratio1 > ratio2:
        return 2
    else:
        return 0


radius_1 = int(input("Insert the radius of the first pizza(cm): "))
pizza_price1 = float(input("Insert the price of the first pizza($): "))

radius_2 = int(input("Insert the radius of the second pizza(cm): "))
pizza_price2 = float(input("Insert the price of the first pizza($): "))

rt1 = pizza_pricetosize(radius_1, pizza_price1)
rt2 = pizza_pricetosize(radius_2, pizza_price2)

if compare(rt1, rt2) == 1:
    print(f"First pizza is a better deal.({rt1:.2f} $/m^2)")
elif compare(rt1, rt2) == 2:
    print(f"Second pizza is a better deal.({rt2:.2f} $/m^2)")
else:
    print("It's the same.")
