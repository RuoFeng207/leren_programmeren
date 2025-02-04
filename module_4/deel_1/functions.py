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

def prime_teller(getal):
    lijst =[]
    for i in range(1,getal+1):
        if is_prime(i):
            lijst.append(i)
    print(lijst)
    return getal
prime_teller(100)