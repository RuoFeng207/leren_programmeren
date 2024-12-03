from fruitmand import fruitmand
lijst3=[]
for fruit in reversed(fruitmand):
    fruit=(fruit["weight"])
    lijst3.append(fruit)
gewicht = sum(lijst3)
gewicht=gewicht/1000
gewicht=gewicht
print(f"Het gewicht van de fruitmand zonder watermeloen is {gewicht} kg")

lijst=[]
for fruit in fruitmand:
    fruit=fruit["name"]
    lijst.append(fruit)

lijst.append("watermeloen")
watermeloen=2500

lijst2=[]
for fruit in reversed(fruitmand):
    fruit=(fruit["weight"])
    lijst2.append(fruit)
lijst2.append(watermeloen)
gewicht = sum(lijst2)
gewicht=gewicht/1000
gewicht=gewicht
print(f"Het gewicht van de fruitmand met watermeloen is {gewicht} kg")