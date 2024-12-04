from fruitmand import fruitmand

gewicht = sum(fruit["weight"] for fruit in fruitmand)
gewicht=gewicht/1000

print(f"gewicht zonder watermeloen is {gewicht:.2f} kg")

watermeloen={
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)

for fruit in fruitmand:
    print(fruit["name"])

gewicht = sum(fruit["weight"] for fruit in fruitmand)
gewicht=gewicht/1000

print(f"gewicht met watermeloen is {gewicht:.2f} kg")