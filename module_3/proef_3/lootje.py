import random

deelnemers = []
lootjes = []
for x in range(3):
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
for y in range(3):
    while True:
        kies1= random.choice(deelnemers)
        kies2 = random.choice(lootjes)
        
        
        if kies1 != kies2:
            deelnemers.remove(kies1)
            lootjes.remove(kies2)
            trekt = print(f"{kies1} heeft {kies2}")
            break
        