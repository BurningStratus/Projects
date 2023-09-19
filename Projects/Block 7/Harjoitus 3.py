# prog has 5 functions: help, add, find, show, remove and exit: prog asks for airports names and their codes

airports = {}


def addtodict(group):  # function to add new records
    name = input("name of the airport: ")
    code = input("code of the airport: ")
    for i in group:     # func. checks if record with same code exists
        if group[i] == code:
            print(f"code [{code}] already exists")
            print(f"here -> {i} [{group[i]}]")
            return 0
    if name not in group:  # func. checks if name isnt in dictionary
        group[name] = code
        print("record added")
        return 0
    elif name in group:
        print("name or code already exist")
        print(f"here -> {name} [{group[name]}]")
        return 0
    else:
        return None


def remove(group):
    record = input("specify record to remove: ")
    if record in group:
        del group[record]
        print("record deleted")
    else:
        print("err: record not found")
    return None


def show(group):  # shows all records
    print("...retrieving records...")
    for i in group:
        print(f"{i} [{airports[i]}]")
    print("...all records listed...")
    return None


def find(group):  # find in database(easie thunn SQL)
    strng = input("find by name or code: ")
    for i in group:
        if strng == group[i]:
            print(f"{i} corresponds with [{strng}] ")
        elif i == strng:
            print(f"{strng} corresponds with [{group[i]}]")
        else:
            print(f"couldn't find record that corresponds with {strng}")
    return 0


def help_cmd():  # shows all commands and common usage
    print("Available prompts are:\nhelp\nadd\nremove\nshow\nfind\nexit")
    print("Usage: [command] + ENTER\n")
    return None


print(f'''
####@##############@#######%#########@############$####

Database of airports. Names and ICAO-codes are stored.
########//Type help to view list of commands.//########

###########$#########@##########$######%###############''')

cmd = input("command: ")
while cmd != "exit":  #  prog revolves functions util user types "exit"
    if cmd == "help":
        help_cmd()
        cmd = input("command: ")
    elif cmd == "add":
        addtodict(airports)
        cmd = input("command: ")
    elif cmd == "remove":
        remove(airports)
        cmd = input("command: ")
    elif cmd == "show":
        show(airports)
        cmd = input("command: ")
    elif cmd == "find":
        find(airports)
        cmd = input("command: ")
    else:
        print(f"err: not supported prompt '{cmd}'")
        cmd = input("command: ")
else:
    print("Bye")
