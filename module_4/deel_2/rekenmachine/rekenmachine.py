print("Wat wild u doen?")
print("A) getallen optellen")
print("B) getallen aftrekken")
print("C) getallen vermenigvuldigen")
print("D) getallen delen")
print("E) getallen ophogen")
print("F) getallen verlagen")
print("G) getallen verdubbelen")
print("H) getallen halveren")
print("I) niet")
lijst = ["a","b","c","d","e","f","g","h","i"]
while True:
    choice = input("kies: ").lower()
    if choice in lijst:
        break
    else:
        print("")
        print("Deze optie is niet mogelijk")
    
