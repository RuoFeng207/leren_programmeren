# stond al in het bestand

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
bandje = False
stempel = False


#bouw hieronder de floowchart na

# functie voor toegestaande leeftijd
def oud_genoeg(toegang):
    verschil = toegang - leeftijd
    print(f"Probeer het over {verschil} jaar nog eens")

#vraagt je leeftijd voor toegang
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
#chek de vip lijst+leeftijd>=21

if naam in VIP_LIST and leeftijd>=21:
    print("Jij krijg van mij een blauw bandje")
    kleur="blauw"

if naam in VIP_LIST and leeftijd<21:
    print("Jij krijgt van mij een rood bandje")
    kleur="rood"
if naam not in VIP_LIST and leeftijd>=21:
    print("Jij krijgt van mij een stempel")
    stempel=True

#vraag wat ze willen drinken
while True:
    
    drank = str(input("Wat wil je drinken ").lower())
    
    if drank.isalpha():
        break
    else:
        print("Je kunt hier geen cijfers invoeren ")

# drankje keus true

if drank== "cola" and bandje == True:
    print("Alsjebieft met dit drankje is van het huis")
    quit()
if drank == "bier" and bandje== True or stempel == True:
    print("Alsjebieft met dit drankje is van het huis")
    quit()
if drank== "champagne" and bandje== True and kleur =="blauw":
    print(f"Oke hier is je drankje dat is dan {PRIJS_CHAMPAGNE} euro ")
    quit()
    
#drankje keus false
if drank not in DRANKJES:
    print("Ik begrijp er niks van, hier een glaasje water.")
    quit()

