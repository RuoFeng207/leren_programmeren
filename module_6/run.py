import functions,data
f = functions
d = data
# welkom
f.tekst("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while True:
    # vraag bol
    bollen = f.int_afvang("Hoe veel bolletjes wilt u?")
    # vraag houder
    if bollen >0 and bollen <4:
        pass
    elif bollen >3 and bollen < 9:
        f.tekst(f"Dan krijgt u van mij een bakje met {bollen} bolletjes")
        break
    else:
        f.tekst("Zulke groten bollen verkopen we niet")
for bol in range(1,bollen+1):
    print("")
    key = f.str_afvang(f"Welke smaak wilt u voor bol nr {bol}?",d.keus["smaak"])
    d.smaken[key]["aantal"] +=1 