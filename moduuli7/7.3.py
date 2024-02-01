lentoasemat = {}

while True:
    valinta = input("Valitse (1: uusi lentoasema) (2: hae lentoasemaa) (3: lopeta): ")
    if valinta == "1":
        icao = str.upper(input("Syötä lentoaseman ICAO koodi: "))
        lentoasema = input("Lentoaseman nimi: ")
        lentoasemat[icao] = lentoasema

    elif valinta == "2":
        icao = str.upper(input("Syötä lentoaseman ICAO koodi: "))
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")