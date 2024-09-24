print("Welk seizoen vind jij het fijnst?\nA) Lente\nB) Zomer\nC) Herfst\nD) Winter")
gekozen_seizoen = input('? ').lower()
weer_type = ""
if (gekozen_seizoen == 'a' or gekozen_seizoen=='c'):
    gekozen_seizoen=gekozen_seizoen.lower()
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif (gekozen_seizoen == 'a'or gekozen_seizoen=='b'):
    gekozen_seizoen=gekozen_seizoen.lower()
    weer_type='warm'
else:
    weer_type = 'koud'
    gekozen_seizoen=gekozen_seizoen.lower()

if len(weer_type)>0:
    print(f'Dus jij houd van {weer_type} weer!')