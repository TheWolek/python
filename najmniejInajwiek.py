f= open('liczby2.txt','r')
lines = f.readlines()
f.close()

# print(lines[0],lines[1])
# print(len(lines[0])-1,len(lines[1])-1)
# print(lines[3],lines[4])
# print(len(lines[3])-1,len(lines[4])-1)
# print(lines.index(lines[3]))

biggest = int(lines[0],2)