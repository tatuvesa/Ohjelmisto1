def parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parittomat = parittomat(lista)

print(f"Alkuperäinen lista: {lista}")
print(f"Parittomat pois: {parittomat}")