from fruitmand import fruitmand
fruitmand.sort(key=lambda fruit:fruit["weight"], reverse=True)

for fruit in fruitmand:
    naam=(fruit["name"])
    gewicht=(fruit["weight"])
    gewicht=gewicht/1000
    print(f"{naam} is {gewicht} kg")