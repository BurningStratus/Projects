
# DONE program asks for names until it receives "None"
# DONE whether name is already in a set, prog prints either "name exists" or "new name added"
# in the end it prints out everything from a set

names = {""}


def name_check(name, group):
    group = names
    if name not in group:
        group.add(name)
        print("Name added")
        return group
    elif name in group:
        print("Error: existing name")
        return group
    else:
        return group


name_inp = input("Insert name: ")
while name_inp != "":
    name_check(name_inp, names)
    name_inp = input("Insert name: ")
else:
    for i in names:
        print(i)
