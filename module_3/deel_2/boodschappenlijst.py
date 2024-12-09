hoeveel = []
product = []

while True:
    while True:
        artikel = input("Welk artikel wilt u toevoegen? ").lower()
        if not artikel.isalpha():
            print("U kunt hier geen cijfer invoeren.")
            print("")
        else:
            break
    print("")

    if artikel in product:
        index = product.index(artikel) 
        while True:
            try:
                aantal = int(input(f"Hoeveel wilt u daarvan toevoegen? U heeft er al {hoeveel[index]} van. "))
                hoeveel[index] += aantal 
                break
            except ValueError:
                print("U kunt hier alleen hele getallen invoeren.")
                print("")
    else:
        product.append(artikel)  
        while True:
            try:
                aantal = int(input("Hoeveel wilt u daarvan toevoegen? ").lower())
                hoeveel.append(aantal)  
                break
            except ValueError:
                print("U kunt hier alleen hele getallen invoeren.")
                print("")

    while True:
        nogeens = input("Wilt u nog iets bestellen? ").lower()
        if nogeens == "ja" or nogeens == "nee":
            break
        else:
            print("")
            print("U kunt alleen maar ja of nee invullen.")
    print("")
    
    if nogeens == "nee":
        break

print("========Bon=======")
for i in range(len(product)):
    print(f"{hoeveel[i]} x {product[i]}")