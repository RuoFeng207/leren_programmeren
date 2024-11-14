lijst=[]
getal = 50
num =0
#visueel
while True:
    lijst.append(getal) #toevoegen lijst

    getal+=1
    num+=1
    var = ""
    teller =0
    for y in lijst:
        if teller==0:
            var +=(f"{y}")
        else:var+=(f"+ {y} ")
        teller+=1
    #berekenen
   

    som =sum(lijst)
    print(f"{num}. {var}= {som}")  
    if som>1000:
        break   

#zoek uit teller
