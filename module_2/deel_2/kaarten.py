import random
for keer in range (4):
    for kaart in range(1,14):
        if kaart ==1:
            kaart = "aas"
        elif kaart==11:
            kaart ="boer"
        elif kaart ==12:
            kaart= "vrouw"
        elif kaart == 13:
            kaart ="koning"
        if keer ==0:
            print(f"harten {kaart}")
        elif keer ==1:
            print(f"schoppen {kaart}")
        elif keer ==2:
            print(f"klaveren {kaart}")
        else:
            print(f"ruiten {kaart}")