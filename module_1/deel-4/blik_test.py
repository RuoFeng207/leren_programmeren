from test_lib import test,report
from math import pi
from blik_op_functies import calculate_cilinder_content

expected= 251.3 #Verwacht
result = round (calculate_cilinder_content(diameter=8.0, height=5.0),1)  #krijgt
test("TEST inhout = 251.3 in cm ", expected, result)

expected= 665.2 #Verwacht
result = round (calculate_cilinder_content(diameter=11.0, height=7.0),1)  #krijgt
test("TEST inhout = 665.2 in cm ", expected, result)

expected= 1781.3 #Verwacht
result = round (calculate_cilinder_content(diameter=18.0, height=7.0),1)  #krijgt
test("TEST inhout = 1781.3 in cm ", expected, result)

expected= 353.4 #Verwacht
result = round (calculate_cilinder_content(diameter=15.0, height=2.0),1)  #krijgt
test("TEST inhout = 353.4 in cm ", expected, result)

expected= 0.0 #Verwacht
result = round (calculate_cilinder_content(diameter=0.0, height=6.0),1)  #krijgt
test("TEST inhout = 0.0 in cm ", expected, result)

report()