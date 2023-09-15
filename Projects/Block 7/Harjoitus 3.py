# prog has 3 functions: help, add new, find existing and end: prog asks for airports names and their codes

airports = {}


def addtodict(group):  # function to add new records
    name = input("name of the airport: ")
    code = input("code of the airport: ")
    if name not in group and code not in group:
        group[name] = code
        print("record added")
        return group
    elif name in group or code in group:
        print("name or code already exists")
        print(group[name])
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
    return 0


def help_cmd():  # shows all commands and common usage
    print("Available prompts are:\nhelp\nadd\nshow\nfind\nexit")
    print("Usage: [command] + ENTER\n")
    return None

print("####@##############@#######%#########@############$###\n")
print("Database of airports. Names and ICAO-codes are stored.")
print("########//Type help to view list of commands.//########\n")
print("###########$#########@##########$######%###############")

cmd = input("command: ")
while cmd != "exit":  # executable to revolve functions
    if cmd == "help":
        help_cmd()
        cmd = input("command: ")
    elif cmd == "add":
        addtodict(airports)
        cmd = input("command: ")
    elif cmd == "show":
        show(airports)
        cmd = input("command: ")
    elif cmd == "find":
        find(airports)
        cmd = input("command: ")
    else:
        print("err: not supported prompt")
        cmd = input("command: ")
else:
    print("Bye")
