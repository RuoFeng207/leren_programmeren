# def test(Naam): #functie, parameter
#     print("Hallo",Naam) #print string parameter
# test("jan") #argument


def getal(getal1: int, getal2:int)-> int:

    return getal1 +getal2
print(getal(getal1=1, getal2=2))


def tekst(hallo:str, aantal:int ):
    for i in range(aantal):
        print(hallo) 

tekst(hallo="hallo",aantal=3)
print("------------")
tekst(hallo="doei",aantal=6)


def aanval(defense:int,health:int,attack)->int:
    return defense, health,attack
print(aanval(defense=1,health=2,attack=3))

def kamer(deur_1:str):
    return deur_1
    
  

