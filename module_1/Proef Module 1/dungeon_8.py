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
items = ['schild',"zwaart","sleutel"]
rupee =0
schatkist =False

# def vijand
def vijand(gevecht):
   return gevecht
#===[kamer 3]===#
def kamer_3(rupee):
  print("")
  print("Je stapt een grote kamer binnen, en je ziet een kraampje met daar achter een goblin.")
  print("Op het bordje er naast staat wapens 1 rupee.")
  while True:
      #kopen 
      while True:
      
        kopen = input("Wil je wapens kopen bij de goblin? ")
        kopen=kopen.lower()
        if kopen =="ja":
          break
        elif kopen =="nee":
          break
        else: 
          print("Deze optie is niet geldig je moet ja of nee antwoorden")


      if kopen =="ja":

        while True:
          
          print(f"je kan kiezen uit {items}")
          
          item = input("Wat kies je? ")
          if item == "schild":
            player_defense=+1
          elif item=="zwaart":
            player_attack=+1
          elif item =="sleutel":
            schatkist= True
          print("")
          item=item.lower()
          if item in items:
            break
          else:
            print("De goblin verkoopt dit voorwerp niet")

        if item in items:
          rupee -=1
          items.remove(item)
          print(f"Je hebt een {item} gekocht en hebt {rupee} rupee(s) over")
          
          if items ==[]:
            uitverkocht =print("De goblin is uit verkocht")
            print("")
            print("Blij met je nieuwe  spullen loop je veder")
            print("")
            break
          else:
            if rupee>=1:
              print("Wil je nog wat kopen")
            else:
              print("O het lijt er op dat je geen rupees meer hebt")
              print("Je kan dus niks meer kopen.")
              print("bij met je nieuwe aankoop(en) loop je veder")
              break

      elif kopen =="nee":
        print("Je besluit niks te kopen en loopt door")
        break
      return player_defense,player_attack,schatkist,uitverkocht

#kamer 7
def kamer_7(rupee):
   kans_rupee=random.randint(1,10)
   if kans_rupee ==1:
      print("Je doet de deur open maar...")
      print("Um dat is vreemd er is niks in deze kamer, je zou denken dat er meer te doen was in een dungeon.")
      print("")
      
      time.sleep(3)
      print("Je kijkt wat beter om je heen en ziet 2 deuren, op een deur van staat kamer 2 en op de andere staat kamer 8")
      print("Welke kamer neem jij?")
   else:
      print("Je doet hem open en ziet iets schitteren een rupee!")
      rupee =rupee+1
      print("Je loopt er heen en pakt hem op")
      print(f"je hebt nu {rupee} rupee(s) in je inventory")
      print("Je kijkt wat beter om je heen en ziet 2 deuren, op een deur van staat kamer 2 en op de andere staat kamer 8")
      print("Welke kamer neem jij?")
      print("")
      


#kamer 8

def kamer_8(rupee:int,player_health:int)->int:
    print("Je komt in een kamer en ziet een gokmachien")
    print("Er staat een bortje bij ")
    print("----------------------------De spel regels-----------------------------")
    print("Als het aantal ogen groter is dan 7 winst is aantal rupees x 2")
    print("Als het aantal ogen minder is dan 7 verlis is player health -1")
    print("Als het aantal ogen gelijk is aan 7 winst +1 rupee en +4 player health")
    print("-----------------------------------------------------------------------")
    while True:
        while True:
          gedobbeld = random.randint(1,12)
          if player_health ==0:
           
            print("Game Over")
            exit()
          else:

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
            print(f"Je inzet is {player_health} player health punten")
            time.sleep(1)
        
            if gedobbeld <7:
                player_health=player_health-1
                print(f"Je goeide een {gedobbeld}!")
                print("Helaas je hebt veloren.")
                print(f"Je hebt nu {rupee} rupees en {player_health} palyer health punt(en)")
                
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
            break
    print("Je ziet 2 deuren naar 2 nieuwe kamers een gaat naar kamer 3 en de ander naar kamer 9")
    print("Welke kamer neem je?")
    while True:
       kamer=input("Je neemt kamer: ")
       if kamer =="3":
          break
       elif kamer =="9":
          break
       else:
          print("Deze optie is ongeldig probeer opnieuw")
          print("")
    if kamer== "3":
       print(kamer_3(rupee))
    elif kamer=="9":
       print(kamer_9(player_health,player_defense))   
       print(kamer_3(rupee))
     
#===[kamer 9]===#
def kamer_9(player_health,player_defense):
   kans=random.randint(1,2)
   if kans ==1:
      print("Je voelt een soort vreemde kacht je voelt je opeens veel energieker")
      player_health=player_health+1
      print(f"Je kijt naar je health bar en ziet dat je {player_health} punten hebt ")
   elif kans==2:
      print("Je voelt een soort vreemde kacht je voelt je opeens als of je on aantasbaar bent")
      player_defense=player_defense+1
      print(f"Je kijt naar je defense bar en ziet dat je {player_defense} defense punten hebt")

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(4)

