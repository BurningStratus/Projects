#  func, which gets gas in USgal and converts it to Liters
#  program which asks gas in USgal and converts 'em to Ls
#  program operates until it gets negative values. 1 gal = 3.785 L

def conv(us_gal):
    liter = us_gal * 3.785
    return liter

gal = float(input("Enter amount of gas in US gallons: "))

while gal >= 0:
    liters = conv(gal)
    print(f"{gal:.2f} US gallons is the same as {liters:.2f} liters of gas.\n")
    gal = float(input("Enter amount of gas in US gallons: "))
else:
    print("Bye")