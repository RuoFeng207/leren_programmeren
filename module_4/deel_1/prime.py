from functions import *
print("1 Wil je weten hoeveel prime er tot en met een getal is ")
print("2 Wil je dat je even veel prime hebt als het nummer dat je hebt")
print("3 Wil je dat je zien hoeveel prime er tussen 2 getallen zijn")

while True:
    while True:
        try:
            keus =int(input("Kies 1,2 of 3: "))
            break
        except:
            print("Je mag aleen cijfers invoeren")
    if keus == keus<1 or keus>3:
        print("Je kan alleen 1,2 of 3 invoeren")
    else:
        break
while True:
    if keus == 1:
        while True:
            try:
                vraag = int(input("Voer een getal in: "))
                break
            except:
                print("Je kunt alleen cijfers invoeren")
        print(prime_teller(vraag))

    elif keus == 2:
        
        while True:
            try:
                vraag = int(input("Voer een getal in: "))
                break
            except:
                print("Je kunt alleen cijfers invoeren")
        print(prime_loop(vraag))
    else:
        while True:
            try:
                vraag = int(input("Voer een getal in: "))
                break
            except:
                print("Je kunt alleen cijfers invoeren")
        print(tussen_cijfers(vraag))

    while True:
        nogeens = input("Wil je nog eens? ").lower()
        if nogeens == "ja":
            break
        elif nogeens == "nee":
            break
        else:
            print("Je kan alleen ja of nee invoeren")
    if nogeens == "nee":
        break
