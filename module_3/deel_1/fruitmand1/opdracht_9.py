from fruitmand import fruitmand
lijst=[]
for fruit in fruitmand:
    fruit=fruit['color']
    lijst.append(fruit)
lijst.remove("red")
print(lijst)