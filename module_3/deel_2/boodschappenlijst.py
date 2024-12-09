hoeveel =[]
product=[]

while True:
    artiekel = input("Welk artikel wilt u toevoegen? ")
    if not artiekel.isalpha():
        print("U kunt hier geen cijfer invoeren.")
        print("")
    else:
        break
print("")
product.append(artiekel)

for a in product:
    print(a)



while True:
    try:
        aantal = int(input("Hoeveel wilt u daarvan toevoegen? "))
        break
    except ValueError:
        print("U kunt hier alleen hele getallen invoeren.")
        print("")

hoeveel.append(aantal)

for x in (hoeveel):
    print(x)




