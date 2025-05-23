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

def str_afvang(vraag:str, optie_1:str, optie_2:str, optie_3:str,optie_4:str):
    while True:
        tekst(f"{vraag}\n")
        antwoord = input().lower()
        if antwoord == optie_1:
            return optie_1
        elif antwoord == optie_2:
            return optie_2
        elif antwoord == optie_3:
            if optie_3 != None:
                return optie_3
        elif antwoord == optie_4:
            if optie_4 != None:
                return optie_4
        else:
            tekst("Sorry, dat snap ik niet...\n")
            print("")


def smaak(smaak_bol:str):
    naam = d.smaken[smaak_bol]["naam"]
    aantal = d.smaken[smaak_bol]["aantal"]
    prijs = d.smaken[smaak_bol]["prijs"]
    som = aantal*prijs
    print(f"{naam} {aantal:3.0f} x {prijs:.2f}{'= €':>6}{som:5.2f}")
    return som
    

# def bon():
#     som = 0
    
#     if som > 0:
#         print(f"{'-------- +':>33}")
#         print(f"{'Totaal':<22} = € {som:.2f}")
#     else:
#         print("Je hebt niks")

# bon()