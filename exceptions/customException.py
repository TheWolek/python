class PizzaError(Exception):
    def __init__(self, pizza, wiadomosc):
        # Exception.__init__(wiadomosc)
        self.pizza = pizza	
        self.wiadomosc = wiadomosc

class ZaDuzoSeraError(PizzaError):
    def __init__(self, pizza, ser, wiadomosc):
        PizzaError.__init__(self, pizza, wiadomosc)
        self.ser = ser

def zrobPizze(pizza,ser):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza,'brak wybranej pizzy w menu')
    if ser > 100:
        raise ZaDuzoSeraError(pizza,ser,'za dużo sera')
    print(pizza,ser)

for (pizza,ser) in [('calzone',110), ('margherita',100), ('mafia',50)]:
    try:
        zrobPizze(pizza,ser)
    except PizzaError as pe:
        print('Error#',pe, ':', pe.pizza)
    except ZaDuzoSeraError as tmce:
        print('Error#',tmce,':',tmce.ser)