f = open('liczby2.txt','r')
lines = f.readlines()
f.close()

podz2 = 0
podz8 = 0

# print(lines[1])
# print(lines[1][-2])
# print(lines[1][-4:-1])

for line in lines:
    if line[-2] == '0':
        podz2 += 1
    
    if line[-4:-1] == '000':
        podz8 += 1

print('ilosc podzielnych przez 2:',podz2,'ilosc podzielnych przez 8:',podz8)