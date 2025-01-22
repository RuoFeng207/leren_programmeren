def gegevens():
    naam = input("Wat is je naam? ").capitalize()
    while True:
        try: 
            leeftijd = int(input("Wat is je leeftijd "))
            break
        except ValueError:
            print("Je mag aleen hele cijfers doen")
    d= {"naam":naam,
    "leeftijd":leeftijd}
    print(f"{d["naam"]} is {d["leeftijd"]} jaar")
    return d

gegevens()