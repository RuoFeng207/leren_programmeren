import functions as f
import data as d

f.tekst("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.")
klant = f.str_afvang("Bent u een particuliere klant of een zakelijke klant?",0)


while True:
    if klant == d.ijs_winkel[0][0]['afkorting']:
        d.ijs_winkel[0][0]['particuliere klant'] = True
    elif klant == d.ijs_winkel[0][1]['afkorting']:
        d.ijs_winkel[0][1]['zakelijke klant'] = True
    if klant == d.ijs_winkel[0][0]['afkorting']:
        while True:
            bollen = f.int_afvang("Hoeveel bolletjes wilt u?")
        
            if bollen >0  and bollen < 4:
                houder = f.str_afvang("Wilt u een hoorntje of een bakje?",2)
                if houder == "H":
                    d.ijs_winkel[2][0]['aantal']+=1 # hoorntje +1 
                else:
                    d.ijs_winkel[2][1]['aantal']+=1 # bakje +1
                break
            elif 3 < bollen < 9:
                f.tekst(f"Dan krijgt u van mij een bakje met {bollen} bolletjes")
                d.ijs_winkel[2][1]['aantal']+=1 # bakje +1
                break
            elif bollen >= 9:
                f.tekst("Zulke grote bollen verkopen we niet.")
    elif klant == d.ijs_winkel[0][1]['afkorting']:
        bollen = f.int_afvang("Hoeveel liter wilt u?")
        
    for bol in range(1, bollen + 1):
        if klant == d.ijs_winkel[0][0]['afkorting']:
            keus_smaak = f.str_afvang(f"Welke smaak wilt u voor bol nr {bol}?",1)
        elif klant == d.ijs_winkel[0][1]['afkorting']:
            keus_smaak = f.str_afvang(f"Welke smaak wilt u voor liter nr {bol}?",1)
        if keus_smaak == "A":
            d.ijs_winkel[1][0]["aantal"]+=1 # aarbei
        elif keus_smaak == "C":
            d.ijs_winkel[1][1]["aantal"]+=1 # chocolade
        elif keus_smaak == "M":
            d.ijs_winkel[1][2]["aantal"]+=1 # mint
        elif keus_smaak == "V":
            d.ijs_winkel[1][3]["aantal"]+=1 # vanile

    if klant == d.ijs_winkel[0][0]['afkorting']:
        toppings = f.str_afvang("Wat voor toppings wilt u daarbij?",3)
        if toppings == "B":
            d.ijs_winkel[3][1]["aantal"]+=1 # slagroom
        elif toppings == "C":
            d.ijs_winkel[3][2]["aantal"]+=1 # sprinkels
        elif toppings == "D":
            d.ijs_winkel[3][3]["aantal"]+=1 # caramel saus

    if klant == d.ijs_winkel[0][0]['afkorting']:
        f.tekst("Wilt u nog eens? [druk dan op Enter]")
        nog_eens = input()
        if nog_eens != "":
            f.bon()
            break
    else:
        f.bon()
        break