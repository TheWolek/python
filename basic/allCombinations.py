# Napisz program wypisujący i podający wszystie możliwe kombinacje liter z podanej listy
import random
from math import factorial
char_list = ['a','e','i','o','u']

def rand():
    random.shuffle(char_list)
    print(''.join(char_list))

def silnia(n):
    if n>1:
        return n*silnia(n-1)
    elif n in (0,1):
        return 1

counter = 0
allposible = factorial(len(char_list))
while counter < allposible:
    rand()
    counter = counter +1

print('Istnieje ' + str(counter) + ' kombinacji')