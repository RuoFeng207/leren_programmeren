deelnemers =[]
for x in range(3):
    while True:
        naam = input("Wat is je naam? ")
        try:
            naam= float(naam)
            print("Je naam mag geen cijfers bevatten")
        except ValueError:
            deelnemers.append(naam)
        
        while True:
            if naam in deelnemers:
                print("Deze naam zit al in de lijst.")
            else:
                deelnemers.append(naam)
                break

        


#     while True:
#         while True:
#             naam=input("Wat is jou naam? ")
#             if naam.isalpha():
#                 naam = naam.capitalize()
#                 print(naam)
#                 break
#             else:
#                 print("Je naam mag geen cijfers of tekens bevatten.")
#                 print("")
        # if naam in deelnemers:
        #     print("Deze naam zit al in de lijst.")
        # else:
        #     deelnemers.append(naam)
        #     break

# print(deelnemers)