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
#def vijand
def vijand(gevecht):
   return gevecht
#kamer_3


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(4)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {getal1}{operator}{getal2}= ')

andwoord =int(input("wat is jouw andwoord? "))
if code != andwoord:
  print("dit andwoord is niet corect.")
  
  time.sleep(2)
else:
  print("")
  print("Gelukt je hebt de code gekraakt!")
  print('Het stadbeeld laat de sleutel vallen en je pakt het op')
print("")
print("Dan zie je 2 deuren op een daar van staat kamer 3 en op de andere staat kamer 6")
print("Welke kamer neem jij?")

while True:
  kamer=input("Je neemt kamer: ")
  if kamer =="3":
    break
  elif kamer =="6":
    break
  else:
    print("Deze optie is ongeldig probeer opnieuw")
  print("")

if kamer=="3":
    # === [kamer 3] === #
    #random voorwerp
    items = ['schild',"zwaart"]
    item = random.choice(items)
    if item =="schild":
        player_defense += 1
    if item=="zwaart":
        player_attack +=2
    print("")
        
    print('Je ziet een nieuwe deur en duwt hem open, je stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}.')
    print(f'Je pakt het {item} op en houd het bij je.')
    
    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
    print("")
      
      
    print('Je loopt tegen een man met zwaard aan.')
    print(f"Je hebt {player_health} health punten,")
    print(f"Je doet de zombie per aanval {player_attack} punten schade toe ")
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
else:
    zombie_attack_amount = math.ceil(player_health / vijand_hit_damage)
    
    player_hit_damage = (player_attack - vijand(gevecht=0))
    player_attack_amount = math.ceil(vijand(gevecht=2) / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
items = ['schild',"zwaart"]
item = random.choice(items)
if item =="schild":
  player_defense += 1
if item=="zwaart":
  player_attack +=2

print('Je ziet een nieuwe deur en duwt hem open, je stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(6)

print("")
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een man met zwaard aan.')
print(f"De man met zwaard heeft {vijand(gevecht=2)} health punten,")
print(f"Hij doet jou per aanval {vijand(gevecht=1)} punten schade toe ")
print(f'Zijn defense is {vijand(gevecht=0)} punten')
time.sleep(4)

vijand_hit_damage = (vijand(gevecht=0) - player_defense)
if vijand_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de man met zwaard, hij kan je geen schade doen.')
else:
    vijand_attack_amount = math.ceil(player_health / vijand_hit_damage)
    
    player_hit_damage = (player_attack - vijand(gevecht=0))
    player_attack_amount = math.ceil(vijand(gevecht=2) / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de man met zwaard.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de man met zwaard te sterk voor je.')
        print('Game over.')
        exit()
print("")
time.sleep(3)
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
print("Je probeert hem te open en maar...")
time.sleep(2)
print("")
print("Hij zit op slot! ")
if code== andwoord:
   print("Opeens herinner je je de sluitel die je hebt meegenomen uit kamer 2 ")
   print("Je probeert hem uit en... HIJ PAST!")
   print("Je neemt de buit mee")
   print("Gefeliciteerd je hebt gewonnen")
else:
   print("Je voelt in je zaken naar iets waar mee je de kist kan openen een slutel of zo maar niks.")
   print("Helaas je hebt veloren.")
   print("Game over")