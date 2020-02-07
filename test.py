# list1 = [x for x in range(2,11)]
# list2 = list(map(lambda x: 2 ** x, list1))
# print(list2)
t = []
i = 0
p = 1
counter = 0
while True:
    p = 3**i
    t.append(p)
    if p>100000:
        break
    i+=1

f = open('liczby.txt.','r')
lines = f.readlines()
f.close()

for line in lines:
    line = int(line.strip())
    if line in t:
        counter += 1
        print(line)

print('odp:',counter)