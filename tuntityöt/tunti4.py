## listoja

nimet = ["ahmed", "ahmed1", "ahmed2", "ahmed3", "ahmed4", "ahmed5"]

print(nimet[0:6])

nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)