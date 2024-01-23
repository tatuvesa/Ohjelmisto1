##numerot = []

##while True:
##    luku = input("Anna luku: ")
##    if luku == "":
##        break
##    else:
##        numerot.append(int(luku))

##if numerot:
##    print("Pienin luku on", min(numerot))
##    print("Suurin luku on", max(numerot))

luvut = []
luku = input("Anna luku: ")

while luku != "":
    arvo = float(luku)
    luvut.append(arvo)
    luku = input("Anna luku: ")
print("Pienin luku on", min(luvut))
print("Suurin luku on", max(luvut))