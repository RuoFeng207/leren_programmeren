import random

zak=[]

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
for x in range(hoeveel):
    kleur= ("oranje","blauwe","groene","bruine")
    kleur =random.choice(kleur)
    zak.append(kleur)
print(f"Je zak is gevult met {zak} M&M's")