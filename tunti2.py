import math
import random

ika = int(input("Kerro ikäsi: "))

#if ika < 18:
#    print("Painu hiiteen")
#else:
#    print("Tervetuloa")

#if ika >= 18:
#   print("Tervetuloa")

if ika < 18:
    print("Lähde kotiin")

elif ika >= 18 and ika <= 20:
    paperit = input("Anna henkkarit j/e: ")

    if paperit == "j":
        print("Tervetuloa mans")
    else:
        print("Hyvä yritys mutta mene kotiin")

else:
    print("Tervetuloa!")