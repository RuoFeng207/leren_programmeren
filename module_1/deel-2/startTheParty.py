
gastheer=input("Wat is de naam van de gastheer/vrouw: ")
gasten = 4
drank = True
chips = True



#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
# # Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.
start_condition_2 = gastheer or gasten and chips and drank
# # Een feest met chips, maar zonder drank kan niet beginnen.
start_condition_3 = not chips and drank
# # Een feest met gasten kan niet beginnen als er geen chips en geen drank is.
start_condition_4 = gasten and chips and drank
# # Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.
start_condition_5 = gastheer and drank
# # Alleen chips is geen feest.
start_condition_6 = not chips 


if gastheer==("Ruo Feng") or not gastheer==("Van pelt") or start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6 and gasten >3 and not gasten>20 :
    
    print('Start the Party')

else:
    
    print('No Party')