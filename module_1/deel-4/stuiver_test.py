from test_lib import test, report
from stuivers import afronden_5cent

verwacht =bedrag =62.60
krijgt = afronden_5cent (bedrag= 62.60)
test ("Ik verwacht 62.60 euro",verwacht,krijgt)

verwacht =bedrag =76.60
krijgt = afronden_5cent (bedrag= 76.61 )
test ("Ik verwacht 76.60 euro",verwacht,krijgt)

verwacht =bedrag = 28.80
krijgt = afronden_5cent (bedrag=28.82 )
test ("Ik verwacht 28.80 euro",verwacht,krijgt)

verwacht =bedrag =2.25
krijgt = afronden_5cent (bedrag= 2.23)
test ("Ik verwacht 2.25 euro",verwacht,krijgt)

verwacht =bedrag =28.35
krijgt = afronden_5cent (bedrag= 28.34)
test ("Ik verwacht 28.35w euro",verwacht,krijgt)

report()
