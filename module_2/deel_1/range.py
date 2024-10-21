vraag = int(input("Hoeveel lijsten wil je zien? "))
lijst_2=[]
for x in range(1,vraag+1):
    
    
    lengte = int(input(f"Hoelang wil je lijst {x}: "))
    lijst_1=[]

    for y in range(1,lengte+1):
        lijst_1.append(y)

    lijst_2.append(lijst_1)
print(lijst_2)