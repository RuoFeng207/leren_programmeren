import time
import random

player_attack = 1
player_defense = 0
player_health = 3
player_rupee_amount = 0
speciaal_item = 0  

def PlayerAttackEnemy(player_health, enemy_attack, enemy_defense, enemy_health):
    while player_health > 0 and enemy_health > 0:
        player_hit_damage = player_attack - enemy_defense
        if player_hit_damage > 0:
            enemy_health -= player_hit_damage
            print(f'Je hebt tegen de vijand {player_hit_damage} schade gedaan. De vijand heeft nu nog {enemy_health} health.')
        else:
            print('Je aanval doet geen schade aan de vijand, yikes.')
        
        if enemy_health <= 0:
            print('Je hebt de vijand verslagen!!!!!')
            return player_health

        enemy_hit_damage = enemy_attack - player_defense
        if enemy_hit_damage > 0:
            player_health -= enemy_hit_damage
            print(f'De vijand raakte je! Je hebt {enemy_hit_damage} schade gekregen. Je health is nu {player_health}.')
        else:
            print('De vijand doet geen schade aan je, yippie.')
        
        if player_health <= 0:
            print('Helaas is de vijand te sterk voor je.')
            print('Game over.')
            exit()

    return player_health

time.sleep(3)

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
time.sleep(3)

# === [kamer 7] === #
cijfers = [1,2,3,4,5,6,7,8,9,10]
rupee = random.choice(cijfers)
if cijfers == 7:
    print('je ziet rechts van je een deur')
    player_rupee_amount = player_rupee_amount + 0
else:
    print('Je ziet een rupee op de grond liggen.')
    player_rupee_amount = player_rupee_amount + 1
    print(f'Je hebt nu {player_rupee_amount} rupee in je inventaris.')
    print('je ziet rechts van je een deur')
    
time.sleep(3)

# === [kamer 8] === #
dobbel_1 = random.randint(1,6)
dobbel_2 = random.randint(1,6)
totaal = dobbel_1 + dobbel_2

