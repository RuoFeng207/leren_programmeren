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
def brekening():
    # hoortje
    if d.ijs_winkel[2][0]['aantal'] >0:
        print(f"{d.ijs_winkel[2][0]['aantal']} x {d.ijs_winkel[2][0]['prijs']} = {d.ijs_winkel[2][0]['aantal']*{d.ijs_winkel[2][0]['prijs']}}")
    #bakje
    elif d.ijs_winkel[2][1]['aantal'] >0:
        pass
    

print(type(d.ijs_winkel[2][0]['aantal']))
print(type(d.ijs_winkel[2][0]['prijs']))
print(f"{d.ijs_winkel[2][0]['aantal']} x {d.ijs_winkel[2][0]['prijs']} = {d.ijs_winkel[2][0]['aantal']*d.ijs_winkel[2][0]['prijs']}")