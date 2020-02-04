my_list = []
data = 1,2,3,4        #(1,2,3,4) tuple
my_list = list(data)      #[1,2,3,4] list
my_list = [1.2,'abc',True,['xyz']]
#   1.2     'abc'   True    ['xyz']
#    0        1       2        3
#   -4       -3      -2       -1                

my_list[1] # => 'abc'
my_list[len(my_list)-1] # => ['xyz']  
my_list[3][0] # => 'xyz'
my_list[-1] # => ['xyz'] 

my_list[0:2] # => [1.2,'abc',True]
my_list[-1:-2] # => [['xyz'],True]
my_list[1:] # => ['abc',True,['xyz']]

my_list.index(True) # => 1
len(my_list) # => 3
#my_list.sort() # najlepiej gdy mamy dane tego samego typu
my_list.reverse()
'abc' in my_list # => True

my_list[0] = 12          #[12,'abc',True,['xyz']]
my_list[0:1] = [13,'def']        #[13,'def',True,['xyz']] 
my_list.append(150)          #[13,'def',True,['xyz'],150] 

my_list + [1,2]      #[13,'def',True,['xyz'],150,1,2]
['re'] * 3        #['re','re','re'] 

my_list.insert(1,3)      #[13,3,'def',True,['xyz'],150,1,2]

del my_list[1]       #[13,'def',True,['xyz'],150,1,2]
del my_list[-1:-3]       #[13,'def',True,['xyz']]
my_list.remove(13)       #['def',True,['xyz']]
my_list.count(True) #=> 1
my_list.pop() #=> ['xyz']        ['def',True]
my_list.pop(1) #=> True       ['def']
my_list.clear()      #[]

#sum(list) - zwróci sume elementów listy (jeśli wszyskie są int lub float)
#min(list) - zwróci najmniejszy z elementów listy (jeśli wszyskie są int lub float)
#max(list) - zwróci największy z elementów listy (jeśli wszyskie są int lub float)

for item in my_list:
    print('')

my_list = ['xyz',2]
my_list2 = my_list        
my_list2[0] = 'abc'
print(my_list) #=> ['abc',2]
#oba wskazuja na to samo miejsce w pamieci

#by skopiować listę (jako nowy całkiem obiekt) można użyć slice
my_list = ['xyz',2]
my_list2 = my_list[:]
my_list2[0] = 'abc'
print(my_list,my_list2) #=> ['xyz',2],['abc',2]

myList = [8, 10, 6, 2, 4]

# sortowanie babelkowe od kuchni:
for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i]

#[expression for element in list if conditional]
my_list = [5,210,23,41,23,2]
my_list2 = [num for num in my_list if num%2 == 0]
print(my_list2)