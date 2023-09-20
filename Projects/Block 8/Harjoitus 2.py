import mysql.connector

# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database='flight_game',
    user= "root" ,
    password= "red_banana",
    autocommit=True
)

def find_bycountry_code(code):
    sql = "SELECT country.name, airport.type, count(*) FROM country, airport WHERE"
    sql += " country.iso_country = airport.iso_country AND airport.iso_country = '" + code + "'"
    sql += " GROUP BY airport.type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(f"country: {i[0]} type: {i[1]} amount: {i[2]}")

codes = input("Country code: ")
find_bycountry_code(codes)