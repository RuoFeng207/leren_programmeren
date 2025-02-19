from functions_rekenen_2 import *
from test_lib import test, report
expected = 10
calculated = addition(nummer_1= 5,nummer_2=5)
test("resultaat:",expected,calculated)

expected = 5
calculated = subtraction(nummer_1= 10,nummer_2=5)
test("resultaat:",expected,calculated)

expected = 10
calculated = addition(nummer_1= 5,nummer_2=5)
test("resultaat:",expected,calculated)

report()