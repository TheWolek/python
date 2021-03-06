#dictionary - nie uporządkowany zbiór danych. Klucz: Wartość

my_dict = {}
my_dict = {
  'name': 'john',
  'age': 20,
  1: [1,2,3]
}
my_dict['name'] #=> 'john'
my_dict['surname'] = 'kowalski'   #{'name':'john','age':20,1:[1,2,3],'surname':'kowalski'}
my_dict.get('name') #=> 'john'
my_dict.get('test') #=> 'None'
#my_dict['test'] #=> ERROR

my_dict.keys() #=> ['name','age',1,'surname']
my_dict.values() #=> ['john',20,[1,2,3],'kowalski']
len(my_dict) #=> 4
my_dict.update({2:(4,5,6)})

my_dict.pop('name') #=> 'john'     {'age':20,1:[1,2,3],'surname':'kowalski'}
del my_dict['surname']
my_dict.clear()       #{}