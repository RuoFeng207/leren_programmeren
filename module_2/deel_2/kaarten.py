import random
symbool = ["harte", "klaveren","schoppen","ruiten"]
set = ["aas","2","3","4","5","6","7","8","9","10","boer","vrouw","koning"]
stapel = 54
dek=[]
for keer in range (4):
    for kaart in set:
        kaart =(f"{symbool[keer]} {kaart}")
        dek.append(kaart)
        
for x in range(1,8):
    keus = random.choice(dek)
    hand= (f"kaart {x}: {keus}")
    stapel= stapel-1
    dek.remove(keus)
    print(hand)
print("")
print(f"dek ({stapel} kaarten): {dek}")