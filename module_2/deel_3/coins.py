# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [50,20,10,500,200,100] # waarde munt

toPay = int(float(input('Amount to pay: '))* 100) # vraag hoeveel er betaald word
paid = int(float(input('Paid amount: ')) * 100) # vraag hoeveel je betaald hebt
change = paid - toPay # verschil tussen bedrag en betaald bedrag

while change > 0 and len(coinValues) > 0: # als de verandering 0 is en de convalues is 0 zet regel 12-20 aan het werk

  coinValue = coinValues.pop(0) # verwijderd index 0 uit coinvalues
  nrCoins = change // coinValue # verschil delen door coinvalue // = afronden naar beneden

  if nrCoins > 0: # als nr coins groter is dan 0 zet regel 17=20 in werking
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # hoeveelheid munten en waarden printen
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # vraag hoeveel je terug betaald heb
    change -= nrCoinsReturned * coinValue #change =change - nrcoinsreturned
print(f"paid back ")

if change > 0: #change groter dan 0 zet regel 22-25 in werking
  print('Change not returned: ', str(change) + ' cents') # ptint hoeveel er nog niet betaald is 
else:
  print('done')