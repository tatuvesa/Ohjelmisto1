maat1 = []
maat2 = ["Suomi", "Ruotsi", "Norja", "Tanska", "Islanti"]
maat3 = ["Viro", "Latvia", "Liettua"]
maat2.extend(maat3)
maat1.extend(maat2)
maat1.append("Puola")

print(maat1[1])
if "Viro" in maat2:
    print("Juu")
else:
    print("Ei")
if "Viro" in maat1:
    print("Joopajoo")
else:
    print("Eipäei")
print(maat1[-1])

#   Ruotsi      koska maat1[1] 0 on suomi
#   Juu     Viro, latvia ja liettua syötetään 2 listaan
#   Joopajoo    kaikki edeltävät maat lisätään 1 listaan.
#   Puola   lopussa oleva lauseke hakee viimeisen maan listassa joka on Puola.