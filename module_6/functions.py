import time,sys,data
d = data

def tekst(woord: str, newline: bool = True):
    for letter in woord:
        time.sleep(d.tekst_snelheid)
        sys.stdout.write(letter)
        sys.stdout.flush()
    if newline:
        sys.stdout.write('\n')
        sys.stdout.flush()

def int_afvang(vraag: str):
    while True:
        tekst(vraag)
        try:
            antwoord = int(input())
            return antwoord
        except ValueError:
            tekst("Sorry, dat snap ik niet...")
            print("")

def str_afvang(vraag: str, keus: dict):
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

def gegevens_bon(dictonary, houder_keuze=None):
    afstand = 14
    subtotal = 0 

    for _, info in dictonary.items():
        woord = info['naam']
        if isinstance(info['prijs'], dict):
            prijs_per_stuk = info['prijs'].get(houder_keuze, 0) if houder_keuze else 0
        else:
            prijs_per_stuk = info['prijs']

        prijs = info['aantal'] * prijs_per_stuk
        subtotal += prijs  

        tussen_lengte = afstand - len(woord)
        tussen = ' ' * tussen_lengte if tussen_lengte > 0 else ''
        if info['aantal'] > 0:
            print(f"{woord}{tussen}{info['aantal']} x €{prijs_per_stuk:.2f}{'':>3}= €{prijs:.2f}")

    return subtotal

def toon_bon():
    print('---------["Papi Gelato"]---------')
    houder_keuze = None
    for key, info in d.houders.items():
        if info['aantal'] > 0:
            houder_keuze = key
            break

    totaal_bedrag = 0
    totaal_bedrag += gegevens_bon(d.smaken)
    totaal_bedrag += gegevens_bon(d.houders)
    totaal_bedrag += gegevens_bon(d.toppings, houder_keuze=houder_keuze)

    if totaal_bedrag > 0:
        print(f"{'-------- +':>36}")
        print(f"{'Totaal'}{'':>19} = €{totaal_bedrag:.2f}")
    else:
        print(f"{'':>6}Je hebt niks besteld")

def reset_bestelling():
    for dic in (d.smaken, d.houders, d.toppings):
        for item in dic.values():
            item['aantal'] = 0
    d.totaal.clear()