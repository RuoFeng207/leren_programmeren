import time, math,random

player_attack = 1
player_defense = 0
player_health = 3
# numpad kamer 2
getal1= random.randint(10,25)
getal2 = random.randint(-5,75)
operators =["+","-","x"]
operator= random.choice(operators)
if operator =="+":
  code =  getal1+getal2
if operator=="-":
  code = getal1-getal2
if operator =="x":
  code = getal1*getal2

#Goblin zooi
items = ['schild',"zwaart"]
rupee =1
# def vijand
def vijand(gevecht):
   return gevecht
#kamer 8
gedobbeld = random.randint(1,12)
def kamer_8(rupee:int,player_health:int)->int:
    print("Je komt in een kamer en ziet een gokmachien")
    print("Er staat een bortje bij ")
    print("----------------------------De spel regels-----------------------------")
    print("Als het aantal ogen groter is dan 7 winst is aantal rupees x 2")
    print("Als het aantal ogen minder is dan 7 verlis is rupee en player health -1")
    print("Als het aantal ogen gelijk is aan 7 winst +1 rupee en +4 player health")
    print("-----------------------------------------------------------------------")
    while True:
        gebruik = input("wil je de gokmachiene gebruiken?\n")
        gebruik=gebruik.lower()
        if gebruik =="ja":
            break
        elif gebruik =="nee":
            break
        else: 
          print("Deze optie is niet geldig je moet ja of nee antwoorden")
        
    if gebruik=="ja":
        print("")
        print(f"Je inzet is {rupee} rupee en {player_health} player health punten")
        time.sleep(1)
    
        if gedobbeld <7:
            player_health=player_health-1
            rupee=rupee-1
            print(f"Je goeide een {gedobbeld}!")
            print("Helaas je hebt veloren.")
            print(f"Je hebt nog {rupee} rupees en {player_health} palyer health punten")
        elif gedobbeld>7:
            rupee=rupee*2
            print(f"Je goeide een {gedobbeld}!")
            print(f"gefeliciteerd je hebt gewonennen je hebt nu {rupee} rupees ")

        else:
            player_health+4
            rupee=+1
            print(f"Je goeide een {gedobbeld}!")
            print(f"gefeliciteerd je hebt gewonennen je hebt nu{rupee} aantal rupees en {player_health} player health punten")
    elif "nee":
        print("Het lijkt je veel te riskant en je loopt door.")

print(kamer_8(rupee,player_health))


  



    