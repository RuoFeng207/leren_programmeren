getal_1 = int(input("Geef getal 1: "))
getal_2 = int(input("Geef getal 2: "))

if getal_1 > getal_2:
    print(f"{getal_1} is groter dan {getal_2}")
    max = getal_1
    print(f"Max getal is {max}")
    print(f"{getal_2} is kleiner dan {getal_1}")
    Min = getal_2
    print(f"Minimum getal is {Min}")
  
elif getal_1< getal_2:
    print(f"{getal_2} is groter dan {getal_1}")
    max = getal_2
    # print(f"Max getal is {max}")
    print(f"{getal_1} is kleiner dan {getal_2}")
    Min = getal_1
    # print(f"Minimum getal is {Min}")
else:
    print(f"{getal_1} is gelijk aan {getal_2}")
    print("Er is geen maximum of minimum.")
print(f"Max getal is {max}")
print(f"Minimum getal is {Min}")