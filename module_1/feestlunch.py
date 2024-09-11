from termcolor import colored, cprint, COLORS


#in euro
croissantjes_prijs = 0.39
stokbroden_prijs = 2.78 
Kortingsbon= 0.50
#aantal
aantal_croissantjes = int(input("Hoeveel croissantjes wilt u: "))
aantal_stokbrood = int(input("Hoeveel stokbrood wilt u: "))
aantal_kortingsbonnen =int(input("Hoeveel kortingsbonnen heeft u: "))

#totaal
totaal = aantal_croissantjes*croissantjes_prijs + aantal_stokbrood*stokbroden_prijs - aantal_kortingsbonnen*Kortingsbon
print(f"De feestlunch kost je bij de bakker {colored(totaal,'yellow', attrs=['bold'])} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!")