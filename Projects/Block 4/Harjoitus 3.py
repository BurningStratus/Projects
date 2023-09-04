
num = input("Number: ")

bnum = 0
lnum = 0

while num != "":
    num = int(num)

    if num < lnum:
        lnum = num
        print("NUMB", num)

    elif num > bnum:
        bnum = num
        print("BUCK", bnum)
    num = input("Number: ")
else:
    print(bnum, lnum)