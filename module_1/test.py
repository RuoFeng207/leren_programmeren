import time, math,random

def test(Naam:str,jaar:int)-> str: #functie, parameter
    print(f"Hallo{Naam} en ben {jaar} jaar oud") #print string parameter
test("jan",12) #argument


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

player_attack = 1
player_defense = 0
player_health = 3


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
    

vijand("Zombie",2,1,0)    
vijand("Man met zwaart",3,2,0)
