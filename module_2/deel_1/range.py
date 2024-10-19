vraag = int(input("Hoeveel lijsten wilt u zien? "))
lijst=[]
for i in range(1,vraag+1):
    lengte =int(input(f"Hoelang moet lijst {i} zijn "))
    for x in range (1,lengte+1):
        lijst.append(x)

print(lijst)