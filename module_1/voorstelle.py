naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht= input("Ben je een A) een jonge of B) een meisje? ").lower()
kleur = input("Wat is je favoriete kleur? ")
favo_nummer = int(input("Wat is je favoriete getal? "))
verschil = abs(leeftijd-favo_nummer)
geslacht_voor_naam_woord= 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{naam()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", kleur)
print(f"Het verschil tussen {leeftijd} leeftijd en {favo_nummer} is:",geslacht_voor_naam_woord)
