def addition(nummer_1:float, nummer_2:float):
    add =nummer_1+nummer_2
    return add
get_som = lambda nummer_1,nummer_2: f"{nummer_1} + {nummer_2} = {nummer_1+nummer_2}"
print(get_som(5,3))

def subtraction(nummer_1:float, nummer_2:float):
    subtract = nummer_1 - nummer_2
    return subtract
get_som = lambda nummer_1,nummer_2: f"{nummer_1} - {nummer_2} = {nummer_1-nummer_2}"
print(get_som(5,3))

def multiplication(nummer_1:float, nummer_2:float):
    multipli = nummer_1 * nummer_2
    return multipli
get_som = lambda nummer_1,nummer_2: f"{nummer_1} x {nummer_2} = {nummer_1*nummer_2}"
print(get_som(5,3))

def division(nummer_1:float, nummer_2:float):
    divis = nummer_1/nummer_2
    return divis
get_som = lambda nummer_1,nummer_2: f"{nummer_1} : {nummer_2} = {nummer_1/nummer_2:.1f}"
print(get_som(5,3))
# print(addition(10,3))
# print(subtraction(10,3))
# print(multiplication(10,3))
# print(division(10,3))