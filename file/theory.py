# 1. Open
# 2. Read or Write
# 3. Close file

# f = open('test.txt','rw')
# f = open('test2.txt','w+') jesli plik nie istnieje utworzy go
# f = open('test3.txt','a') dopisywanie danych

# f.close()

#  with open('test.txt','rw') as f:
#      f.write('first line\n')
#      f.write('second line')

# f = open('test.txt','r')
# f.read() => cały plik

# for line in f:
#   print(line, end = '')

# cały plik linia po linij
# fl = f.readlines()
# form line in fl:
#   print(line)