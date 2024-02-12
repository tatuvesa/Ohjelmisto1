import mysql.connector
from geopy.distance import geodesic

def etaisyys(icaokoodi):
    sql = "select latitude_deg, longitude_deg from airport where ident like '%" + icaokoodi + "%';"
    kursori = mydb.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos is None:
        return None
    else:
        return tulos[0], tulos[1]

mydb = mysql.connector.connect(
       host='localhost',
       port='3306',
       database='flight_game',
       user='root',
       password='5alattu',
       autocommit=True
       )

def laskeetaisyys():

    nimi = input("Anna icao: ").upper()
    nimi2 = input("Anna toinen icao: ").upper()

    koordinaatti = etaisyys(nimi)
    koordinaatti2 = etaisyys(nimi2)

    if koordinaatti is None or koordinaatti2 is None:
        print("Icao-koodia tai koodeja ei löydy tietokannasta.")

    else:
        distance = geodesic(koordinaatti, koordinaatti2).kilometers
        print(f"Lentokenttien {nimi} ja {nimi2} välinen etäisyys on {distance:.2f} kilometriä.")

laskeetaisyys()