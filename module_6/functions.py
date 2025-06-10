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
        tekst(vraag)
        try:
            antwoord = int(input())
            if antwoord <1:
                tekst("Sorry, dat snap ik niet...")
            else:
                break
        except ValueError:
            tekst("Sorry, dat snap ik niet...")
        print("")
        return antwoord
def str_afvang(vraag:str,lijst:int):
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
        print("")
        antwoord = input().capitalize()
        if antwoord not in opties:
            tekst("Sorry, dat snap ik niet")
            print("")
        else:
            break
    return antwoord