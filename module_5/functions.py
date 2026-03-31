from data import *
import sys
import time
import random

# Text typer function
def print_slow(str:str) -> str:
    str = str.replace('.', '.\n')
    str = str.replace('?', '?\n')
    for char in str:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()

def choice(choice_1:str, choice_2:str, Q_type:str, action:str = None) -> str:
    while running:
        if Q_type == 'direction':
            print_slow('Je kan nu twee kanten op, welke kant kies je?')
        elif Q_type == 'y/n':
            print_slow(f'Wil je hier {action}?')
        print_slow(f'{choice_1} of {choice_2}?')
        answer = input().lower()
        if answer not in (choice_1, choice_2):
            print_slow('Deze optie is niet mogelijk.')
        else:
            return answer
        
def buffs(chamber:int) -> int:
    if chamber != 8:
        fate = random.randint(1,10)
        d1 = d2 = None
    else:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        fate = d1 + d2
    
    if fate != 7 and chamber == 7:
        player['rupee_amount']+=1
    elif chamber == 8:
        if fate == 7:
            player['health'] +=4
        elif fate <7:
            player['health'] -=1
        else:
            player['rupee_amount']*=2
    elif chamber == 9:
        if (fate%2 == 0 ):
            player['defence'] +=1
        else:
            player['health'] +=2
    if chamber != 8:
        return fate
    else:
        return fate, d1, d2
def sum(text):
    a = random.randint(10, 25)
    b = random.randint(-5, 75)
    gekozen_operator = random.choice(list(ops.keys()))
    correct_answer = ops[gekozen_operator](a, b)
    print (correct_answer)
    while running:
        try:
            print_slow(f'{text} {a} {gekozen_operator} {b} = ?'
                  'Wat voer je in?')
            answer = int(input())
        except ValueError:
            print_slow('Je kan enkel een heel cijfer in voeren.')
        if answer == correct_answer:
            return True
        else:
            return False
            

def markt():
    display = list(items.keys())
    while running:
        if player['rupee_amount']>0:
            print_slow('Wat wil je kopen?')
            print_slow(f'Je kan kiezen uit {display}.')
            answer = input().lower()
            if answer not in display:
                print_slow('Dit verkoop ik helemaal niet, kan je kijken?')
            else:
                if answer == 'zwaard':
                    player['attack'] +=2
                    print_slow(f'Je attack is nu {player['attack']}')
                elif answer == 'schild':
                    player['defence'] +=1
                    print_slow(f'Je defence is nu {player['defence']}')
                else:
                    items['sleutel'] == True
                    print_slow('die ga je zeker nodig hebben ;) ')
                player['rupee_amount'] -=1
                print_slow(f' en je hebt nog {player['rupee_amount']} rupees over.')
                answer = choice('ja','nee','y/n','nog iets kopen')
                if answer == 'nee':
                    break
        else:
            print_slow('Je hebt niet genoeg rupees om iets te kopen.')
            break

def fight(npc: str) -> str:
    while player["health"] > 0 and enemy[npc]["health"] > 0:
        player_hit_damage = player["attack"] - enemy[npc]["defense"]
        if player_hit_damage > 0:
            enemy[npc]["health"] = max(enemy[npc]["health"] - player_hit_damage, 0)
            print_slow(f'Je hebt tegen de {npc} {player_hit_damage} schade gedaan.'
                  f'De {npc} heeft nu nog {enemy[npc]["health"]} health.')
        else:
            print_slow(f'Je aanval doet geen schade aan de {npc}, yikes.')
        if enemy[npc]["health"] <= 0:
            print_slow(f'Je hebt de {npc} verslagen!!!!!')
            break

        enemy_hit_damage = enemy[npc]["attack"] - player["defense"]
        if enemy_hit_damage > 0:
            player["health"] = max(player["health"] - enemy_hit_damage, 0)
            print(f'De {npc} raakte je! Je hebt {enemy_hit_damage} schade gekregen. '
                  f'Je health is nu {player["health"]}.')
        else:
            print(f'De {npc} doet geen schade aan je, yippie.')
        if player["health"] <= 0:
            print(f'Helaas is de {npc} te sterk voor je. Game over.')
            break

