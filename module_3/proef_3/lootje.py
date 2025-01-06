deelnemers =[]
for x in range(3):
    while True:
        while True:
            naam=input("Wat is jou naam? ")
            if naam.isalpha():
                naam = naam.capitalize()
                print(naam)
                break
            else:
                print("Je naam mag geen cijfers of tekens bevatten.")
                print("")
        if naam in deelnemers:
            print("Deze naam zit al in de lijst.")
        else:
            deelnemers.append(naam)
            break

print(deelnemers)