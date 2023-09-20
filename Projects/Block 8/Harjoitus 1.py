import mysql.connector
import time
import random
delay = random.uniform(1,3)
delay1 = random.uniform(2,4)

username = input("username: ")
if username == "":
    username = "root"
password = input("password: ")

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='flight_game',
    user= username ,
    password= password,
    autocommit=True
)

def find_with_icao(number):
    sql = "select name, iso_region  from airport where ident = '" +  number + "'"
    time.sleep(delay)
    print(f"executing SQL prompt... \n{sql}...")
    time.sleep(delay1)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        time.sleep(delay)
        print(f"ICAO [{number}] corresponds with {i[0]} which is located in {i[1]}")

icao = input("Insert ICAO code: ")
find_with_icao(icao)
