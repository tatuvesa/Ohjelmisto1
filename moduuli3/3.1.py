kuha = float(input("Kerro kuhasi pituus: "))

if kuha < 37:
    print(f"Heitä kuha takaisin järveen! Kuhan pitää olla {37 - kuha:.1f} cm pidempi!\n")
else:
    print("Hieno kala!")