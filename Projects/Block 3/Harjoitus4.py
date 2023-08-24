year = float(input("Enter the year: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year:5.0f}", "Is a leap year.", sep="")
elif year % 4 == 0:
    print(f"{year:5.0f}", "Is a leap year.", sep="")
else:
    print(f"{year:5.0f}", "Is not a leap year.", sep=" ")
