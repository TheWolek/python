def wyborProduktow():
    select = ''
    maxID = len(products)
    global basket
    basket = []
    while select != 'exit':
        select = input('podaj ID produktu / exit: ')
        try:
            select = int(select)
            if select <= maxID:
                basket.append(products[select])
            else:
                print('podaj poprawną liczbę (0-',maxID,')',sep='')
        except ValueError:
            print('podaj poprawną liczbę (0-',maxID,')',sep='')
            continue
    else:
        print('zamówiłeś następujące produkty:')

def policzKoszyk():
    global total
    total = 0
    print('Koszyk:')
    for product in basket:
        print(product[0],product[1],sep=' : ')
        total += product[1]
    print('W sumie:',total) 

#=============================

print('Wybierz produkty wpisując ich ID')
products = {
    1: ('piwo',3.5),
    2: ('pizza',35.0),
    3: ('ser żółty',3.5),
    4: ('tarta',10.0),
    5: ('bułka słodka',2.9)
}

for key, product in products.items():
    print(key,'.',product[0],' : ',product[1],sep='')

print('wpisz exit jeśli nie chcesz już kupować')

wyborProduktow()
policzKoszyk()

total2 = int(total)
while total2%10 != 0:
    total2+=1
print(1,total2,sep='. ')
print(2,total2+10,sep='. ')
Changes=(total2,total2+10)
selecting = True
while selecting:
    try:
        select = int(input('z ilu wydać? (1,2): '))
        if(select in [1,2]):
            selecting = False
        else:
            print('podaj poprawną liczbę (1-2): ')
            selecting = True
    except ValueError:
        print('podaj poprawną liczbę (1-2): ')
        selecting = True

policzKoszyk()
change = round(Changes[select-1]-total,2)
print('Suma:',total,'Do wydania z:',Changes[select-1],'Reszta:',change)