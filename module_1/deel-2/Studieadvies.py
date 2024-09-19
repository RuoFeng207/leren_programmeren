from studieadviestext import * 
max_score= 28
#met bonus opdracht 1 en 2
# inlijding
print(STUDIEDOKTER_TITEL)
AANTAL_WEKEN_VRAAG = int(input( 'Hoeveel weken ben je al bezig met de opleiding? '))
print(f"{AANTAL_WEKEN_VRAAG} weken oke")


#vraag 1
while True:
    score = 0
    print(f"Vraag 1: {COMPETENTIE_STELLING_1}")
    andwoord= int(input(f"{OPTIES}\n\n" ))
    if andwoord == 0:
        score=score +0
    elif andwoord==1:
        score=score+1
    elif andwoord ==2:
        score=score+2
    elif andwoord==3:
        score=score +3
    elif andwoord==4:
        score=score +4
   
    else:
        print("Deze optie is niet mogelijk probeer opnieuw\n")
    
    # #vraag 2

    print(f"Vraag 2: {COMPETENTIE_STELLING_2}")
    andwoord= int(input(f"{OPTIES}\n\n" ))
    if andwoord == 0:
        score=score +0
    elif andwoord==1:
        score=score+1
    elif andwoord ==2:
        score=score+2
    elif andwoord==3:
        score=score +3
    elif andwoord==4:
        score=score +4
    else:
        print("Deze optie is niet mogelijk probeer opnieuw\n")
    
    #vraag 3

    print(f"Vraag 3: {COMPETENTIE_STELLING_3}")
    andwoord= int(input(f"{OPTIES}\n\n" ))
    if andwoord == 0:
        score=score +0
    elif andwoord==1:
        score=score+1
    elif andwoord ==2:
        score=score+2
    elif andwoord==3:
        score=score +3
    elif andwoord==4:
        score=score +4
   
    else:
        print("Deze optie is niet mogelijk probeer opnieuw\n")
    
    #vraag 4

    print(f"Vraag 4: {COMPETENTIE_STELLING_4}")
    andwoord= int(input(f"{OPTIES}\n\n" ))
    if andwoord == 0:
        score=score +0
    elif andwoord==1:
        score=score+1
    elif andwoord ==2:
        score=score+2
    elif andwoord==3:
        score=score +3
    elif andwoord==4:
        score=score +4
   
    else:
        print("Deze optie is niet mogelijk probeer opnieuw\n")

    #vraag 5

    print(f"Vraag 5: {COMPETENTIE_STELLING_5}")
    andwoord= int(input(f"{OPTIES}\n\n" ))
    if andwoord == 0:
        score=score +0
    elif andwoord==1:
        score=score+1
    elif andwoord ==2:
        score=score+2
    elif andwoord==3:
        score=score +3
    elif andwoord==4:
        score=score +4
   
    else:
        print("Deze optie is niet mogelijk probeer opnieuw\n")
    
    if AANTAL_WEKEN_VRAAG >9:
    #vraag 6
    
        print(f"Vraag 6: {COMPETENTIE_STELLING_6}")
        andwoord= int(input(f"{OPTIES}\n\n" ))
        if andwoord == 0:
            score=score +0
        elif andwoord==1:
            score=score+1
        elif andwoord ==2:
            score=score+2
        elif andwoord==3:
            score=score +3
        elif andwoord==4:
            score=score +4
        else:
            print("Deze optie is niet mogelijk probeer opnieuw\n")
        
        #vraag 7
        
        print(f"Vraag 7: {COMPETENTIE_STELLING_7}")
        andwoord= int(input(f"{OPTIES}\n\n" ))
        if andwoord == 0:
            score=score +0
        elif andwoord==1:
            score=score+1
        elif andwoord ==2:
            score=score+2
        elif andwoord==3:
            score=score +3
        elif andwoord==4:
            score=score +4
    
        else:
            print("Deze optie is niet mogelijk probeer opnieuw\n")
    break

cijfer =score/7




if cijfer <=2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif cijfer >=3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
   print(COMPETENTIE_ADVIES_GERUSTSTELLEND)


