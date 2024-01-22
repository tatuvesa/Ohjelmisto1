# 3.1 kuha
kuha = float(input("Kerro kuhasi pituus: "))

if kuha < 37:
    print(f"Heitä kuha takaisin järveen! Kuhan pitää olla {37 - kuha:.1f} cm pidempi!\n")
else:
    print("Hieno kala!")

# 3.2 laivan hyttiluokka

hytti = str.upper(input("Mistä hyttiluokasta haluat tietää? LUX / A / B / C: "))

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!\n")

# 3.3 Biologinen sukupuoli

sukupuoli = str.lower(input("Mikä on biologinen sukupuolesi mies/nainen: "))
if sukupuoli == "mies" or sukupuoli == "nainen":
    hemoglobiini = float(input("Mikä on hemoglobiini arvosi?: "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on normaali.")

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on normaali.")
else:
    print("Virheellinen sukupuoli.")

# 3.4 karkausvuosi

vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")