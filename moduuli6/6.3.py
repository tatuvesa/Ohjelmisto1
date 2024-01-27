def gallonatlitroiksi(gallona):
    return gallona * 3.785

def paaohjelma():
    while True:
        gallona = float(input("Gallona määrä: "))
        if gallona < 0:
            print("Lopetetaan ohjelma.")
            break
        litra = gallonatlitroiksi(gallona)
        print(f"{gallona} gallonaa on {litra:.2f} litraa.")

paaohjelma()