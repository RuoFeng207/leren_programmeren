
def vraag_getal(aantal):
    antwoord = input("Voer het "+antwoord+" getal in: ")
    getal = int(aantal)
    return getal

getal_2 = vraag_getal("tweede")
getal_1 = vraag_getal("eerste")

def deel_getallen(a,b):
    
    antwoord = int(a / b)
    return antwoord

resultaat= getal_1/getal_2
if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    print ("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))
    resultaat = deel_getallen(getal_1, getal_2)

