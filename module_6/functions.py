import time
import sys
import data as d 

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
        print("")
        tekst(vraag)
        try:
            antwoord = int(input())
            if antwoord <1:
                tekst("Sorry, dat snap ik niet...")
            else:
                break
        except ValueError:
            tekst("Sorry, dat snap ik niet...")
    return antwoord
    
def str_afvang(vraag:str,lijst:int):
    print("")
    tekst(vraag)
    while True:
        opties = []
        teller = 0
        for x in d.ijs_winkel[lijst]:
            keus =d.ijs_winkel[lijst][teller]['afkorting']
            naam =d.ijs_winkel[lijst][teller]['naam']
            print(f"{keus}: {naam}")
            opties.append(keus)
            teller+=1
        antwoord = input().capitalize()
        if antwoord not in opties:
            tekst("Sorry, dat snap ik niet")
        else:
            break
    return antwoord

def print_regel(naam,aantal,prijs):
    totaal = aantal * prijs
    if aantal>0:
        print(f"{naam:12} {aantal:5} x €{prijs:.2f} =  €{totaal:.2f}")
        d.totaal.append(totaal)

def print_houders(lijst):
    for item in lijst:
        naam = item['naam']
        aantal = item['aantal']
        prijs = item['prijs']  # altijd float
        print_regel(naam,aantal,prijs)

def print_dubbele(lijst_index, prijs_key):
    for item in lijst_index:
        naam = item['naam']
        if "aantal.B" in item:
            aantal = item["aantal.B"]
            prijs = item["prijs"]["Bakje"]
            print_regel(naam,aantal,prijs)
            aantal = item["aantal.H"]
            prijs = item["prijs"]["Hoortje"]
            print_regel(naam,aantal,prijs)
        else:
            prijs = item['prijs']
            if isinstance(prijs, dict):
                prijs = prijs[prijs_key]
            aantal = item['aantal']
            print_regel(naam,aantal,prijs)
            
    return lijst_index, prijs_key

def bon():
    print("----------['Papi Gelato']----------")
    prijs_smaak = "bedrijf" if d.ijs_winkel[0][1]['zakelijke klant'] else "klant"
    print_dubbele(d.ijs_winkel[1], prijs_smaak)
    print_houders(d.ijs_winkel[2])
    saus_key = "Hoortje" if d.ijs_winkel[2][0]['aantal'] > 0 else "Bakje"
    print_dubbele(d.ijs_winkel[3], saus_key)
    som = sum(d.totaal)
    print(f"{'---------+':>36}")
    if d.ijs_winkel[0][1]['zakelijke klant']:
        d.btw = som * 0.09 
        print(f"{'BTW':29} €{d.btw:.2f}")
    print(f"{'Totaal':29} €{som:.2f}")
