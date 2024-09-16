
gastheer = True
gasten = True
drank = True
chips = True


gastheer= input("Wat is de naam van je gastheer/vrouw: ") 

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
# Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.
start_condition_2 = gastheer or gasten and chips and drank
# Een feest met chips, maar zonder drank kan niet beginnen.
start_condition_3 = chips or chips and drank
# Een feest met gasten kan niet beginnen als er geen chips en geen drank is.
start_condition_4 = gasten and chips and drank
# Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.
start_condition_5 = gastheer and drank
# Alleen chips is geen feest.
start_condition_6 = gasten and gastheer and drank


if start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6:
    gastheer==("Ruo Feng")
    print('Start the Party')

else:
    gastheer==("Rudi")
    print('No Party')