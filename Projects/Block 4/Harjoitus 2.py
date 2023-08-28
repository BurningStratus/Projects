print("Convert Inches to Centimetres")

inch = float(input("Inches: "))

while inch > 0:
    cm = inch * 2.54
    print(inch, '"', '>>', f"{cm:3.1f}", "cm")
    inch = float(input("Inches: "))
else:
    print("Invalid number!")
