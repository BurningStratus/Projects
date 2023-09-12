# Almanac of bad programming.

# 1.[MODIFYING GLOBAL VARIABLES]
# When creating a function that needs to make/modify a list, don't modify the initial one.
# Create a new instead.

# This is an example of modifying a global variables, so the function is dependent on initial values.
# This is considered a bad programming, because code is difficult to debug and maintain.
# Also it IS better to create a new list inside a function to add needed values there.
# Bad sport ahead    --->
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def noprime(list_1):  # function to evaluate everything from a list.
    for i in list_1:
        if i % 2 == 0:
            list_1.remove(i)
    return list_1

# End of bad sport 1.<---

