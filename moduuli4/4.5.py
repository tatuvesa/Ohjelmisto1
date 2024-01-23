import math
import random

tunnus = ("python")
salasana = ("rules")
kayttajatunnus = input("Käyttäjätunnus: ")
syottosalasana = input("Syottosalasana: ")
arvaukset = 0

while kayttajatunnus != "python" or syottosalasana != "rules":
    print("Väärä käyttäjätunnus tai salasana.")
    kayttajatunnus = input("Käyttäjätunnus: ")
    syottosalasana = input("Salasana: ")


