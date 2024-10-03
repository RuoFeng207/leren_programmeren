#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_lib import test, report
from meten_is_weten_functie import num

expected = "Getal 1 en 2 zijn even groot" #resultaat     
result = num(num1=3, num2=3) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = "Maximum: 3 en minimum: 2 " #resultaat
result = num(num1=3,num2=2) #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected ="Maximum: 7 en minimum: 3" #resultaat
result = num(num1=3, num2=7)#roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()