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
rupee = 0
# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(4)

# === [kamer 7] === #
print("Je doet hem open en ziet iets schitteren een rupee!")
rupee +=1
print("Je loopt er heen en pakt hem op")
print(f"je hebt nu {rupee} rupee(s) in je inventory")
print("")

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
# === [kamer 3] === #
if kamer=="3":
  items = ['schild',"zwaart"]
  
