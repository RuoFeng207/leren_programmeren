import time
while True:
    poging = 5
    while True:
        wachtwoord = input("Voer uw wachtwoord in: ")
        if wachtwoord =="humtidumtie217":
            print("Oke kom er maar in")
            break
        else:
            poging=poging-1
            if poging>0 and poging<6:
                print(f"dit wachtwoord is in corect je hebt nog {poging} pogingen")
            else:
                print("helaas je wachtwoord is incorect probeer het over 24 uur")
                time.sleep(86400)
                break
    if wachtwoord =="humtidumtie217":
        break
          