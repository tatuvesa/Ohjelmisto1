import mysql.connector

def haekentta(nimi):
    sql = "select name, ident from airport where name like '%" + nimi + "%';"
    kursori = mydb.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän kokonimi on {rivi[0]} ja sen ICAO on {rivi[1]}")
    return
def hae(sql):
    kursori = mydb.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

mydb = mysql.connector.connect(
       host='localhost',
       port='3306',
       database='flight_game',
       user='root',
       password='5alattu',
       autocommit=True
       )
while True:
    print("1: kentän suppeat tiedot.")
    print("2: kentän laajat tiedot.")
    print("Jätä kenttä tyhjäksi poistuaksesi.")

    kentanNimi = input("Anna kentän nimi: ")
    valinta = input("Valitse 1 tai 2: ")

    if valinta == "1":
        haekentta(kentanNimi)

    elif valinta == "2":
        sql = "select ident, airport.name, country.name from airport, country where airport.iso_country = country.iso_country and airport.name like '%" + kentanNimi + "%';"
        tulos = hae(sql)
        for rivi in tulos:
            print(rivi[0], rivi[1], rivi[2])

    elif valinta != "1" and valinta != "2" or kentanNimi == "":
        break

    else:
        print("Virheellinen syöte.")