# name = '\\kat\\plik'
# name = '/kat/plik'

# 1. Open
# 2. Read or Write
# 3. Close file

# r - read, plik musi istniec
# w - write, plik nie musi istniec, ponowny zapis usunie zawartos
# a - append, plik nie musi istniec, dopisywanie na koncu pliku, zapis i odczyt
# r+ - read + update, plik musi istniec
# w+ -  write + update, plik nie musi istniec, poprzednia zawartos zostanie nietknieta

f = open('test.txt','r', encoding='utf-8')
print(f.read())
f.close()
# f = open('test2.txt','w+')
# f = open('test3.txt','a')

# f.close()

# for line in f:
#   print(line, end = '')

# cały plik linia po linij
# fl = f.readlines()
# form line in fl:
#   print(line)