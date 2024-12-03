from fruitmand import fruitmand
lijst=[]
kleur = {
    "red": "rood",
    "yellow": "geel",
    "green": "groen",
    "orange": "oranje",
    "brown": "bruin"
}
for fruit in fruitmand:
    naam=(fruit["name"])
    kleur=(fruit["color"])

    lengte=len(naam)
    neuw =print(naam, lengte)
