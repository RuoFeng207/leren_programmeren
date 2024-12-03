from fruitmand import fruitmand
min_lengte = 0

kleur = {
    "red": "rood",
    "yellow": "geel",
    "green": "groen",
    "orange": "oranje",
    "brown": "bruin",
    "pink":"roze"
}

for fruit in fruitmand:
    naam = fruit["name"]
    kleur2 = fruit["color"]
    gewicht= fruit["weight"]
    lengte = len(naam)


    if lengte > min_lengte:
        min_lengte = lengte
        N_kleur= kleur[kleur2]
        langste_fruit = naam
        N_gewicht=gewicht/1000
       
       
print(f"De {langste_fruit} ({min_lengte} letters) een {N_kleur} kleur en een gewicht van {N_gewicht} kg")