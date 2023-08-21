print("This sumple program will show product, sum and mid value of three numbers.")
number1_raw = input("Number 1: ")
number2_raw = input("Number 2: ")
number3_raw = input("Number 3: ")

num1 = float(number1_raw)
num2 = float(number2_raw)
num3 = float(number3_raw)

prod = num1 * num2 * num3
summ = num1 + num2 + num3
midd = summ/3

print("Prod: " + str(prod))
print("Sum: " + str(summ))
print("Mid: " + str(midd))