def chamber_1():
    print_slow('Door de twee grote deuren loop je een gang binnen.'
                'Het ruikt hier muf en vochtig.'
                'Je ziet een deur voor je.')
    chamber_7()
def chamber_2():
    print_slow('Je stapt door de deur heen en je ziet een standbeeld voor je.'
        'Het standbeeld heeft een rupee vast.'
        'Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    correct_sum=sum('Daarboven zie je een som staan:')
    if correct_sum == True:
        print_slow('Het standbeeld laat de rupee vallen en je pakt het op.')
        player['rupee_amount']+=1
        print_slow(f'Je hebt nu {player['rupee_amount']} rupee in je inventaris.')
    else:
        print_slow('Er gebeurt niets.')
    answer =choice('ja', 'nee','y/n','de shortcut nemen?')
    if answer == 'ja':
        chamber_8()
    else:
        chamber_6()
def chamber_3():
    print_slow('Je loopt de kamer binnen en ziet een goblin.'
                'De goblin verkoopt verschillende items.'
                f'ik zie dat je {player["rupee_amount"]} rupees hebt'
                'De goblin zegt dat elk item 1 rupee kost.')
    
    answer =choice('ja','nee','y/n','iets kopen')
    if answer == "ja":
        markt()
    else:
        print_slow('Je besluit niks te kopen.')
        chamber_4()

def chamber_4():
    print_slow('Maar toen hoorde je een luid gebrul.'
                'Het is een brute en hij ziet er niet vriendelijk uit.')
    fight("brute")
    if player['health']>0:
        chamber_5()

def chamber_5():
    print_slow('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.'
               'Tot je verbazing zie je een schatkist in het midden van de kamer staan.'
               'Je loopt er naartoe.')
    if items["sleutel"] == True:
        print_slow('Je hebt een sleutel, opent de kist en er zit goud in. '
                   'Je wint het spel!')
    else:
        print_slow('Helaas heb je geen sleutel om de kist te openen en je verliest.'
                   'Game over')
def chamber_6():
    print_slow('Voorzichtig open je de deur.'
               'Ineens zie je een zombie die recht op je af komt.')
    fight('zombie')
    if player['health']>0:
        print('Je ziet dat je twee kanten op kan gaan: links (kamer 3) of rechts (kamer 8)')
        answer = choice('links','rechts','direction')
        if answer == 'links':
            chamber_3()
        else:
            chamber_8()
def chamber_7():
    fate= buffs(7)
    if fate == 7:
        print_slow('Vreemd de kamer is leeg.')
    else:
        print_slow('Je ziet een rupee op de grond liggen.'
                    f'Je hebt nu {player['rupee_amount']} rupee in je inventaris.')
        
    answer = choice('rechtdoor', 'rechts','direction')
    if answer == 'rechts':
        chamber_8()
    else:
        chamber_2()

def chamber_8():
    fate, d1, d2 = buffs(8)
    print('Je gaat naar rechts en komt in een gok ruimte terecht.')
    print('Je ziet ineens een machine staan waar je twee dobbelstenen gooit.')
    answer = choice('ja', 'nee','y/n','gokken')
    if answer == 'ja':
        print_slow(f'Je gooit een {d1} en een {d2} en dat komt op een {fate}.')
        if fate == 7:
            print_slow('Gefeliciteerd, omdat je precies een 7 hebt gerolt krijd je +4 levenspunte'
                       f'Je hebt nu {player["health"]} levenspunten.')
        elif fate > 7:
            print_slow('Lekker gedaan, omdat je hoger dan een 7 hebt gerolt verdubblen je rupees'
                       f'Je hebt nu {player["rupee_amount"]} rupees.')
        else:
            print_slow('Yikes, omdat je onder een 7 hebt gerolt verlies je een levenspunt.'
                       f'Je hebt nu {player["health"]} levenspunten.')
    else:
        print_slow('Je besluit niet te gokken.')
    answer = choice('links','rechts','direction')
    if answer == 'rechts':
        chamber_3()
    else:
        chamber_9()

def chamber_9():
    fate = buffs(9)
    print_slow('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt.')
    if fate %2 == 0:
        print_slow('Je defense voelt ineens beter.'
                   f'Je defence is nu {player["defence"]}.')
    else:
        print_slow('Je voelt je ineens beter en machtiger.'
                   f'Je health is nu {player["health"]}.')