import random

# #selecteer 2 nummers
num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

# #vraag om een antwoord
number =(input(f'Weet jij wat {num1}+{num2} is? '))

# #geef reactie op het antwoord
try:
    number=int(number)

    if (number == num1+num2):
        print('Dat is juist')
    elif(number != num1+num2):
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen heel getal!')
