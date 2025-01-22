def gegevens():
    lijst=[]
    while True:
        naam = input("Wat is je naam? ").capitalize()
        woon = input("Waar woon je ").capitalize()
        while True:
            try: 
                leeftijd = int(input("Wat is je leeftijd "))
                break
            except ValueError:
                print("Je mag aleen hele cijfers doen")
        gegeven= {"naam":naam, "leeftijd":leeftijd,"woon":woon}
        deel=(f"{gegeven["naam"]}, die in {gegeven["woon"]} woont, is {gegeven["leeftijd"]} jaar")
        lijst.append(deel)
        while True:
            nogeens=input("Wil je nog een naam invoeren? (Ja/Nee) ").lower()
            print("")
            if nogeens =="nee":
                break
            elif nogeens=="ja":
                break
            else:
                print("Je kunt aleen ja of nee invoeren")
        if nogeens == "nee":
            break

    while lijst:
        show = lijst.pop(0)
        print(show)
    return gegeven

gegevens()