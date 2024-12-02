from fruitmand import fruitmand
lijst=[]
for fruit in reversed(fruitmand):
    fruit=(fruit["weight"])
    lijst.append(fruit)
gewicht = sum(lijst)
gewicht=gewicht/1000

print(f"Het gewicht van de fruitmand is {round(gewicht,1)} kg")