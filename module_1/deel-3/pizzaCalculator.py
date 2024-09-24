
#nummer chek
# Keuze pizza
while True:

    try:
        small= int(input("Hoeveel small pizza's wilt u? "))
        break
    except:
        print("Dit is geen heel nummer ")

while True:
    try:
        medium = int(input("Hoeveel medium pizza's wilt u? "))
        break
    except:
        print("Dit is geen heel nummer")
        
while True:
    try:
        large = int(input("Hoeveel large pizza's wilt u? "))
        break
    except:
        print("Dit is geen heel nummer")

# #prijs pizza
prijs_small = 6.57
prijs_medium = 8.95
prijs_large = 12.99

# chek =<0
print("****************************KASSA BON****************************")
if small<=0:
    quit
else:
    print(f"Pizza's small:      {small}x{prijs_small}= {small*prijs_small}")  
if medium<=0:
    quit
else:
     print(f"Pizza's medium:     {medium}x{prijs_medium}= {medium*prijs_medium}")
if large<=0:
    quit
else:
    print(f"Pizza's large:      {large}x{prijs_large}= {small*prijs_large}") 

if small<=0 and medium<=0 and large<=0:
    print("Je hebt niks besteld")
else:
    totaal=(small*prijs_small + medium*prijs_medium + large*prijs_large)
    totaal =round(totaal,2)
    print(f"Totaal:            {totaal}")   

print("-----------------------------------------------------------------")
 
#1.0
# # Keuze pizza
# small=int(input("Hoeveel small pizza's wilt u? "))
# medium = int(input("Hoeveel medium pizza's wilt u? "))
# large = int(input("Hoeveel large pizza's wilt u? "))
# # #prijs pizza
# prijs_small = 6.57
# prijs_medium = 8.95
# prijs_large = 12.99
# #som 
# totaal=(small*prijs_small + medium*prijs_medium + large*prijs_large)
# totaal =round(totaal,2)
# print("****************************KASSA BON****************************")
# print(f"Pizza's small:      {small}x{prijs_small}= {small*prijs_small}")  
# print(f"Pizza's medium:     {medium}x{prijs_medium}= {medium*prijs_medium}") 
# print(f"Pizza's large:      {large}x{prijs_large}= {small*prijs_large}") 
# print(f"Totaal:            {totaal}")                                    
# print("-----------------------------------------------------------------")