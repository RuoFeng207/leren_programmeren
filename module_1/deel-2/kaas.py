import time

print ("Je gaat zo een spel spelen met me jij neemt een kaas in gedachten en ik ga het raden. ")
print("Je mag aleen andwoorden met ja of nee.")

time.sleep(2)




kleur =input('is de kaas geel? ')
kleur = kleur.lower()

if kleur ==("ja"): 
    gaten = input("Zitten er gaten in? ")
    gaten = gaten.lower()
    
    if gaten ==("ja"):
        prijs=input("Is de prijs belachelijk duur? ")
        prijs=prijs.lower()
        if prijs==("ja"):
            print("Emmenthaler")
        elif prijs ==("nee"):
            print("leerdammer")
      
    elif gaten ==("nee"):
        hard = input("Is de kaas zo hard als steen? ")
        hrad=hard.lower()
        if hard==("ja"):
            print("Parmigiango, Reggiano")
        elif hard==("nee"):
            print("Goudse kaas")
        else:
            print("Deze keuze is ongeldig.")

        
    else:
        print("Deze keuze is ongeldig.")

elif kleur ==("nee"):
    schimel=input("Heeft de kaas blauwe schimmel? ")
    schimel=schimel.lower()
    if schimel==("ja"):
        korst =input("Heeft de kaas korst? ")
        korst=korst.lower()
        if korst ==("ja"):
            print("Blue de Rochbaron")
        elif korst==("nee"):
            print("Foume dambert")
        else:
            print("Deze keuze is ongeldig")
    elif schimel ==("nee"):
        korst_2=input("Heeft de kaas korst? ")
        korst_2=korst_2.lower()
        if korst_2==("ja"):
            print("Camembert")
        elif korst_2==("nee"):
            print("Mozzarella")
        else:
            print("Deze keuze is ongeldig.")
    else:
        print("Deze keuze is ongeldig.")
    
else:
    print("Deze keuze is ongeldig.")

