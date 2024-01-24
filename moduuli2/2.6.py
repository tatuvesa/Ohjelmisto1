import random

numero1 = ""
for _ in range(3):
    numero1 += str(random.randint(0, 9))
numero2 = ""
for _ in range(4):
    numero2 += str(random.randint(1, 6))

print("\nKolminumeroinen koodi on: ", numero1)
print("Nelinumeroinen koodi on: ", numero2 + "\n")