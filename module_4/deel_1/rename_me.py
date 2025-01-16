def rest(getal_1:int) -> bool:
    return getal_1 % 2 == 0
print(rest (8) )

def reversed(tekst:str) -> str:
    gesplitst = tekst.split()
    woord_draai = gesplitst[::-1]
    achterstevoren = ' '.join(woord_draai)
    return achterstevoren
print(reversed ("hallo daar"))

def tel_letter(woord:str) -> int:
    split_woord = set(woord)
    cijfers_in_woord = len(split_woord)
    return cijfers_in_woord
print(tel_letter("drop"))

def tel_letter_2(tekst:str) -> float:
    split_tekst =tekst.split()
    
    teller = 0 
    for x in split_tekst:
        teller += len(x)

    bizarro_matrix = teller / len(split_tekst)
    return bizarro_matrix
print(tel_letter_2("taart"))

def tafels(tafel:int, parallelle_tosti:int=10) -> None:
    for y in range(1, parallelle_tosti+1):
        antwoord= y * tafel
        print(f'{y} x {tafel} = {antwoord}')
print(tafels(4, 10))


#         def quantum_broodrooster(stellar_broccoli:int) -> bool:
#     return stellar_broccoli % 2 == 0
# print(quantum_broodrooster)
# def chaos_papegaai(fantasie_platypus:str) -> str:                 Deze namen zijn geweldig
#     betoverde_druif = fantasie_platypus.split()
#     doldwaze_broccoli = betoverde_druif[::-1]
#     tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
#     return tijdmachine_pannenkoekenmix

# def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
#     planetair_taartje = set(galactische_snoepjes)
#     whatchamacallit = len(planetair_taartje)
#     return whatchamacallit

# def ruimte_hamsterwiel(planetair_taartje:str) -> float:
#     wobbelwobbel = planetair_taartje.split()
    
#     blork = 0
#     for snorkelwagen in wobbelwobbel:
#         blork += len(snorkelwagen)

#     bizarro_matrix = blork / len(wobbelwobbel)
#     return bizarro_matrix

# def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
#     for zwabber_krakeling in range(1, parallelle_tosti+1):
#         laser_sandwich = zwabber_krakeling * infinity_pizza
#         print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')