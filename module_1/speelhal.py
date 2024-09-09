#al het geld is in euro 
toegang = 7.45
personen = 4
#koste voor 5 minuten
koste_VIP_VR = 0.37
aantal_min = 45
# totaal

totaal_toegang = toegang*personen

totaal_vr = koste_VIP_VR*aantal_min*personen

totaal_prijs =round(totaal_toegang*totaal_vr,2)

print(f"Je totaal prijs is {totaal_prijs} euro")