licznik = 0
f = open('test.txt','r',encoding='utf-8')
linia = f.readline()
while linia != '':
    licznik += 1
    linia = f.readline()
f.close()
print('Linie w pliku:',licznik)