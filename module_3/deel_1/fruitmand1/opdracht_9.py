from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit["name"]== "druif":
        fruitmand.remove(fruit)
kleuren=[]
for fruit in fruitmand:
    if not fruit["color"] in kleuren:
        kleuren.append(fruit["color"])
print(kleuren)