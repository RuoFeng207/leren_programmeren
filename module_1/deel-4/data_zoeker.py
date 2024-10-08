from test_lib import test, report

data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'


def get_value(data: str, separator: str, position: int) -> str:
  waarde =data.split(separator)
  if 0 <= position< len(waarde):
    return waarde [position] # read value at position of split_values
  else:
    waarde = None
  



verwacht = "Bram:6"
krijgt = get_value(data,",",8)
test("naam verwacht Bram",verwacht,krijgt)

verwacht = "Sofie:8"
krijgt = get_value(data,",",0)
test("naam verwacht Sopie",verwacht,krijgt)

verwacht = "Emma:7"
krijgt = get_value(data,",",1)
test("naam verwacht Emma",verwacht,krijgt)

verwacht = "Ahmed:9"
krijgt = get_value(data,",",2)
test("naam verwacht Ahmed",verwacht,krijgt)

verwacht = "Daan:6"
krijgt = get_value(data,",",3)
test("naam verwacht Daan",verwacht,krijgt)
report()