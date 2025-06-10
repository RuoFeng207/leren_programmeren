import functions
import data
f = functions
d = data

f.tekst("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.")

klant =f.str_afvang("Bent u een particuliere klant of een zakelijke klant?",d.keus["klant"])
if klant == "zakelijke klant":
    liters= f.int_afvang("Hoeveel L wilt u?")
    for liter in range(1, liters + 1):
        print("")
        keus_smaak = f.str_afvang(f"Welke smaak wilt voor L nr {liter}?", d.keus['smaak'])
        d.smaken[keus_smaak]['aantal'] += 1
        d.totaal.append(d.smaken[keus_smaak]['prijs']['bedrijf'])
    f.toon_bon()
elif klant == "particuliere klant":
    while True:
        while True:
            bollen = f.int_afvang("Hoeveel bolletjes wilt u?")
            if 0 < bollen < 4:
                keus_houder = f.str_afvang("Wilt u een hoorntje of een bakje?", d.keus["houder"])
                d.houders[keus_houder]['aantal'] += 1
                break
            elif 3 < bollen < 9:
                f.tekst(f"Dan krijgt u van mij een bakje met {bollen} bolletjes")
                d.houders['bakje']['aantal'] += 1
                keus_houder = 'bakje'  
                break
            elif bollen >= 9:
                f.tekst("Zulke grote bollen verkopen we niet.")
            else:
                f.tekst("Sorry, dat snap ik niet.")

        for bol in range(1, bollen + 1):
            print("")
            keus_smaak = f.str_afvang(f"Welke smaak wilt u voor bol nr {bol}?", d.keus['smaak'])
            d.smaken[keus_smaak]['aantal'] += 1
            d.totaal.append(d.smaken[keus_smaak]['prijs']['klant'])

        keus_toppings = f.str_afvang("Wat voor toppings wilt u daarbij?", d.keus["toppings"])
        if keus_toppings == "slagroom":
            d.toppings[keus_toppings]['aantal'] += 1
        elif keus_toppings == "sprinkels":
            d.toppings[keus_toppings]['aantal'] += bollen
        elif keus_toppings == "caramel saus":
            
            d.toppings[keus_toppings]['aantal'][keus_houder] += 1

        keus = f.tekst("Wilt u nog iets bestellen? [druk op enter om nog iets te bestellen]")
        keus = input()
        if keus == "":
            f.tekst("Oke")
            print("")
        else:
            f.toon_bon()
            f.reset_bestelling()
            break
