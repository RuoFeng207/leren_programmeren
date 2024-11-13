
poging = 5
while True:
    wachtwoord = input("Voer uw wachtwoord in: ")
    if wachtwoord =="humtidumtie217":
        print("Oke kom er maar in")
    elif poging>1 and poging<6:
        poging=poging-1
        print(f"dit wachtwoord is in corect je hebt nog {poging} pogingen")
    else:
        print("helaas je wachtwoord is incorect probeer het over 24 uur")
        break