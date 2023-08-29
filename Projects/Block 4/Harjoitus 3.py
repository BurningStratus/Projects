
num = input("Number: ")

bnum = 0
lnum = 0

while num != "":
    num = int(num)

    if num > bnum:
        bnum = num
        print("BUCK", bnum)

    elif num < bnum:
        lnum = num
        print("NUMB", num)
    num = input("Number: ")

else:
    print(bnum, lnum)