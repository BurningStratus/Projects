# function, which gets a list of integers
# global prog which deletes all non-prime numbers.

#for luku_jota_vastaan_testataan in range(3, luku_jota_testataan - 1):

userlist = []


def noprime(user_list):  # function to evaluate everything from a user-def. list
    #  user_list.sort()
    for i in user_list:
        if i % 2 != 0:
            user_list.remove(i)

    return user_list
        # elif i % 2 == 1:
        #     user_list.remove(i)


sum_list = input("Integer: ")
# "While" for user to define a list
while sum_list != "":
    sum_list = int(sum_list)
    userlist.append(sum_list)
    print(userlist)
    sum_list = input("Integer: ")

# calling a function and calculating results.
print(userlist)

noprime(userlist)

print(f"User-defined list without non-prime numbers:\n{userlist}.")

#  https://realpython.com/python-return-statement/#returning-vs-printing