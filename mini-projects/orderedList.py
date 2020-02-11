# Napisz funkcje, która sprawdzi brakujące liczby w liście
# oraz je wypisze
# lista jest posortowana rosnaco od 1 do 100

from random import randrange
nums = [x for x in range(1,41)]
for n in range(1,10):
    rand = randrange(0,39)
    del nums[rand]
print(nums)

def findMissing():
    missing = []
    for num in nums:
        if (nums[num+1]) - nums[num] != 1:
            missing.append(num)
            print('missing')
    return missing

print('brakujące liczby to',findMissing())