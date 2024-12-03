from fruitmand import fruitmand
import random
while True:
    try:
        getal = int(input("Voer een heelgetal in: "))
        break
    except:
        print("Dit is geen heelgetal.")

mand =[]
lijst=[]
for fruit in fruitmand:
    fruit=(fruit["name"])
    lijst.append(fruit)

for i in range(getal):
    keuze =random.choice(lijst)
    mand.append(keuze)
print(f"Mand! {mand}")
