from functions_rekenen import *
def getal_afhandelen_2():
    while True:
        try:
            n1 = float(input("voer getal 1 in: "))
            break
        except:
            print("Je kan alleen maar cijfers")
    while True:
        try:
           n2 = float(input("voer getal 2 in: "))
           break
        except:
            print("Je kan alleen maar cijfers invoeren")
    return n1, n2

def getal_afhandel():
    while True:
        try:
            n1 = float(input("voer een getal in: "))
            break
        except:
            print("Je kan alleen cijfers invoeren")
    return n1
while True:
    print("Wat wild u doen?")
    print("A) getallen optellen")
    print("B) getallen aftrekken")
    print("C) getallen vermenigvuldigen")
    print("D) getallen delen")
    print("E) getallen ophogen")
    print("F) getallen verlagen")
    print("G) getallen verdubbelen")
    print("H) getallen halveren")
    print("I) niet")

    lijst = ["a","b","c","d","e","f","g","h","i"]
    while True:
        choice = input("kies: ").lower()
        if choice in lijst:
            break
        else:
            print("")
            print("Deze optie is niet mogelijk")
    if choice == "a":
        n1,n2 = getal_afhandelen_2()
        som = addition(n1,n2)
        print("----------------------------")
        print(f"de uitkomst van {n1} + {n2} = {som:.1f}")
    if choice == "b":
        n1,n2 = getal_afhandelen_2()
        som = subtraction(n1,n2)
        print("----------------------------")
        print(f"de uitkomst van {n1} - {n2} = {som:.1f}")
    if choice == "c":
        n1,n2 = getal_afhandelen_2()
        som = multiplication(n1,n2)
    if choice == "d":
        n1,n2= getal_afhandelen_2()
        som = division(n1,n2)
        print("----------------------------")
        print(f"de uitkomst van {n1} : {n2} = {som:.1f}")
    if choice == "e":
        n2 = 1
        n1 = getal_afhandel()
        som = addition(n1,n2)
        print("----------------------------")
        print(f"de uitkomst van {n1} + {n2} = {som:.1f}")
    if choice == "f":
        n2 = 1
        n1 = getal_afhandel()
        som = subtraction(n1,n2)
        print("----------------------------")
        print(f"de uitkomst van {n1} + {n2} = {som:.1f}")
    if choice == "g":
        n2 = 2
        n1 = getal_afhandel()
        som = multiplication(n1,n2)
        print("----------------------------")
        print(f"de verdubbeling van {n1} = {som:.1f}")
    if choice == "h":
        n2 = 2
        n1 = getal_afhandel()
        som = subtraction(n1,n2)
        print("----------------------------")
        print(f"de halvering van {n1} = {som:.1f}")
    if choice == "i":
        print("Oke doei")
        break
    print("")