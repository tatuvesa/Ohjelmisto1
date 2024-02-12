import mysql.connector

def kentanicao(maakoodi):
    sql = "select type, count(type) from airport where iso_region like '%" + maakoodi + "%' group by type;"
    kursori = mydb.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän tyyppi on {rivi[0]} ja niitä on {rivi[1]}")
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

    nimi = input("Anna maakoodi: ").upper()

    if nimi == "":
        break

    kentanicao(nimi)

