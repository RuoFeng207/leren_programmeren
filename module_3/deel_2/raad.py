import random
ronde =1
teller=0
score=0
while ronde<21:
    print(f"ronde {ronde}")
    ronde+=1
    keuze=random.randint(1,1000)
    print(keuze)
    while True:
        while True:
            try:
                raad=int(input("raad het getal: "))
                break
            except ValueError:
                print("Je kan aleen maar cijfers invoeren")
        verschil = abs(keuze-raad)

        if verschil<20 and verschil >0:
            print("Je bent heel warm")
        elif verschil<50 and verschil>0:
            print("je bent warm")
        if keuze==raad:
            print("Je hebt het geraden!")
            score+=1
            print(f"Je score is {score}")
            break
        if teller ==10:
            print(f"Je score is {score}")
            break
    while True:
        nogeens=input("Wil je nog een ronde spelen? ").lower()
        if nogeens=="ja":
            break
        elif nogeens=="nee":
            break
        else:
            print("Je kunt alleen maar antwoorden met ja of nee ")
    if nogeens=="nee":
        print("Bedankt voor het spelen")
        break