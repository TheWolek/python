mystr = ""
mystr += 'aBC'
mystr *= 2

# ideksy takie same jak lista   
mystr[:-1]
mystr.find('a') # zwraca index pierwszego wystąpienia
mystr.isalpha() # sprawdza czy zawiera tylko znaki alfabetu
mystr.isdigit() # sprawdza czy zawiera tylko cyfry
mystr.isalnum() # sprawdza czy zawiera znaki alfabetu i cyfry

','.join(["a","b","c"])
mystr.lower()
mystr.lstrip() # zwraca łańcuch bez spacji na początku
mystr.replace('a','D') # zwraca kopie łańcha, wystąpienia pierwszego argumentu zamienione na drugi
mystr.split() # dzieli łańcuch i tworzy listę wszystkich wykrytych podłańcuchów
mystr.startswith('D')
mystr.endswith('c')

print('2020-01-01' < '2020-01-20')