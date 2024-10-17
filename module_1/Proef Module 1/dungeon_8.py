import time, math,random
# kamers 

kamer_2 = True
kamer_6 = True
kamer_8 = True
kamer_9 = True

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
items = ['schild',"zwaard","sleutel"]
rupee =0
schatkist =False
#gevecht
def vijand(vijand:str,vijand_health: int, vijand_attack:int,vijand_defense:int)->str:
    print(f"De {vijand} heeft {vijand_health} health punten")
    print(f"Hij doet je per aanval {vijand_attack} punte schade toe")
    print(f"En hij heeft {vijand_defense} defense punten")
    print("")
    time.sleep(2)
    zombie_hit_damage = (vijand_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
        player_hit_damage = (player_attack - vijand_defense)
        player_attack_amount = math.ceil(vijand_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de {vijand}.')
            print(f'Je health is nu {player_health}.')
        else:
            print(f'Helaas is de {vijand} te sterk voor je.')
            print('Game over.')
            exit()

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(4)

# === [kamer 7] === #
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
  time.sleep(3)

  #keuze kamer 
  while True:
        kamer=input("Je neemt kamer: ")
        if kamer =="2":
           break
        elif kamer =="8":
            kamer_2 = False
            kamer_6 = False
            break
        else:
            print("Deze optie is ongeldig probeer opnieuw")
            print("")

# === [kamer 2] === #
if kamer_2== True:
  print("")
  print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
  print('Het standbeeld heeft een rupee vast.')
  print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
  print(f'Daarboven zie je een som staan {getal1}{operator}{getal2}= ')

  antwoord =int(input("wat is jouw andwoord? "))
  if code != antwoord:
      print("dit antwoord is niet corect.")
      print("")
      time.sleep(2)
  else:
      print("")
      print("Gelukt je hebt de code gekraakt!")
      print('Het stadbeeld laat zijn rupee vallen en je pakt hem op')
      rupee=rupee+1
      print(f"je hebt nu {rupee} rupee(s) in je inventory")

  print('Achter het standbeeld zie je 2 deuren, een gaat naar kamer 6 en de ander naar kamer 8')
  print("Welke kamer neem jij?")

    #keuze kamer 
  while True:
        kamer=input("Je neemt kamer: ")
        if kamer =="6":
           break
        elif kamer =="8":
            kamer_6 = False
            break
        else:
            print("Deze optie is ongeldig probeer opnieuw")
            print("")

  
  time.sleep(3)
#===[kamer 6]===#
if kamer_6 == True:
  print("")
  print('Je loopt tegen een zombie aan.')
  print(f"Je hebt {player_health} health punten,")
  print(f"Je doet de zombie per aanval {player_attack} punten schade toe ")
  print(f'Jou defnse is {player_defense} punten')
  print("")
  time.sleep(2)

  vijand("Zombie",2,1,0)
  print("Je ziet 2 nieuwe deuren een naar 3 en de ander naar kamer 8")
  print("Welke kamer neem je?")

  #kamer keuze
  while True:
        kamer=input("Je neemt kamer: ")
        if kamer =="8":
           break
        elif kamer =="3":
            kamer_8 = False
            kamer_9 = False
            break
        else:
            print("Deze optie is ongeldig probeer opnieuw")
            print("")
  

#===[kamer 8]===#
if kamer_8== True:
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
              print(f"gefeliciteerd je hebt gewonennen je hebt nu {rupee} aantal rupees en {player_health} player health punten")
      
      elif "nee":
          print("Het lijkt je veel te riskant en je loopt door.")
          print("")
          break
  print("Je ziet 2 deuren naar 2 nieuwe kamers een gaat naar kamer 3 en de ander naar kamer 9")
  print("Welke kamer neem je?")
  #kamer keuze 
  while True:
        kamer=input("Je neemt kamer: ")
        if kamer =="9":
           break
        elif kamer =="3":
            kamer_9 = False
            break
        else:
            print("Deze optie is ongeldig probeer opnieuw")
            print("")

#===[kamer 9]===#
if kamer_9 == True:
  kans=random.randint(1,2)
  if kans ==1:
    print("Je voelt een soort vreemde kacht je voelt je opeens veel energieker")
    player_health=player_health+1
    print(f"Je kijt naar je health bar en ziet dat je {player_health} punten hebt ")
  elif kans==2:
    print("Je voelt een soort vreemde kacht je voelt je opeens als of je on aantasbaar bent")
    player_defense=player_defense+1
    print(f"Je kijt naar je defense bar en ziet dat je {player_defense} defense punten hebt")
  time.sleep(3)

  #===[kamer 3]===#
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
            player_defense=player_defense+1
            print("Je hebt een schild gekocht je defense gaat met +1 omhoog ")
            print(f"Je kijkt naar je defense bar en ziet dat je {player_defense} punen hebt")
          elif item=="zwaard":
            player_attack=player_attack+2
            print("Je hebt een zwaart gekocht je attack gaat met +2 omhoog ")
            print(f"Met dit zwaart ben je veel sterker je attack is nu {player_attack} punten")
          elif item =="sleutel":
            schatkist= True
            print("Je hebt een sleutel gekocht mischien komt het nog van pas")
          print("")
          item=item.lower()
          if item in items:
            break
          else:
            print("De goblin verkoopt dit voorwerp niet")

        if item in items:
          rupee -=1
          items.remove(item)
          
          
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
              print("O het lijkt er op dat je geen rupees meer hebt")
              print("Je kan dus niks meer kopen.")
              print("bij met je nieuwe aankoop(en) loop je veder")
              break

      elif kopen =="nee":
        print("Je besluit niks te kopen en loopt door")
        break
# #===[kamer 4]===#
print("")
print('Je loopt tegen een zombie aan.')
print(f"Je hebt {player_health} health punten,")
print(f"Je doet de zombie per aanval {player_attack} punten schade toe ")
print(f'Jou defnse is {player_defense} punten')
time.sleep(2)
print("")
print("Je loop een lange gang door en opend de volgende deur")
vijand("Man met zwaart",3,2,0)

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