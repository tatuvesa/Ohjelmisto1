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