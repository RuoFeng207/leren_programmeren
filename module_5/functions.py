from data import *
import sys
import time
import random


# Text typer function
def print_slow(str:str) -> str:
    str = str.replace(".", ".\n")
    str = str.replace("?", "?\n")
    for char in str:
        time.sleep(0)
        sys.stdout.write(char)
        sys.stdout.flush()

def choice(choice_1:str, choice_2:str) -> str:
    while question:
        print_slow('Je kan nu twee kanten op.')
        print_slow(f'Ga je {choice_1} of {choice_2}?')
        answer = input().lower()
        if (answer not in (choice_1, choice_2)):
            print_slow('Deze optie is niet mogelijk.')
        else:
            break
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
        player["rupee_amount"]+=1
    elif (chamber == 8):
        if (fate == 7):
            player["health"] +=4
        elif (fate <7 ):
            player["health"] -=1
        else:
            player["rupee_amount"]*=2
    elif (chamber == 9):
        if (fate%2 == 0 ):
            player["defence"] +=1
        else:
            player["health"] +=2
    return fate, d1, d2

def chamber_1():
    print_slow('Door de twee grote deuren loop je een gang binnen.')
    print_slow('Het ruikt hier muf en vochtig.')
    print_slow('Je ziet een deur voor je.')

def chamber_7():
    fate= buffs(7)
    if ( fate == 7):
        print_slow('Vreemd de kamer is leeg.')
    else:
        print_slow('Je ziet een rupee op de grond liggen.')
        print_slow(f'Je hebt nu {player["rupee_amount"]} rupee in je inventaris.')
    answer = choice("rechtdoor", "links")
    print(answer)
    return answer

def chamber_8():
    fate, d1, d2 = buffs(8)
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


def chamber_9():
    fate = buffs(9)
    print_slow('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt.')
    if (fate%2 == 0 ):
        print_slow('Je defense voelt ineens beter.')
        print_slow(f'Je defence is nu {player["defence"]}.')
    else:
        print_slow('Je voelt je ineens beter en machtiger.')
        print_slow(f'Je health is nu {player["health"]}.')