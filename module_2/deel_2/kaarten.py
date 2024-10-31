import random
hand = []
stapel = []
teller=0
# dek kaarten
while True:
    set = ["aas",2,3,4,5,6,7,8,9,10,"boer","vrouw","koning"]
    nummer= random.choice(set)
    simboolen =["harte", "klaveren","schoppen","ruiten"]
    kaart_simbool = random.choice(simboolen)
    kaart =(f"{kaart_simbool} {nummer}")
    if kaart not in hand:
        hand.append(kaart)
        teller+=1
    elif teller ==7:
        break
print(hand)