deur = input('ga je rechtdoor of naar rechts?? ').lower()
if deur == 'rechts':
    print('je gaat naar rechts en komt in een gok ruimte terecht')
    print('je ziet ineens een machine staan waar je twee dobbelstenen gooit')
    gokken = input('wil je een gokje wagen? ja/nee ').lower()
    if gokken == 'ja':
        print('laten we dan beginnen >:) ')
        print('je gooit de twee dobbelstenen')
        print(f'je gooit een {dobbel_1} en een {dobbel_2} en dat komt op een {totaal} ')
        if totaal == 7:
            print('gefeliciteerd, omdat je precies een 7 hebt gerolt krijd je +4 levenspunte')
            player_health = player_health + 4
            print(f'je hebt nu {player_health} levenspunten')
        elif totaal > 7:
            print('lekker gedaan, omdat je hoger dan een 7 hebt gerolt verdubblen je rupees')
            player_rupee_amount = player_rupee_amount * 2
            print(f'je hebt nu {player_rupee_amount} rupees')
        elif totaal < 7:
            print('yikes, omdat je onder een 7 hebt gerolt verlies je een levenspunt')
            player_health = player_health - 1
            print(f'je hebt nu {player_health} levenspunten')
            if player_health < 1:
                print('Game over')
                quit()
    
    time.sleep(3)
    print('je ziet dat je twee kanten op kan gaan links/rechts')
    richting_2 = input('kies je ervoor om naar links of om naar rechts te gaan? ')
    if richting_2 == 'links':
        print('je loopt door de linker deur')
    
    # === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
    
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'ik zie dat je {player_rupee_amount} rupees hebt')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item = speciaal_item + 1
                player_rupee_amount = player_rupee_amount - 1
                print('die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)

    # === [kamer 4] ===#
    print('Dapper met je nieuwe gekochte spullen loop je de kamer binnen.')
    print('Maar toen hoorde je een luid gebrul.')
    print('Het is een brute en hij ziet er niet vriendelijk uit.')

    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

    # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        quit()
        time.sleep(3)

    # === [kamer 9] === #
    print('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt')
    stat_buff = random.randint(1,2)
    if stat_buff == 1:
        print('je defense voelt ineens beter')
        player_defense = player_defense + 1
        print(f'je defense is nu {player_defense}')
    elif stat_buff == 2:
        print('je voelt je ineens beter en machtiger ')
        player_health = player_health + 2
        print(f'je health is nu {player_health}')
        time.sleep(3)


# === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
    
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'ik zie dat je {player_rupee_amount} rupees hebt')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item = speciaal_item + 1
                player_rupee_amount = player_rupee_amount - 1
                print('die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)


    # === [kamer 4] ===#
    print('Dapper met je nieuwe gekochte spullen loop je de kamer binnen.')
    print('Maar toen hoorde je een luid gebrul.')
    print('Het is een brute en hij ziet er niet vriendelijk uit.')

    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

    # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        quit()
        time.sleep(3)

# === [kamer 2] === #
a = random.randint(10, 25)
b = random.randint(-5, 75)
gekozen_operator = random.choice(['+', '-', '*'])
if gekozen_operator == '+':
    som = a + b
elif gekozen_operator == '-':
    som = a - b
elif gekozen_operator == '*':
    som = a * b

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een rupee vast.')
print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
print(f'Daarboven zie je een som staan: {a} {gekozen_operator} {b} = ??')
antwoord = int(input('Wat toets je in? '))
time.sleep(3)

if antwoord == som:
    print('Het standbeeld laat de rupee vallen en je pakt het op.')
    player_rupee_amount = player_rupee_amount + 1 
else:
    print('Er gebeurt niets....')
    time.sleep(3)

print('Ineens zie je een shortcut in de muur.')
Ja_Nee = input('Wil je het riskeren om de shortcut te nemen of niet? ja/nee? ').lower()
if Ja_Nee == 'ja':
    time.sleep(3)


    # === [kamer 8] === #
    print('je opent de deur en komt in een gok ruimte terecht')
    print('je ziet ineens een machine staan waar je twee dobbelstenen gooit')
    gokken = input('wil je een gokje wagen? ja/nee ').lower()
    if gokken == 'ja':
        print('laten we dan beginnen >:) ')
        print('je gooit de twee dobbelstenen')
        print(f'je gooit een {dobbel_1} en een {dobbel_2} en dat komt op een {totaal} ')
        if totaal == 7:
            print('gefeliciteerd, omdat je precies een 7 hebt gerolt krijd je +4 levenspunte')
            player_health = player_health + 4
            print(f'je hebt nu {player_health} levenspunten')
        elif totaal > 7:
            print('lekker gedaan, omdat je hoger dan een 7 hebt gerolt verdubblen je rupees')
            player_rupee_amount = player_rupee_amount * 2
            print(f'je hebt nu {player_rupee_amount} rupees')
        elif totaal < 7:
            print('yikes, omdat je onder een 7 hebt gerolt verlies je een levenspunt')
            player_health = player_health - 1
            print(f'je hebt nu {player_health} levenspunten')
            if player_health < 1:
                print('Game over')
                quit()
    time.sleep(3)
    
    time.sleep(3)
    print('je ziet dat je twee kanten op kan gaan links/rechts')
    richting_2 = input('kies je ervoor om naar links of om naar rechts te gaan? ')
    if richting_2 == 'links':
        print('je loopt door de linker deur')
        
        # === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
    
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'ik zie dat je {player_rupee_amount} rupees hebt')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item = speciaal_item + 1
                player_rupee_amount = player_rupee_amount - 1
                print('die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)

    # === [kamer 4] ===#
    print('Dapper met je nieuwe gekochte spullen loop je de kamer binnen.')
    print('Maar toen hoorde je een luid gebrul.')
    print('Het is een brute en hij ziet er niet vriendelijk uit.')
    time.sleep(3)

    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

    # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        quit()
        time.sleep(3)
    
    # === [kamer 9] === #
    print('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt')
    stat_buff = random.randint(1,2)
    if stat_buff == 1:
        print('je defense voelt ineens beter')
        player_defense = player_defense + 1
        print(f'je defense is nu {player_defense}')
    elif stat_buff == 2:
        print('je voelt je ineens beter en machtiger ')
        player_health = player_health + 2
        print(f'je health is nu {player_health}')
        time.sleep(3)

    # === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
    
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'ik zie dat je {player_rupee_amount} rupees hebt')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item = speciaal_item + 1
                player_rupee_amount = player_rupee_amount - 1
                print('die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)

    # === [kamer 4] ===#
    print('Dapper met je nieuwe gekochte spullen loop je de kamer binnen.')
    print('Maar toen hoorde je een luid gebrul.')
    print('Het is een brute en hij ziet er niet vriendelijk uit.')
    time.sleep(3)

    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

    # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        quit()
        time.sleep(3)

elif Ja_Nee == 'nee':
    # === [kamer 6] === #
    print('Voorzichtig open je de deur.')
    print('Ineens zie je een zombie die recht op je af komt.')
    
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    player_health = PlayerAttackEnemy(player_health, zombie_attack, zombie_defense, zombie_health)

    print('Je ziet dat je twee kanten op kan gaan: links (kamer 3) of rechts (kamer 8).')
richting = input('Ga je liever naar rechts of naar links? ').lower()
if richting == 'links':
    # === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
    
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'Ik zie dat je {player_rupee_amount} rupees hebt.')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item += 1
                player_rupee_amount = player_rupee_amount - 1
                print('Die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)

    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

        # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        time.sleep(3)
        

elif richting == 'rechts':
    # === [kamer 8] === #
    print('Je opent de deur en komt in een gok ruimte terecht')
    print('Je ziet ineens een machine staan waar je twee dobbelstenen gooit')
    gokken = input('Wil je een gokje wagen? ja/nee ').lower()
    if gokken == 'ja':
        print('Laten we dan beginnen >:) ')
        dobbel_1 = random.randint(1, 6)
        dobbel_2 = random.randint(1, 6)
        totaal = dobbel_1 + dobbel_2
        print(f'Je gooit een {dobbel_1} en een {dobbel_2}, dat komt op een {totaal} ')
        if totaal == 7:
            print('Gefeliciteerd, omdat je precies een 7 hebt gerold krijg je +4 levenspunten')
            player_health += 4
            print(f'Je hebt nu {player_health} levenspunten')
        elif totaal > 7:
            print('Lekker gedaan, omdat je hoger dan een 7 hebt gerold verdubbel je rupees')
            player_rupee_amount *= 2
            print(f'Je hebt nu {player_rupee_amount} rupees')
        elif totaal < 7:
            print('Yikes, omdat je onder een 7 hebt gerold verlies je een levenspunt')
            player_health -= 1
            print(f'Je hebt nu {player_health} levenspunten')
            if player_health < 1:
                print('Game over')
                quit()
    
    time.sleep(3)
    print('je ziet dat je twee kanten op kan gaan links/rechts')
    richting_2 = input('kies je ervoor om naar links of om naar rechts te gaan? ')
    if richting_2 == 'links':
        print('je loopt door de linker deur')
        # === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
        
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'ik zie dat je {player_rupee_amount} rupees hebt')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item = speciaal_item + 1
                player_rupee_amount = player_rupee_amount - 1
                print('die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)
        
        # === [kamer 4] === #
    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

        # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        time.sleep(3)

        
        # === [kamer 9] === #
    print('Je voelt een soort magisch gevoel zodra je deze kamer binnenloopt')
    stat_buff = random.randint(1,2)
    if stat_buff == 1:
        print('je defense voelt ineens beter')
        player_defense = player_defense + 1
        print(f'je defense is nu {player_defense}')
    elif stat_buff == 2:
        print('je voelt je ineens beter en machtiger ')
        player_health = player_health + 2
        print(f'je health is nu {player_health}')
        time.sleep(3)
        
    # === [kamer 3] === #
    items = ['schild', 'zwaard', 'armor', 'sleutel']
        
    print('Je loopt de kamer binnen en ziet een goblin.')
    print('De goblin verkoopt verschillende items.')
    print(f'ik zie dat je {player_rupee_amount} rupees hebt')
    print('De goblin zegt dat elk item 1 rupee kost.')
    time.sleep(3)

    while True:
        kopen = input('Wil je iets kopen ja/nee? ').lower()
        if kopen == 'ja':
            print(items)
            verkocht = input('Wat wil je kopen? ')
            if verkocht == 'zwaard':
                player_attack += 2
                player_rupee_amount -= 1
                print(f'Je attack is nu {player_attack} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'schild':
                player_defense += 1
                player_rupee_amount -= 1
                print(f'Je defense is nu {player_defense} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'armor':
                player_health += 2
                player_rupee_amount -= 1
                print(f'Je health is nu {player_health} en je hebt nog {player_rupee_amount} rupees over.')
            elif verkocht == 'sleutel':
                speciaal_item = speciaal_item + 1
                player_rupee_amount = player_rupee_amount - 1
                print('die ga je zeker nodig hebben ;) ')
            else:
                print('Dit verkoop ik helemaal niet, kan je kijken?')
        elif kopen == 'nee':
            print('Aw jammer dat je niks wilt kopen.')
            break
        else:
            print('Je kan alleen ja of nee invoeren.')
        time.sleep(3)
        
        # === [kamer 4] === #
    brute_attack = 2
    brute_defense = 0
    brute_health = 3

    player_health = PlayerAttackEnemy(player_health, brute_attack, brute_defense, brute_health)

        # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een brute of zombie tegenkomen.')
    print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if speciaal_item == 1:
        print('Je hebt een sleutel, opent de kist en er zit goud in. Je wint het spel!')
    else:
        print('Helaas heb je geen sleutel om de kist te openen en je verliest.')
        time.sleep(3)

