vuodenajat = {
    1: "talvi.", 2: "talvi", 3: "kevät", 4: "kevät", 5: "kevät",
    6: "kesä", 7: "kesä", 8: "kesä", 9: "syksy", 10: "syksy",
    11: "syksy", 12: "talvi"
}

kuukausi = int(input("Anna kuukauden numero: "))
if kuukausi in vuodenajat:
    print(f"Vuodenaika on {vuodenajat[kuukausi]}")
else:
    print("Virheellinen kuukausi.")