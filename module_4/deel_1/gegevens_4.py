from functies import gegvens

a=gegvens()
print("")
for persoon in a:
    print(f"{persoon["naam"]} die in {persoon["woon"]} woont is {persoon["leeftijd"]} jaar")