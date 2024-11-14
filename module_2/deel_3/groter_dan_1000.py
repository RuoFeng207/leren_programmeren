lijst=[]
getal = 50
#visueel
for x in range(10):
    lijst.append(getal) #toevoegen lijst

    getal+=1  
    var = ""
    for y in lijst:
        var+=(f"{y} ")
    lijst.append("+")
    
    #berekenen
    som = 2
    print(f"{var} = {som}")     
