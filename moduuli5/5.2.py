import random
import math

luvut = []
luku = int(input("Anna numero: "))

while luku != "":
    arvo = int(luku)
    luvut.append(arvo)
    luku = input("Anna numero: ")

luvut.sort(reverse=True)
for luku in range(1):
    print(f"Suurimmat luvut: {luvut[0:5]}")