deelnemers =[]
for x in range(3):
    while True:
        naam=input("Wat is jou naam? ")
        if naam.isalpha():
            naam.capitalize()
            while True:
                
                if naam in deelnemers:
                    print("Deze naam is al aanwezig kies een andere naam")
                    print("")
                    
                else:
                    deelnemers.append(naam)
                    break
            break
        else:
            print("Je naam mag geen cijfers of tekens bevatten.")
            print("")


