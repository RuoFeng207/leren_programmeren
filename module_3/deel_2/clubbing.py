# stond al in het bestand

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')



#bouw hieronder de floowchart na

# functie voor toegestaande leeftijd
def oud_genoeg(toegang):
    verschil = toegang - leeftijd
    print(f"Probeer het over {verschil} jaar nog eens")

#vraagt je leeftijd
while True:
    try:
        leeftijd=int(input("Hoe oud ben jij? "))
        break
    except(ValueError):
        print("aleen cijfers")

#gooit je er uit als je jonger dan 18 bent en laat je weten over hoeveel jaar je terug kan komen
if leeftijd<18:
    print("sorry je mag er niet in ")
    oud_genoeg(18)
    quit() #eindigt het programma

#vraagt om naam
while True:
    
    naam = str(input("Wat is je naam? ").lower())
    
    if naam.isalpha():
        break
    else:
        print("Je kunt hier geen cijfers invoeren ")

