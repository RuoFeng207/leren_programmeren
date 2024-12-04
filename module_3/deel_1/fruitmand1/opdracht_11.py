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
    if fruit["color"] == kleur and fruit["round"]== True:
        print(fruit["name"])
        rond+=1
        print(rond)
    else:
        niet_rond+=1
        print(niet_rond)

if rond>niet_rond:
    print("Er zijn meer niet ronde dan ronde vruchten van die kleur.")
elif rond<niet_rond:
    print("Er zijn meer ronde dan niet ronde vruchten van die kleur.")
else:
    print("Je hebt evenveel ronde als niet ronde vruchten van die kleur.")
