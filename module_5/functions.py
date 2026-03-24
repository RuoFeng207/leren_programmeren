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
    fate = random.randint(1,10)
    if (fate != 7 and chamber == 7):
        player["rupee_amount"]+=1
    if (chamber == 9):
        if (fate%2 == 0 ):
            player["defence"] +=1
        else:
            player["health"] +=2
    return fate

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
def chamber_9():
    fate = buffs(9)
    print_slow('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt.')
    if (fate%2 == 0 ):
        print('Je defense voelt ineens beter.')
        print(f'Je defence is nu {player["defence"]}.')
    else:
        print('Je voelt je ineens beter en machtiger.')
        print(f'Je health is nu {player["health"]}.')