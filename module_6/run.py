import functions as f
import data as d

f.tekst("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.")
klant = f.str_afvang("Bent u een particuliere klant of een zakelijke klant?",0)
#print(klant)
if klant == d.ijs_winkel[0][1]['afkorting']:
    f.int_afvang("Hoeveel bolletjes wilt u?")