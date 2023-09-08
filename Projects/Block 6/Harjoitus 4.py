# function, which gets a list of integers
# global prog which sums up all nums from a user-defined list
userlist = []


def summ_sum(user_list):  # function to evaluate everything from user-def. a list
    summ = 0
    for i in user_list:
        summ = summ + i
    print(f"The sum of all parts of the list equals: {summ}.")
    return summ


sum_list = input("Integer: ")
# "While" for user to define a list
while sum_list != "":
    sum_list = int(sum_list)
    userlist.append(sum_list)
    print(userlist)
    sum_list = input("Integer: ")
else:
    print(f"User-defined list is {userlist}.")
# calling a function and calculating results.
summ_sum(userlist)