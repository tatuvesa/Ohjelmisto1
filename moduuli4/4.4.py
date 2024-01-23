import math
import random

randomi = random.randint(1,10)
numero = int(input("Arvaa luku (1-10): "))

while numero != randomi:
    if numero > randomi:
        print("Liian korkea!")
    elif numero < randomi:
        print("Liian alhaalla!")
    numero = int(input("Arvaa luku (1-10): "))
else:
    print("Oikein!")