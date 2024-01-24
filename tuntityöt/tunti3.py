##kerrat = int(input("montako kertaa?: "))
##tehdyt = 0
##while tehdyt < kerrat:
##    print("Haista")
##   tehdyt = tehdyt + 1

##komento = input ("Anna komento: ")
##while komento != "lopeta":
##    print ("Suoritan toiminnon: " + komento)
##    komento = input("Anna komento: ")
## print ("Toiminnot lopetettu.")

##import random

##noppa1 = noppa2 = heitot = 0
##while (noppa1 != 6 or noppa2 != 6):
#    noppa1 = random.randint(1, 6)
#    noppa2 = random.randint(1, 6)
#    heitot = heitot + 1
#print(f"Tarvittiin {heitot:d} heittoa.")

#eka = 1
#while eka <= 5:
#    toka = 1
#    while toka <= 5:
#        print(f"{eka} kertaa {toka} on {eka*toka:d}")
#        toka = toka + 1
#    eka = eka + 1

#import random
#toistot = 0
#heitot_yhteensä = 0
#while toistot < 1000000:

#    noppa1 = noppa2 = heitot = 0
#    while (noppa1!=6 or noppa2!=6):
#        noppa1 = random.randint(1,6)
#        noppa2 = random.randint(1,6)
#        heitot = heitot + 1
#    #print(f"Tarvittiin {heitot:d} heittoa.")
#    toistot = toistot + 1
#    heitot_yhteensä = heitot_yhteensä + heitot

#heitot_keskimäärin = heitot_yhteensä/toistot
#print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")

komento = input("Anna komento: ")
while komento != "lopeta":
    if komento == "MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")