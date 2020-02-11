# Napisz program wypisujący i podający wszystie możliwe kombinacje 
# liter z podanej listy (każda litera występuje raz)
import random
from math import factorial
char_list = ['a','e','i']

def rand():
    random.shuffle(char_list)
    print(''.join(char_list))

counter = 0
allposible = factorial(len(char_list))
while counter < allposible:
    rand()
    counter = counter +1

print('Istnieje ' + str(counter) + ' kombinacji')