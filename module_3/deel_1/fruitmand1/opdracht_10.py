from fruitmand import fruitmand

lijst = []
for fruit in fruitmand:
    gewicht = fruit["weight"]
    lijst.append(gewicht)

lijst.sort(reverse=True)

print("Gesorteerd van groot naar klein:", lijst)