# Napisz program z funkcją pobierający dwie liczby z klawiatury 
# i zwracający ich iloczyn 
# lub jeśli jest on większy od 1000 - ich sumę 

num1 = int(input('Podaj pierwszą liczbę: '))
num2 = int(input('Podaj drugą liczbę: '))

def licz(x,y):
    if x*y > 1000:
        return x+y
    else:
        return x*y

print(licz(num1,num2))