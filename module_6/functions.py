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
        optie_tekst = ", ".join(f"{sleutel}: {optie}" for sleutel, optie in keus.items()) 
        tekst(optie_tekst)
        
        antwoord = input().capitalize()

        if antwoord in keus:
            return keus[antwoord]
        else:
            tekst("Sorry, dat snap ik niet...")
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