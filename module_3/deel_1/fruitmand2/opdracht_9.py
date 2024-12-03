from fruitmand import fruitmand
lijst=[]
for fruit in fruitmand:
    fruit=fruit['color']
    lijst.append(fruit)
    if "red"not in fruitmand:
        print("er is geen rood fruit in deze fruitmand")
        break
    else:
        lijst.remove("red")
        print(lijst)