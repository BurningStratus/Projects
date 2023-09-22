import mysql.connector
import random

print('''
#########################################################
# add entries to local database 'users' easy and simple.#
#                                                       #
#                                      BurningStratus   #
#########################################################
''')
usr = input("username: ")
if usr == "":
    usr = "root"
pasw = input("password: ")

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='users',
    user=usr,
    password=pasw,
    autocommit=True
)
cmd_m = None  # used to control adding more users while maintaining usability
cmd_u = None  # same as above but for machines


def random_ip():  # This makes up ips to add to database
    part1 = str(random.randint(0, 99))
    part2 = str(random.randint(0, 999))
    part3 = str(random.randint(0, 99))
    part4 = str(random.randint(0, 99))
    ip_rand = part1 + part3 + part4 + part2
    return ip_rand


def addto_machines(ident, machin, sys):  # adds entries to user_machines
    sql = "INSERT INTO user_machines(user_id, machine, system) "
    sql += f"VALUES({ident}, '{machin}', '{sys}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return "machine added"


def addto_users(user, fname, lname):  # adds users
    sql = "INSERT INTO user_details(username, first_name, last_name) "
    sql += f"VALUES('{user}', '{fname}', '{lname}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.fetchall()
    return "user added"


def upd_int_sql():  # used for automatically fetch the max id for easy addition of machines.
    sql = "SELECT max(user_machines.user_id), max(user_details.user_id) "
    sql += "from user_machines, user_details;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    d1 = 0
    d2 = 0

    for i in result:
        d1 = i[0] + 1
        d2 = i[1]
    if d2 == d1:  # notifies when id of user_machines = id of user_details.
        print("// error intercepted //")
        d1 = -1
        return d1
    else:
        print(f"id updated //{d1}")
        return d1

cmd = input("add machine/user: ")

while cmd != "stop":  # general loop
    if cmd == "machine":  # loop for asy addition of machines to database
        while cmd_m != "stop machine":
            id_sql = upd_int_sql()
            if id_sql < 0:
                print("add more users")
                break

            machine = random_ip()
            system = input("system: ")
            print(addto_machines(id_sql, machine, system))

            cmd_m = input("continue/stop machine: ")

        cmd = input("add machine/user: ")
    elif cmd == "user":  # loop for easy addition of users to database
        while cmd_u != "stop user":

            new_username = input("username: ")
            first_name_n = input("first name: ")
            last_name_n = input("last name: ")

            print(addto_users(new_username, first_name_n, last_name_n))

            cmd_u = input("continue/stop user: ")

        cmd = input("add machine/user: ")
    elif cmd == "help":
        print("available prompts are: machine/user , stop machine|user, stop")
else:
    print("Bye")
