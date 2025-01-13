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
while True:
    probleem= False
    random.shuffle(lootjes)
    for y in range(len(lootjes)):
        if lootjes[y]==deelnemers[y]:
            probleem= True
            break
    
    if probleem== False:
        break
while True:
    while True:
                zien=input("Wat is jou naam? ")
                if zien.isalpha():
                    zien = zien.capitalize()
                    print(zien)
                    break
                else:
                    print("Je naam mag geen cijfers of tekens bevatten.")
                    print("")

    for i in range(len(lootjes)):
        if zien== lootjes[i]:
            trekt = print(f"Je hebt {deelnemers[i]}")
            print("")
            break
    while True:
        volgende=input("Wil je nogeens invoeren? ")
        if volgende=="ja":
            break
        elif volgende =="nee":
            break
        else:
            print("Je kunt alleen ja of nee invoeren")
            print("")
    if volgende=="nee":
        break