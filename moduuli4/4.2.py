pituus = float(input("Pituus tuumina: "))

while pituus > 0:
    sentit = pituus * 2.54
    print(f"{sentit:.2f}")
    pituus = float(input("Pituus tuumina: "))
else:
    print("Lopetetaan ohjelma.")