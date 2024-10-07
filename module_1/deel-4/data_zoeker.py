# toets_data has name:score combinations separated by a komma
def get_value(toets_data: str, separator: str, position: int) -> str:
    toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
    separator = ','
    position= 8 # position of Bram, first position starts with 0
    
    splitted_strings = toets_data.split(separator) # string splits itself into collection of strings
    if 0 <= position< len(splitted_strings):
        value = splitted_strings[position] # read value at position of split_values
    else:
        value = None
    
    return(value) # prints: Bram:6

print(get_value("Bram:6",",",9))

