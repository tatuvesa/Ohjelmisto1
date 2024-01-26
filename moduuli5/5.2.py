luvut = []
luku = int(input("Anna numero: "))

while luku != "":
    luvut.append(int(luku))
    luku = input("Anna numero: ")

luvut.sort(reverse=True)
print(f"Suurimmat luvut: {luvut[0:5]}")