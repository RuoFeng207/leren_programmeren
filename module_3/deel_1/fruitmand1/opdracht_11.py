from fruitmand import fruitmand
rond =0
niet_rond=0

kleuren = ["red", "yellow", "brown", "green"]

while True:
    kleur = input("Voer een kleur in: ")
    kleur = kleur.lower()
    if kleur in kleuren:
        break
    else:
        print("Dit is geen kleur ")

for fruit in fruitmand:
    if fruit["color"]==kleur:
        kleur_fruit=(fruit["color"])
        if fruit["round"]==True:
            rond+=1
        else:
            niet_rond+=1

verschil = rond-niet_rond

if rond > niet_rond:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}.")
elif rond < niet_rond:
    print(f"Er zijn {abs(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}.")
else:
    print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur}.")