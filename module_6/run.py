import functions,data
f = functions
d = data
# welkom
f.tekst("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n")

while True:
    while True:
        d.bol = f.int_afvang("Hoeveel bolletjes wilt u?")
        if d.bol >0 and d.bol <4:
            keus = f.str_afvang(f"Wilt u deze {d.bol} bolletje(s) in een hoorntje of een bakje?","hoorntje","bakje")
            if keus == "hoorntje":
                d.hoorntje +=1
            else:
                d.bakje +=1
            break
        elif d.bol > 3 and d.bol <9:
            f.tekst(f"Dan krijgt u van mij een bakje met {d.bol} bolletjes.\n")
            d.bakje +=1
            break
        else:
            f.tekst("Sorry, zulke grote bakken hebben we niet.\n")
    # Nogeens bestellen?
    nogeens = f.str_afvang("Wilt u nog meer bestellen?","ja","nee")
    if nogeens == "nee":
        f.bon()
        f.tekst("Bedankt en tot ziens.\n")
        break