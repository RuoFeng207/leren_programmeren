def vraag():
    data = {}
    data["naam"] = input("Wat is je naam? ")
    data["woon"]= input("waar woon je? ")
    data["leeftijd"] = input("Wat is je leeftijd? ")
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

a=gegvens()
print("")
for persoon in a:
    print(f"{persoon["naam"]} die in {persoon["woon"]} woont is {persoon["leeftijd"]} jaar")