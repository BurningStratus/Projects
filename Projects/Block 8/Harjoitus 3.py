#  Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
#  Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
#  Laskenta perustuu tietokannasta haettuihin koordinaatteihin.

#  prog asks for 2 icao codes
#  prog calculates distance between both based on coordinates

import mysql.connector
import geopy
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='flight_game',
    user= "root" ,
    password= "cr1ng3",
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
    print(latd)
    return latd


def retriever_long(icao):
    sql = "SELECT longitude_deg FROM airport "
    sql += "where ident = '" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        longd = i[0]
    print(longd)
    return longd


icao_1 = input("ICAO1: ")
latitude_1 = retriever_lat(icao_1)
longitude_1 = retriever_long(icao_1)

place_1 = (latitude_1, longitude_1)

icao_2 = input("ICAO2: ")
latitude_2 = retriever_lat(icao_2)
longitude_2 = retriever_long(icao_2)

place_2 = (latitude_2, longitude_2)

print(distance.distance(place_1, place_2).kilometers)