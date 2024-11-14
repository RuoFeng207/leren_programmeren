lijst=[]
getal = 50
#visueel
for x in range(10):
    lijst.append(getal) #toevoegen lijst

    getal+=1  
    var = ""
    for y in lijst:
        if x>0:
            var+=(f"+{y} ")
    #berekenen
    if x >0:

        som =sum(lijst)
        print(f"{var}= {som}")     

