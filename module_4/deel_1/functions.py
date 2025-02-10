# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # als het nummer gelijk of kleiner is dan 1 geef false terug geen priemgetal
    if number <= 1:
        return False
    
    # als het nummer gelijk is aan 2 dan is het eeb priemgetal
    if number == 2:
        return True
    
    # als de rest van het 2 gelijk is aan 0 dan is het geen priemgetal
    if number % 2 == 0:
        return False
    
    # als het getal een getal tot de macht 0.5 is en de rest van d is gelijk aan 0 dan geen priemgetal
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # geeft alle variable terug 
    return True

# prime x aantal 
def prime_teller(getal):
    lijst =[]
    for i in range(1,getal+1):
        if is_prime(i):
            lijst.append(i)

    return lijst


#prime aantal gegeven
def prime_loop(cijfer):
    lijst_2 = []
    teller = 1
    prime =0
    while True:
        teller+=1
        if is_prime(teller):
            lijst_2.append(teller)
            prime+=1
            if prime == cijfer:
                break
    return lijst_2
        


def tussen_cijfers(cijfer_1,cijfer_2):
    lijst_3 =[]

    for x in range(cijfer_1,cijfer_2+1):
        if is_prime(x):
            lijst_3.append(x)
    return lijst_3
            

