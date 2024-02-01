nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Nimi on jo syötetty")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)