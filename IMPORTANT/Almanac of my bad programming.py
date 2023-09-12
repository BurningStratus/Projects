# Almanac of bad programming.
# 1[MODIFYING GLOBAL VARIABLES]
# 2[IMPLICIT RETURN VALUE]


# 1[MODIFYING GLOBAL VARIABLES]

# When creating a function that needs to make/modify a list, don't modify the initial one.
# Create a new instead.
# It IS better to create a new list inside a function to add needed values there.

# This is an example of modifying a global variables, so the function is dependent on initial values.
# This is considered a bad programming, because code is difficult to debug and maintain.

# My mistakes here are:
# 1. I made a function which modified a global value
# 2. I made a function that wasn't self-contained
# 3. Function returned an implicit value(not a meaningful one)

# Bad sport ahead  --->
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # given list
def noprime(list_1):  # function to evaluate everything from the list_1.
    for i in list_1:
        if i % 2 == 0:
            list_1.remove(i) # noprime() modifies the existing list_1
    return list_1
"""
# End of bad sport <---

# 2[IMPLICIT RETURN VALUE]

# Inside a function, if function can't reach none of the conditions to return a reasonable RETURN value,
# it will return an implicit "return" value, which is " None ".
# Bad sport ahead  --->
"""
def my_abs(number):
    if number > 0:
        return number
    elif number < 0:
        return -number

print(my_abs(-15)) # This returns 15
print(my_abs(15))  # This returns 15 
print(my_abs(0))   # This returns None
"""
# End of bad sport <---
