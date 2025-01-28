from termcolor import colored, COLORS
from functies import gegvens

a=gegvens()
print("")
for persoon in a:
    naam = persoon["naam"]
    woon = persoon["woon"]
    leeftijd = persoon["leeftijd"]
    volwasse = leeftijd-18
    if volwasse<=0:
         print(f"in {colored(woon,"yellow",attrs=["bold"])} woont {colored(naam,"green",attrs=["bold"])}, {colored("die nog niet ", "red",attrs=["bold"])}volwasse is.")
    else:
        print(f"in {colored(woon,"yellow",attrs=["bold"])} woont {colored(naam,"green",attrs=["bold"])}, {colored(f"die al {volwasse} ", "red",attrs=["bold"])}jaar volwasse is.")
