# set - nie uporządkowany zestaw. Każdy element jest unikalny (bez duplikatów) i nie mutowalny
# set sam w sobie jest mutowalny. Można dodawać i usuwać elementy
# używany do operacji matematycznych na zbiorach: suma, część wspólna, różnica

# my_set = {1,2,3}
# my_set = {1.2,'hello',(1,2,3)}

# my_set = {}   type(my_set) => dictionary
# my_set = {1,2,3}  type(my_set) => set
# my_set = set()  type(my_set) => set

# my_set = {1,2,3}
# my_set.add(4)         {1,2,3,4}
# my_set.uppdate([3,4,5])       {1,2,3,4,5}
# my_set.update([4,5],{1,6,8})      {1,2,3,4,5,6,8}

# my_set.discard(4)         {1,2,3,5,6,8}
# my_set.clear()

# A = {1,2,3}   B = {2,4,1,5}
# A.union(B) ; A | B => {1,2,3,4,5}
# A.intersection(B) ; A & B => {2,1}
# A.diffrence(B) ; A - B => {3}