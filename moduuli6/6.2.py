import random
def paaohjelma():
    tahkot = int(input("Syötä tahkojen määrä: "))
    suurinsilmaluku = int(input("Syötä maksimi silmäluku: "))
    while True:
        silmaluku = random.randint(1, tahkot)
        print(silmaluku)
        if silmaluku == suurinsilmaluku:
            break

paaohjelma()