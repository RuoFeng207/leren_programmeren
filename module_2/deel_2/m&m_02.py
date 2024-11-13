import random


while True:
    try:
        hoeveel=(input("Hoeveel M&M's wil je? "))
        hoeveel=int(hoeveel)
        if hoeveel<0:
            print("Je kan niet minder dan 0 M&M's toevoegen")
        else:
            break
        
    except:
        print("Dit is geen hele M&M")
zak ={}

for x in range(hoeveel):
    kleur = ["rood", "blauw", "groen", "geel", "bruin"]
    keus = random.choice(kleur)
    if keus =="blauw":
        kleur.append("oranje")
        if "oranje" in zak:
            zak["oranje"]+=1
        else:
            zak["oranje"]=1
    if keus in zak:
        zak[keus] +=1
    else:
        zak[keus]= 1


print(zak)
