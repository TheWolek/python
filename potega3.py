potegi = []
i = 0
counter = 0

while True:
    p=3**i
    potegi.append(p)
    if p>100000:
        break
    i+=1

#print(potegi)

f = open('liczby.txt','r')
liczby = f.readlines()
f.close()
#print(liczby)

for num in liczby:
    num = int(num.strip())
    if num in potegi:
        print(num)
        counter += 1

print('odp:',counter)