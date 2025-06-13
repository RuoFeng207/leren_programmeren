import functions as f
import data as d

f.tekst("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.")
klant = f.str_afvang("Bent u een particuliere klant of een zakelijke klant?",0)

if klant == d.ijs_winkel[0][0]['afkorting']:
    d.ijs_winkel[0][0]['particuliere klant'] = True
    while True:
        bollen = f.int_afvang("Hoeveel bolletjes wilt u?")
    
        if bollen >0  and bollen < 4:
            houder = f.str_afvang("Wilt u een hoorntje of een bakje?",2)
            if houder == "H":
                d.ijs_winkel[2][0]['aantal']+=1
            else:
                d.ijs_winkel[2][1]['aantal']+=1
            break
        elif 3 < bollen < 9:
            f.tekst(f"Dan krijgt u van mij een bakje met {bollen} bolletjes")
            d.ijs_winkel[2][1]['aantal']+=1
            break
        elif bollen >= 9:
            f.tekst("Zulke grote bollen verkopen we niet.")
        
    for bol in range(1, bollen + 1):
        keus_smaak = f.str_afvang(f"Welke smaak wilt u voor bol nr {bol}?",1)
    f.str_afvang("Wat voor toppings wilt u daarbij?",3)