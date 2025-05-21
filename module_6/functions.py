# imports
import time,sys,data

# afkortingen
d = data

# type writhing
def tekst(woord:str):
    for letter in woord:
        time.sleep(d.tekst_snelheid)
        sys.stdout.write(letter)
        sys.stdout.flush()

# vraag en fout afhang
def int_afvang(vraag:str):
    while True:
        tekst(f"{vraag}\n")
        try:
            antwoord = int(input())
            return antwoord
        except ValueError:
            tekst("Sorry, dat snap ik niet...\n")
            print("")

def str_afvang(vraag:str, optie_1:str, optie_2:str):
    while True:
        tekst(f"{vraag}\n")
        antwoord = input().lower()
        if antwoord == optie_1:
            return optie_1
        elif antwoord == optie_2:
            return optie_2
        else:
            tekst("Sorry, dat snap ik niet...\n")
            print("")

def             
# bonnetje
def bon():
    a = d.bol*d.prijs_bol
    b = d.hoorntje*d.prijs_hoorntje
    c = d.bakje*d.prijs_bakje
    if d.bol>0 or d.hoorntje >0 or d.bakje>0:
        print('-------["Papi Gelato"]---------')
        print("")
        if d.bol >0:
            print(f"Bolletjes {d.bol:4.0f} x {d.prijs_bol:.2f}   = €{a:6.2f}")
        if d.hoorntje >0:
            print(f"Hoorntjes {d.hoorntje:4.0f} x {d.prijs_hoorntje:.2f}   = €{b:6.2f}")
        if d.bakje>0:
            print(f"Bakje     {d.bakje:4.0f} x {d.prijs_bakje:.2f}   = €{c:6.2f}")
        print(f"{'--------- +':>35}")
        print(f"{'Totaal':<24} = € {a+b+c:.2f}")