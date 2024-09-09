#al het geld is in euro 
toegang = 7.45
personen = 4
#koste voor 1 minuten
koste_VIP_VR = 0.074
aantal_min = 45
# totaal

totaal_toegang = toegang*personen

totaal_vr = koste_VIP_VR*aantal_min*personen
print(totaal_vr)

totaal_prijs =round(totaal_toegang+totaal_vr,2)

print(f"Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal_prijs} euro")