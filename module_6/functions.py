# imports
import time,sys,data

# afkortingen
d = data

# type writhing
def tekst(woord: str, newline: bool = True):
    for letter in woord:
        time.sleep(d.tekst_snelheid)
        sys.stdout.write(letter)
        sys.stdout.flush()
    if newline:
        sys.stdout.write('\n')
        sys.stdout.flush()


# vraag en fout afhang
def int_afvang(vraag:str):
    while True:
        tekst(vraag)
        try:
            antwoord = int(input())
            return antwoord
        except ValueError:
            tekst("Sorry, dat snap ik niet...")
            print("")

def str_afvang(vraag: str, keus:dict):
    while True:
        tekst(vraag)
        optie_tekst = ", ".join(f"{sleutel}) {optie}" for sleutel, optie in keus.items()) 
        tekst(optie_tekst)
        
        antwoord = input().capitalize()

        if antwoord in keus:
            return keus[antwoord]
        else:
            tekst("Sorry, dat snap ik niet...")
            print("")

def gegevens_bon(dictonary):
    afstand = 14
    for _, info in dictonary.items():
        woord = info['naam']
        prijs = info['aantal'] * info['prijs']
        tussen_lengte = afstand - len(woord)
        tussen = ' ' * tussen_lengte if tussen_lengte > 0 else ''
        if info['aantal'] > 0:
            print(f"{woord}{tussen}{info['aantal']} x €{info['prijs']:.2f}{'':>3}= €{prijs:.2f}")
            d.totaal.append(prijs)

def toon_bon():
    print('---------["Papi Gelato"]---------')
    gegevens_bon(d.smaken)
    gegevens_bon(d.houders)
    gegevens_bon(d.toppings)

    som = sum(d.totaal)
    if som > 0:
        print(f"{'-------- +':>36}")
        print(f"{'Totaal'}{"":>19} = €{som:.2f}")
    else:
        print(f"{'':>6}Je hebt niks besteld")
