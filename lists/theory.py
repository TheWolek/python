# my_list = []
# my_list = [1.2,'abc',true,['xyz']]
#   1.2     'abc'   true    ['xyz']
#    0        1       2        3
#   -4       -3      -2       -1                

# my_list[1] => 'abc'  my_list[3] => ['xyz']  my_list[3][0] => 'xyz'
# my_list[-1] => ['xyz'] 

# my_list[0:2] => [1.2,'abc',true]
# my_list[-1:-2] => [['xyz'],true]
# my_list[1:] => ['abc',true,['xyz']]

# my_list.index(true) => 1
# my_list.count() => 3
# my_list.sort() asc
# my_list.reverse()
# 'abc' in my_list => true

# my_list[0] = 12          [12,'abc',true,['xyz']]
# my_list[0:1] = [13,'def']        [13,'def',true,['xyz']] 
# my_list.append(150)          [13,'def',true,['xyz'],150] 

# my_list + [1,2]      [13,'def',true,['xyz'],150,1,2]
# ['re'] * 3        ['re','re','re'] 

# my_list.insert(1,3)      [13,3,'def',true,['xyz'],150,1,2]

# del my_list[1]       [13,'def',true,['xyz'],150,1,2]
# del my_list[-1:-3]       [13,'def',true,['xyz']]
# my_list.remove(13)       ['def',true,['xyz']]
# my_list.pop() => ['xyz']        ['def',true]
# my_list.pop(1) => true       ['def']
# my_list.clear()      []