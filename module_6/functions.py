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

def prijs():
    if d.prijs_bol == True:
        d.tot_prijs+=(1.10* d.bol )
    elif d.prijs_hoorntje == True:
        d.tot_prijs+=1.25
    elif d.prijs_bakje == True:
        d.tot_prijs+=0.75
    d.tot_prijs = round(d.tot_prijs,2)
    
    return d.tot_prijs