# === [kamer 7] === #
print(kamer_7(rupee))

while True:
  kamer=input("Je neemt kamer: ")
  if kamer =="2":
    break
  elif kamer =="8":
    break
  else:
    print("Deze optie is ongeldig probeer opnieuw")
  print("")
#kamer 2
if kamer == "2":
    print("")
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print(f'Daarboven zie je een som staan {getal1}{operator}{getal2}= ')

    antwoord =int(input("wat is jouw andwoord? "))
    if code != antwoord:
        print("dit antwoord is niet corect.")
        time.sleep(2)
    
    else:
        print("")
        print("Gelukt je hebt de code gekraakt!")
        print('Het stadbeeld laat zijn rupee vallen en je pakt hem op')
        rupee=rupee+1
        print(f"je hebt nu {rupee} rupee(s) in je inventory")

    print('Achter het standbeeld zie je 2 deuren, een gaat naar kamer 6 en de ander naar kamer 8')
    print("Welke kamer neem jij?")

    while True:
        kamer=input("Je neemt kamer: ")
        if kamer =="6":
            break
        elif kamer =="8":
            break
        else:
            print("Deze optie is ongeldig probeer opnieuw")
            print("")

    if kamer =="8":
       print(kamer_8(rupee=rupee,player_health=player_health))
#===[kamer 6]===#
    else:
       print("")
       print("Je gaat de kamer in en")
       print('Je loopt tegen een zombie aan.')
       print(f"Je hebt {player_health} health punten,")
       print(f"Je doet de zombie per aanval {player_attack} punten schade toe ")
       print(f'Jou defense is {player_defense} punten')
       print("")   
       time.sleep(4)
    
       print(f"De zombie heeft {vijand(gevecht=2)} health punten,")
       print(f"Hij doet jou per aanval {vijand(gevecht=1)} punten schade toe ")
       print(f'Zijn defense is {vijand(gevecht=0)} punten')
       time.sleep(4)
       print("")
       vijand_hit_damage = (vijand(gevecht=0) - player_defense)
       if vijand_hit_damage <= 0:
          print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
          print(kamer_8(rupee=rupee,player_health=player_health))
       else:
        zombie_attack_amount = math.ceil(player_health / vijand_hit_damage)
            
        player_hit_damage = (player_attack - vijand(gevecht=0))
        player_attack_amount = math.ceil(vijand(gevecht=2) / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
            print(kamer_8(rupee=rupee,player_health=player_health))
            print("")
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()
    print("Je ziet 2 nieuwe deuren een naar 3 en de ander naar kamer 8")
    print("Welke kamer neem je?")
    while True:
        kamer=input("Je neemt kamer: ")
        if kamer =="3":
            break
        elif kamer =="8":
            break
        else:
            print("Deze optie is ongeldig probeer opnieuw")
            print("")
    if kamer == "3":
       print(kamer_3(rupee))
    elif kamer=="8":
       print(kamer_8(rupee))

       
else:
  antwoord = quit
  #kamer 8
  print(kamer_8(rupee=rupee,player_health=player_health))
  #kamer 9
print(kamer_9(player_health,player_defense))
#===[kamer 3]===#
print(kamer_3(rupee))
# #===[kamer 4]===#
print('Je loopt tegen een man met zwaard aan.')
print(f"Je hebt {player_health} health punten,")
print(f"Je doet de man met zwaard per aanval {player_attack} punten schade toe ")
print(f'Jou defense is {player_defense} punten')
print("")

print(f"De man met zwaard heeft {vijand(gevecht=3)} health punten,")
print(f"Hij doet jou per aanval {vijand(gevecht=2)} punten schade toe ")
print(f'Zijn defense is {vijand(gevecht=0)} punten')
time.sleep(4)
vijand_hit_damage = (vijand(gevecht=0) - player_defense)
if vijand_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de man met zwaard, hij kan je geen schade doen.')
else:
    vijand_attack_amount = math.ceil(player_health / vijand_hit_damage)
    
    player_hit_damage = (player_attack - vijand(gevecht=0))
    player_attack_amount = math.ceil(vijand(gevecht=2) / player_hit_damage)

    if player_attack_amount < vijand_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de man met zwaard.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de man met zwaard te sterk voor je.')
        print('Game over.')
        exit()
#===[kamer 5]===#
time.sleep(3)
print("")
print('Voorzichtig open je de deur, je wilt niet nog meeer vijanden tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print("Je probeert hem te open en maar...")
time.sleep(2)
print("")
print("Hij zit op slot! ")
if schatkist==True:
   print("Opeens herinner je je de sluitel die je hebt gekocht bij de goblin ")
   print("Je probeert hem uit en... HIJ PAST!")
   print("Je neemt de buit mee")
   print("Gefeliciteerd je hebt gewonnen")
else:
   print("Je voelt in je zaken naar iets waar mee je de kist kan openen een slutel of zo maar niks.")
   print("Helaas je hebt veloren.")
   print("Game over")