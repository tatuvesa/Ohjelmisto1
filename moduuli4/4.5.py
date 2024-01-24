oikeakayttajatunnus = "python"
oikeasalasana = "rules"
yritykset = 0

while yritykset < 5:
    kayttajatunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")

    if kayttajatunnus == oikeakayttajatunnus and salasana == oikeasalasana:
        print("Tervetuloa!")
        break
    elif kayttajatunnus != oikeakayttajatunnus or salasana != oikeasalasana:
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty.")
