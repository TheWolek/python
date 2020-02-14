# Napisz funkcje, która oblicza silnie z podanej liczby
# liczba wpisywana jest z klawiatury

# 3! = 1 * 2 * 3 = 6

def factorial(n):
    fact = 1
    for x in  range(2,n+1): # 2..3..stop9*
        fact *= x
    return fact

print(factorial(3))
print(factorial(10))
