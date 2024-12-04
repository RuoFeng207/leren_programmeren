from fruitmand import fruitmand
kleur_set=set()
if "druif" in fruitmand:
    fruitmand.remove("druif")
for fruit in fruitmand:
    fruit=fruit['color']
    kleur_set.add(fruit)
kleur_set.remove("red")
print(kleur_set)