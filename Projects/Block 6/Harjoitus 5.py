# function, which gets a list of integers
# global prog which deletes all non-prime numbers.

#for luku_jota_vastaan_testataan in range(3, luku_jota_testataan - 1):

userlist = []


def noprime(user_list):  # function to evaluate everything from a user-def. list
    nooprime = []
    for i in user_list:
        if i % 2 == 0:
            nooprime.append(i)
    return nooprime


sum_list = input("Integer: ")
# "While" for user to define a list
while sum_list != "":
    sum_list = int(sum_list)
    userlist.append(sum_list)
    print(userlist)
    sum_list = input("Integer: ")

print(userlist)
print(f"User-defined list without odd numbers:\n{noprime(userlist)}.")

#  https://realpython.com/python-return-statement/#returning-vs-printing