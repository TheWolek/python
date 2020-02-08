f = open('liczby2.txt','r')
lines = f.readlines()
f.close()

found = 0
# print(lines[1])
# zeros = lines[1].count('0')
# unos = lines[1].count('1')
# print('zeros:',zeros,'unos:',unos)

for line in lines:
    zeros = line.count('0')
    unos = line.count('1')
    if zeros > unos:
        found += 1

print(found)
