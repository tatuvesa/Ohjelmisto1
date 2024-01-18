import math
import random

# 1 tehtävä 1 kohta_____________________________________________________________________

print("Hei, Tatu Vesalainen!\n")

# 2 tehtävä 1.__________________________________________________________________________

user = input('Anna nimesi!: ')
print("Terve, " + user + "!\n")

# tehtävä 2 ympyrän säde__________________________________________________________________

sade = float(input("Syötä ympyrän säteen pituus: "))
print("Ympyrän pinta-ala on: ", math.pi * sade**2)

#tehtävä 2 suorakulmion piiri ja pinta-ala__________________________________________________

kanta = float(input("\nAnna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print("Suorakulmion piiri on: ", piiri)
print("suorakulmion pinta-ala on: ", pinta_ala)

# tehtävä 2 kolme kokonaislukua________________________________________________________

print("\nSyötä kolme kokonaislukua.")
luku1 = float(input("Syötä ensimmäinen luku: "))
luku2 = float(input("Syötä toinen luku: "))
luku3 = float(input("Syötä kolmas luku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print("\nLukujen summa on: ", summa)
print("Lukujen tulo on: ", tulo)
print("Lukujen keskiarvo on: ", keskiarvo)

# tehtävä 2 leiviskät, naulat ja luodit____________________________________________________

leiviska = float(input("\nSyötä leiviskät: "))
naulat = float(input("Syötä naulat: "))
luodit = float(input("Syötä luodit: "))

grammat = (leiviska * 20 * 32 + naulat * 32 + luodit) * 13.3

kg = int(grammat / 1000)
grammat = grammat % 1000
print("\nMassa on", kg, " kilogrammaa ja ", round(grammat,2), " grammaa.")

# toinen ratkaisu jota en osaa pyöristää :/
# print(f"Massa on {grammat // 1000} kilogrammaa ja {grammat % 1000} grammaa.")

#tehtävä 2 kohta 6, 3 numeroa ja 4 numeroa_________________________________________________

numero1 = ""
for _ in range(3):
    numero1 += str(random.randint(0, 9))
numero2 = ""
for _ in range(4):
    numero2 += str(random.randint(1, 6))

print("\nKolminumeroinen koodi on: ", numero1)
print("Nelinumeroinen koodi on: ", numero2 + "\n")