# klasa nie ma nic wspólnego z istniejącym obiektem, sama klasa go nie tworzy
class Base:
    __counter = 0 # postawienie __ przed nazwa tworzy prywatną zmienna dla klasy
    def __init__(self,r=0,i=0): # przy inicjowaniu (tworzeniu) obiektu na tej klasie wykona się funkcja __init__
        self.real = r # self to obiekt dla którego będzie przypisana własność lub odczytana
        self.imag = i
        Base.__counter += 1 # przy każdym zainicjowaniu obiektu z tej klasy licznik zostaje zwiększony o 1

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

ob = Base(2,3)  # utworzenie obiektu
ob.getData() # wywołanie metody getData() obiektu ob

ob2 = Base(5)  # utworzenie drugiego obiektu
ob2.attr = 10 # przypisanie wartości do nowej własności obiektu ob2
print(ob2.real,ob2.imag,ob2.attr) # wyświetlanie pojedyńczych własności obiektów
print(ob._Base__counter) # wyświetlenie prywatnego licznika
print(ob.__dict__,ob2.__dict__) # __dict__ wyświetla wszystkie własności obiektu w formie słownika