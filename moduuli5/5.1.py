import random

kerrat = int(input("Kuinka monta arpakuutiota haluat heittää? "))
summa = 0

for i in range(kerrat):
    summa = summa + random.randint(1, 6)
print(f"Silmälukujen summa on: {summa}")