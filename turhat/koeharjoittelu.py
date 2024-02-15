def suorakulmion_piiri(e, t):
    tulos = (sivu1+sivu2)*2
    return tulos

def parittomat(lista):
    parittomat = []
    for i in lista:
        if i % 2 != 0:
            parittomat.append(i)
    return parittomat


sivu1 = 7
sivu2 = 3

print(f"Suorakulmion sivut ovat {sivu1} ja {sivu2}")
print(f"Suorakulmion piiri on {suorakulmion_piiri(sivu1, sivu2)}")

luvut = [12, 5, 21, 4, 8, 0, 11]
parittomat = parittomat(luvut)
print("Alkuperäiset luvut: " + str(luvut))
print("Parittomat luvut: " + str(parittomat))