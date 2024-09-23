a = str(input('Geef een woord: '))
a=len(a)
b = str(input('Geef nog een woord: '))
b=len(b)
if a > b:     
    print('Woord 1 heeft meer letters dan woord 2')
elif a < b:   
    print('Woord 1 heeft minder letters dan woord 2')
else:                   
    print('Woord 1 en woord 2 hebben evenveel letters')