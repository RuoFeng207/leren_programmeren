import random

deelnemers = []
lootjes = []
teller =0
extra = ''
while True:
    teller+=1
    while True:
        while True:
            naam=input("Wat is jou naam? ")
            if naam.isalpha():
                naam = naam.capitalize()
                print(naam)
                break
            else:
                print("Je naam mag geen cijfers of tekens bevatten.")
                print("")
        if naam in deelnemers:
            print("Deze naam zit al in de lijst.")
        else:
            deelnemers.append(naam)
            lootjes.append(naam)
            break
    if teller>=3:
        while True:
            extra= input("Wil je nog een naam invoeren? ")
            extra.lower
       
            if extra =="ja" or extra=="nee":
                break
            else:
                print("Je kan alleen maar ja of nee invoeren")
    if extra =="nee":
        print("Oke")
        break

for y in range(teller):
    while True:
        kies1= random.choice(deelnemers)
        kies2 = random.choice(lootjes)
        
        
        if kies1 != kies2:
            deelnemers.remove(kies1)
            lootjes.remove(kies2)
            trekt = print(f"{kies1} heeft {kies2}")
            while True:
                zien =input("Welke naam wil je zien? ")
                zien = zien.capitalize
                if zien == kies1:
                    print(f"Je hebt {kies2}")
                    break
                if zien == kies2:
                    print(f"Je hebt{kies1}")
                    break
                else:
                    print("Deze naam zit niet in de lijst")
            break