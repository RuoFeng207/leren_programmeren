import random
for kaart in range(2):
    kaarten=["aas",2,3,4,5,6,7,8,9,10,11,12,13]

    kaart=random.choice(kaarten)
    
    print(kaart)
    kaarten.remove(kaart)
    print(kaarten)
