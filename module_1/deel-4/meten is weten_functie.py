def num1_grootst(num1, num2):
   
    if num1 > num2:
        print("Getal 1 is groter dan getal 2")
        print(f"Max getal is {num1}")
        print(f"Minimum getal is {num2}")
    elif num1 < num2:
        print("Getal 2 is groter dan getal 1")
        print(f"Max getal is {num2}")
        print(f"Minimum getal is {num1}")
    else:
        print("Getal 1 en 2 zijn even groot ")
        print("er is geen minimum of maximum")


num1 = int(input("Geef getal 1: "))
num2= int(input("Geef getal 2: "))

num1_grootst(num1,num2)
