#in euro
croissantjes_prijs = 0.39
stokbroden_prijs = 2.78 
Kortingsbon= 0.50
#aantal
aantal_croissantjes = 17
aantal_stokbrood = 2
aantal_kortingsbonnen = 3

#totaal
totaal = aantal_croissantjes*croissantjes_prijs + aantal_stokbrood*stokbroden_prijs - aantal_kortingsbonnen*Kortingsbon
print(f"u moet intotaal {totaal} euro betalen")