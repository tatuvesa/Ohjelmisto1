import math

def lasku(pizza, hinta):
    sade = pizza / 2
    pintaala = math.pi * sade ** 2
    return hinta / pintaala

pizza1 = float(input("Ensimmäisen pizzan koko -> "))
hinta1 = float(input("Pizzan hinta -> "))

pizza2 = float(input("Toisen pizzan koko -> "))
hinta2 = float(input("Pizzan hinta -> "))

pala1 = lasku(pizza1, hinta1)
pala2 = lasku(pizza2, hinta2)

if pala1 < pala2:
    print("Ensimmäinen pizza on hinnaltaan parempi.")
elif pala1 > pala2:
    print("Toinen pizza on hinnaltaan parempi.")
else:
    print("Kummatkin pizzat ovat hinnaltaan hyviä.")