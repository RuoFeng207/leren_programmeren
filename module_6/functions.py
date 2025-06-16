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

def berekening1(lijst_index):
    for item in d.ijs_winkel[lijst_index]:
        naam = item['naam']
        aantal = item['aantal']
        prijs = item['prijs']  # altijd float
        totaal = aantal * prijs
        if aantal>0:
            print(f"{naam:12} {aantal:5} x €{prijs:.2f} =  €{totaal:.2f}")
            d.totaal.append(totaal)
    return lijst_index

def berekening2(lijst_index, prijs_key):
    for item in d.ijs_winkel[lijst_index]:
        naam = item['naam']
        aantal = item['aantal']
        prijs = item['prijs']

        if isinstance(prijs, dict):
            prijs = prijs[prijs_key]
        totaal = aantal * prijs
        if aantal>0:
            print(f"{naam:12} {aantal:5} x €{prijs:.2f} =  €{totaal:.2f}")
            d.totaal.append(totaal)
    return lijst_index, prijs_key

def bon():
    print("----------['Papi Gelato']----------")
    berekening2(1,"klant")    # smaken
    berekening1(2)             # houders
    berekening2(3, 'Hoortje')    # sprinkels
    som = sum(d.totaal)
    print(f"{"---------+":>36}")
    print(f"{"Totaaal":28} €{som:.2f}")