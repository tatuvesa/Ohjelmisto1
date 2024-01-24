leiviska = float(input("\nSyötä leiviskät: "))
naulat = float(input("Syötä naulat: "))
luodit = float(input("Syötä luodit: "))

grammat = (leiviska * 20 * 32 + naulat * 32 + luodit) * 13.3

#kg = int(grammat / 1000)
#grammat = grammat % 1000
#print("\nMassa on", kg, " kilogrammaa ja ", round(grammat,2), " grammaa.")

print(f"Massa on {grammat // 1000} kilogrammaa ja {grammat % 1000:.2f} grammaa.")