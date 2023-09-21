#  prog asks for 2 icao codes
#  prog calculates distance between both based on coordinates

import mysql.connector

from geopy import distance

print("This program calculates the distance between airports using their ICAO - codes.\n")
print("Enter username and password to your localhost. Leave username blank to use 'root'\n")

username = input("username: ")
if username == "":
    username = "root"
passcode = input("password: ")
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='flight_game',
    user= username ,
    password= passcode,
    autocommit=True
)


def retriever_lat(icao):
    sql = "SELECT latitude_deg FROM airport "
    sql += "where ident = '" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        latd = i[0]
    # print(latd)
    return latd


def retriever_long(icao):
    sql = "SELECT longitude_deg FROM airport "
    sql += "where ident = '" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        longd = i[0]
    # print(longd)
    return longd


icao_1 = input("ICAO1: ")
latitude_1 = retriever_lat(icao_1)
longitude_1 = retriever_long(icao_1)

place_1 = (latitude_1, longitude_1)

icao_2 = input("ICAO2: ")
latitude_2 = retriever_lat(icao_2)
longitude_2 = retriever_long(icao_2)

place_2 = (latitude_2, longitude_2)

print(f"Distance between {icao_1} and {icao_2} is {distance.distance(place_1, place_2).kilometers:.2f} km.")
