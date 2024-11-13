# #In een klein dorp aan de voet van een grote berg stond een mysterieuze grot. De grot was omgeven door hoge bomen en had een ingang die glinsterde in het zonlicht. Op een dag besloot een dappere jongen het avontuur aan te gaan en de grot te verkennen. Binnenin ontdekte hij prachtige, witte kristallen die de wanden sierden. Verbluft door de schoonheid, wist hij dat hij een geheim had ontdekt dat het dorp voor altijd zou veranderen.

# Vraag de gebruiker om een verhaal in te voeren
verhaal = input("Voer hier je verhaal in: ")

# Split het verhaal meerdere strings
split_verhaal = verhaal.split()

# Woorden die vervangen moeten worden
woorden = {"klein":"groot","witte":"zwartte","dorp":"stad","grot": "flat","grote":"groot","berg":"dal"}
# Vervang de woorden in het verhaal
vervangen_verhaal = [woorden.get(woord,woord) for woord in split_verhaal]

# Maak het verhaal weer een string
nieuw_verhaal = ' '.join(vervangen_verhaal)

# Print het nieuwe verhaal
print("")
print("Het nieuwe verhaal is:", nieuw_verhaal)