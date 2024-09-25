import random

# #selecteer 2 nummers
num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

# #vraag om een antwoord
number = int(input(f'Weet jij wat {num1}+{num2} is? '))

# #geef reactie op het antwoord
try:
#     if int(number == num1+num2):
#         print('Dat is juist')
#     elif int(number != num1-num2):
#         print('Nee dat klopt niet')
# except ValueError:
#     print('Dat is geen nummer!')

# import random

# Select two numbers
# num1 = random.randint(1, 10)
# num2 = random.randint(5, 15)

# Ask the user for their answer
# number = input(f"Weet jij wat {num1}+{num2} is? ")

try:
    # Convert the user's input to an integer
    number = int(number)
    if number == num1 + num2:
        print("Dat is juist")
    else:
        print("Nee dat klopt niet")
except ValueError:
    print("Dat is geen nummer!")