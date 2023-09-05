
num = input("Give number: ")
num = int(num)
isprime = True

for i in range(2, num):
    if num % i == 0:
        isprime = False
        break
if isprime == True:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
