
#nummer chek
# Keuze pizza
small =-1
medium =-1
large=-1
while small<0:

    try:
        small= int(input("Hoeveel small pizza's wilt u? "))
        if small<0:
            print("Je kan geen negatieve getallen invoeren")
    except:
        print("Dit is geen heel nummer ")

while medium<0:
    try:
        medium = int(input("Hoeveel medium pizza's wilt u? "))
        if medium<0:
            print("Je kan geen negatieve getallen invoeren ")
    except:
        print("Dit is geen heel nummer")
        
while large<0:
    try:
        large = int(input("Hoeveel large pizza's wilt u? "))
        if large<0:
            print("Je kan geen negatieve getallen invoeren")
    except:
        print("Dit is geen heel nummer")

# #prijs pizza
prijs_small = 6.57
prijs_medium = 8.95
prijs_large = 12.99
totaal = 0
# chek =<0
print("****************************KASSA BON****************************")
if small<=0:
    quit
else:
    print(f"Pizza's small:      {small}x{prijs_small}= {small*prijs_small}") 
    totaal = totaal+small*prijs_small
if medium<=0:
    quit
else:
     print(f"Pizza's medium:     {medium}x{prijs_medium}= {medium*prijs_medium}")
     totaal = totaal+medium*prijs_medium
if large<=0:
    quit
else:
    print(f"Pizza's large:      {large}x{prijs_large}= {large*prijs_large}")
    totaal= totaal+large*prijs_large

if small==0 and medium==0 and large==0:
    print("Je hebt niks besteld")
else:
    
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