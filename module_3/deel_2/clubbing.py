# stond al in het bestand

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
bandje = False
stempel = False
kleur=""

def quinten():
    quit()


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
    quinten() #eindigt het programma

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
    bandje= True

if naam in VIP_LIST and leeftijd<21:
    print("Jij krijgt van mij een rood bandje")
    kleur="rood"
    bandje= True
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
    print("Alsjebieft dit drankje is van het huis")

if drank == "bier" and bandje== True or drank=="bier" and stempel == True:
    print("Alsjebieft dit drankje is van het huis")

if drank== "champagne" and bandje== True and kleur =="blauw":
    print(f"Oke hier is je drankje dat is dan {PRIJS_CHAMPAGNE} euro ")

    
#drankje keus false
if drank not in DRANKJES:
    print("Ik begrijp er niks van, hier een glaasje water.")
 
if drank== "cola" and bandje== False:
    print(f"Oke hier is je drankje dat is dan {PRIJS_COLA} euro ")


if drank=="bier" and bandje== False and stempel==False:
    print("Sorry je mag nog geen alcohol bestellen")
    oud_genoeg(21)
   
if drank=="champagne" and bandje== False :
    print("alleeen vips mogen champagne bestellen")

if naam in VIP_LIST and kleur=="rood" and drank =="champagne":
    print("Sorry je bent te jong om alcohol te kopen")
    oud_genoeg(21)
    