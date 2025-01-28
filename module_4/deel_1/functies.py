def vraag():
    data = {}
    data["naam"] = input("Wat is je naam? ").capitalize()
    data["woon"]= input("waar woon je? ").capitalize()
    data["leeftijd"] = int(input("Wat is je leeftijd? "))
    return data

def gegvens():
    lijst = []
    while True:
        q = vraag()
        lijst.append(q)
        nogeens = input("Wil je nog eens? (Ja/Nee) ").lower()
        if nogeens == "nee":
            break
        elif nogeens != "ja":
            print("Je kan alleen ja of nee invoeren")
            break
        print("")
        
    return lijst