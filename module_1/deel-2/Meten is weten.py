getal_1 = input("Geef getal 1: ")
getal_2 = input("Geef getal 2: ")

if getal_1 > getal_2:
    print(f"{getal_1} is groter dan {getal_2}")
    max = getal_1
    print(f"Max getal is {max}")
elif getal_2 >getal_1:
    print(f"{getal_2} is groter dan {getal_1}")
    max = getal_2
    print(f"Max getal is {max}")
else:
    print(f"{getal_1} is gelijk aan {getal_2}")