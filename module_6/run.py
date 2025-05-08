import functions
f = functions

# welkom
f.tekst("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n")

while True:
    while True:
        bolletjes = f.int_afvang("Hoeveel bolletjes wilt u?")
        if bolletjes >0 and bolletjes <4:
            bakje = f.str_afvang(f"Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje?","hoorntje","bakje")
            break
        elif bolletjes > 3 and bolletjes <9:
            f.tekst(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes.\n")
            break
        else:
            f.tekst("Sorry, zulke grote bakken hebben we niet.\n")
    nogeens = f.str_afvang("Wilt u nog meer bestellen?","ja","nee")
    if nogeens == "nee":
        f.tekst("Bedankt en tot ziens.\n")
        break