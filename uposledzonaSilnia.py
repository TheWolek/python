import math
output = []
f = open('liczby.txt.','r')
liczby = f.readlines()
f.close()

for liczba in liczby:
    liczba = liczba.strip()
    c = 0
    for digit in liczba:
        c+= math.factorial(int(digit))
    if int(liczba)==c:
        print(liczba)

#print(output)