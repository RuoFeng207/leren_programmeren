from data import *
import sys
import time
import random

# Text typer function
def print_slow(str:str) -> str:
    str = str.replace('.', '.\n')
    str = str.replace('?', '?\n')
    for char in str:
        time.sleep(0)
        sys.stdout.write(char)
        sys.stdout.flush()

def choice(choice_1:str, choice_2:str, Q_type:str, action:str = None) -> str:
    while running:
        if (Q_type == 'direction'):
            print_slow('Je kan nu twee kanten op, welke kant kies je?')
        elif (Q_type == 'y/n'):
            print_slow(f'Wil je hier {action}?')
        print_slow(f'{choice_1} of {choice_2}?')
        answer = input().lower()
        if (answer not in (choice_1, choice_2)):
            print_slow('Deze optie is niet mogelijk.')
        else:
            return answer
        
def buffs(chamber:int) -> int:
    if (chamber != 8):
        fate = random.randint(1,10)
        d1 = d2 = None
    else:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        fate = d1 + d2
    
    if (fate != 7 and chamber == 7):
        player['rupee_amount']+=1
    elif (chamber == 8):
        if (fate == 7):
            player['health'] +=4
        elif (fate <7 ):
            player['health'] -=1
        else:
            player['rupee_amount']*=2
    elif (chamber == 9):
        if (fate%2 == 0 ):
            player['defence'] +=1
        else:
            player['health'] +=2
    if chamber != 8:
        return fate
    else:
        return fate, d1, d2

def markt():
    display = list(items.keys())
    while running:
        if (player['rupee_amount']>0):
            print_slow('Wat wil je kopen?')
            print_slow(f'Je kan kiezen uit {display}.')
            answer = input().lower()
            if (answer not in display):
                print_slow('Dit verkoop ik helemaal niet, kan je kijken?')
            else:
                if (answer == 'zwaard'):
                    player['attack'] +=2
                    print_slow(f'Je attack is nu {player['attack']}')
                elif (answer == 'schild'):
                    player['defence'] +=1
                    print_slow(f'Je defence is nu {player['defence']}')
                else:
                    items['sleutel'] == True
                    print_slow('die ga je zeker nodig hebben ;) ')
                player['rupee_amount'] -=1
                print_slow(f' en je hebt nog {player['rupee_amount']} rupees over.')
                answer = choice('ja','nee','y/n','nog iets kopen')
                if (answer == 'nee'):
                    break
        else:
            print_slow('Je hebt niet genoeg rupees om iets te kopen.')
            break
def fight():
     while (player['health'] > 0 and monster['health'] > 0):
         pass
def chamber_1():
    print_slow('Door de twee grote deuren loop je een gang binnen.')
    print_slow('Het ruikt hier muf en vochtig.')
    print_slow('Je ziet een deur voor je.')
    chamber_7()

def chamber_3():
    print_slow('Je loopt de kamer binnen en ziet een goblin.')
    print_slow('De goblin verkoopt verschillende items.')
    print_slow(f'ik zie dat je {player["rupee_amount"]} rupees hebt')
    print_slow('De goblin zegt dat elk item 1 rupee kost.')
    answer =choice('ja','nee','y/n','iets kopen')
    if (answer == "ja"):
        markt()
    else:
        print_slow('Je besluit niks te kopen.')

def chamber_4():
    print_slow('Maar toen hoorde je een luid gebrul.')
    print_slow('Het is een brute en hij ziet er niet vriendelijk uit.')
    print("Hier komt de vecht functie")


def chamber_7():
    fate= buffs(7)
    if ( fate == 7):
        print_slow('Vreemd de kamer is leeg.')
    else:
        print_slow('Je ziet een rupee op de grond liggen.')
        print_slow(f'Je hebt nu {player['rupee_amount']} rupee in je inventaris.')
    answer = choice('rechtdoor', 'rechts','direction')
    if (answer == 'rechts'):
        chamber_8()
    else:
        print('Hier komt kamer 2')

def chamber_8():
    fate, d1, d2 = buffs(8)
    print('Je gaat naar rechts en komt in een gok ruimte terecht.')
    print('Je ziet ineens een machine staan waar je twee dobbelstenen gooit.')
    answer = choice('ja', 'nee','y/n','gokken')
    if (answer == 'ja'):
        print(f'Je gooit een {d1} en een {d2} en dat komt op een {fate}.')
        if fate == 7:
            print_slow('Gefeliciteerd, omdat je precies een 7 hebt gerolt krijd je +4 levenspunte')
            print_slow(f'Je hebt nu {player["health"]} levenspunten.')
        elif fate > 7:
            print_slow('Lekker gedaan, omdat je hoger dan een 7 hebt gerolt verdubblen je rupees')
            print_slow(f'Je hebt nu {player["rupee_amount"]} rupees.')
        else:
            print_slow('Yikes, omdat je onder een 7 hebt gerolt verlies je een levenspunt.')
            print_slow(f'Je hebt nu {player["health"]} levenspunten.')
    else:
        print_slow('Je besluit niet te gokken.')
    answer = choice('links','rechts','direction')
    if (answer == 'rechts'):
        chamber_3()
    else:
        chamber_9()

def chamber_9():
    fate = buffs(9)
    print_slow('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt.')
    if (fate %2 == 0 ):
        print_slow('Je defense voelt ineens beter.')
        print_slow(f'Je defence is nu {player["defence"]}.')
    else:
        print_slow('Je voelt je ineens beter en machtiger.')
        print_slow(f'Je health is nu {player["health"]}.')