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
    kleur = random.choice(kleur)
    if kleur in zak:
        zak[kleur] +=1
    else:
        zak[kleur]= 1


print(zak)
#if blauw 
#add oranje