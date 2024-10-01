#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_lib import test, report
from meten_is_weten_functie import num1_grootst,num2_grootst,num_gelijk,num1,num2

expected = num1==num2 #resultaat
result = num_gelijk #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = num1>num2 #resultaat
result =num2_grootst  #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected = num2>num1 #resultaat
result= num2_grootst #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()