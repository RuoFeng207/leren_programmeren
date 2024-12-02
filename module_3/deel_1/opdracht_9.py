from fruitmand import fruitmand
lijst=[]
for fruit in fruitmand:
    fruit=fruit["name"]
    lijst.append(fruit)

lijst.remove("druif")
print(lijst)