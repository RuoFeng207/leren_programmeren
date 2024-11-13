import random
# symbool = ["harte", "klaveren","schoppen","ruiten"]
# set = ["aas","2","3","4","5","6","7","8","9","10","boer","vrouw","koning"]
# kaarten = 0
# dek=[]
# for keer in range (4):
#     for kaart in set:
#         kaarten=kaarten+1
#         kaart =(f"{symbool[keer]} {kaart}")
#         dek.append(kaart)
        
        
# for x in range(1,8):
#     keus = random.choice(dek)
#     hand= (f"kaart {x}: {keus}")
#     kaarten=kaarten-1
#     dek.remove(keus)
#     print(hand)
# print("")
# print(f"dek {kaarten} kaarten): {dek}")
# # aanpassen

symbool = ["harte", "klaveren","schoppen","ruiten"]
set = ["aas","2","3","4","5","6","7","8","9","10","boer","vrouw","koning"]
stapel = 0
dek=[]
#dek genereren
for keer in range (4):
 for kaart in set:
    stapel=stapel+1
    kaart =(f"{symbool[keer]} {kaart}")
    dek.append(kaart)
stapel=stapel+2
dek.append("joker zwart")
dek.append("joker rood")
print(dek)

for x in range(1,8):
    keus = random.choice(dek)
    hand= (f"kaart {x}: {keus}")
    stapel= stapel-1
    dek.remove(keus)
    print(hand)
print("")
print(f"dek ({stapel} kaarten): {dek}")