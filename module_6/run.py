import functions,data
f = functions
d = data
# welkom
f.tekst("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
while True:
    while True:
        # vraag bol
        bollen = f.int_afvang("Hoe veel bolletjes wilt u?")
        # vraag houder
        if bollen >0 and bollen <4:
            keus_houder =f.str_afvang("Wilt u een hoorntje of een bakje?",d.keus["houder"])
            d.houders[keus_houder]['aantal'] +=1
            d.totaal.append(d.houders[keus_houder]['prijs'])
            break    
        elif bollen >3 and bollen < 9:
            f.tekst(f"Dan krijgt u van mij een bakje met {bollen} bolletjes")
            d.totaal.append(d.houders['bakje']['prijs'])
            break
        elif bollen>8:
            f.tekst("Zulke groten bollen verkopen we niet")
        else:
            f.tekst("Sorry, dat snap ik neit")
    for bol in range(1,bollen+1):
        print("")
        keus_smaak = f.str_afvang(f"Welke smaak wilt u voor bol nr {bol}?",d.keus['smaak'])
        d.smaken[keus_smaak]['aantal'] +=1
        d.totaal.append(d.smaken[keus_smaak]['prijs'])
    toppings= f.str_afvang("Wat voor toppings wilt u er bij?",d.keus['toppings'])
    print(toppings)
    if toppings == "Caramel saus":
        if keus_houder == "H":
            d.totaal.append(d.toppings['caramel_saus']['prijs']['hoorntje'])
        else:
            d.totaal.append(d.toppings['caramel_saus']['prijs']['bakje'])
    else:
        d.totaal.append(d.toppings['prijs'])

    keus =f.str_afvang("Wilt u nog iets bestellen?",d.keus['ja/nee'])
    if keus == "nee":
        f.toon_bon()
        break