def gegevens():
    lijst=[]
    while True:
        naam = input("Wat is je naam? ").capitalize()
        while True:
            try: 
                leeftijd = int(input("Wat is je leeftijd "))
                break
            except ValueError:
                print("Je mag aleen hele cijfers doen")
        gegeven= {"naam":naam, "leeftijd":leeftijd}
        deel=(f"{gegeven["naam"]} is {gegeven["leeftijd"]} jaar")
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