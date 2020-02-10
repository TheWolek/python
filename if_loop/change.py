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
    return total

def ZiluReszta():
    global total2,Changes
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
                return Changes[select-1]
            else:
                print('podaj poprawną liczbę (1-2): ')
                selecting = True
        except ValueError:
            print('podaj poprawną liczbę (1-2): ')
            selecting = True

def init():
    global products,basket,total,total2,Changes
    # mozna też pobrać dane z zewnętrznego pliku i stworzyć poniższą listę c:
    products = {
        1: ('piwo',3.5),
        2: ('pizza',35.0),
        3: ('ser żółty',3.5),
        4: ('tarta',10.0),
        5: ('bułka słodka',2.9)
    }
    basket = []
    total = 0
    total2 = 0
    Changes = ()


# =================================================
def main():
    print('Wybierz produkty wpisując ich ID')
    init()

    # wyświetlenie listy
    for key, product in products.items():
        print(key,'.',product[0],' : ',product[1],sep='')

    print('wpisz exit jeśli nie chcesz już kupować')

    wyborProduktow()
    total = policzKoszyk()
    print('W sumie:',total) 
    ChangeSelection = ZiluReszta()
    total = policzKoszyk()
    change = round(ChangeSelection-total,2)
    print('Suma:',total,'Do wydania z:',ChangeSelection,'Reszta:',change)

main()