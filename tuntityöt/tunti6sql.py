import mysql.connector

def haekentta(nimi):
    sql = "select name, ident from airport where name like '%" + nimi + "%';"
    print(sql)
    kursori = mydb.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän kokonimi on {rivi[0]} ja sen ICAO on {rivi[1]}")
    return

mydb = mysql.connector.connect(
       host='localhost',
       port='3306',
       database='flight_game',
       user='root',
       password='5alattu',
       autocommit=True
       )
kentanNimi = input("Anna kentän nimi: ")
haekentta(kentanNimi)