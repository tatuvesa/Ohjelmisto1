import mysql.connector

def kentanicao(icao):
    sql = "select name, municipality from airport where ident like '%" + icao + "%';"
    kursori = mydb.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]} ja sen sijaintikunta on {rivi[1]}")
    return

mydb = mysql.connector.connect(
       host='localhost',
       port='3306',
       database='flight_game',
       user='root',
       password='5alattu',
       autocommit=True
       )
while True:

    nimi = input("Anna kentän ICAO-koodi: ").upper()

    if nimi == "":
        break

    kentanicao(nimi)

