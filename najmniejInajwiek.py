f= open('liczby2.txt','r')
lines = f.readlines()
f.close()

# print(lines[0],lines[1])
# print(len(lines[0])-1,len(lines[1])-1)
# print(lines[3],lines[4])
# print(len(lines[3])-1,len(lines[4])-1)
# print(lines.index(lines[3]))
count = 0
for num in lines:
    lines[count] = lines[count].strip()
    lines[count] = int(lines[count],2)
    count+=1
big = max(lines)
mini = min(lines)

# print(big)
print(lines.index(big)+1)
print(lines.index(mini)+1)