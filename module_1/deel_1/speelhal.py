from termcolor import colored, cprint, COLORS

#al het geld is in euro 
toegang = 7.45
personen = int(input("Met hoeveel personen bent je: "))
#koste voor 1 minuten
koste_VIP_VR = 0.074
aantal_min = int(input("Hoeveel minuten wilt je de vr bril gebruiken: "))
# totaal

totaal_toegang = toegang*personen

totaal_vr = koste_VIP_VR*aantal_min*personen


totaal_prijs =round(totaal_toegang+totaal_vr,2)

print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {aantal_min} minuten VR kost je maar {colored(totaal_prijs,'yellow', attrs=['bold'])} euro")