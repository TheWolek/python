# Napisz funkcje, która sprawdzi brakujące liczby w liście
# oraz je wypisze
# lista jest posortowana rosnaco od 1 do 100

nums = [x for x in range(1,41)]
del nums[2]
print(nums)

def findMissing():
    missing = []
    for num in nums:
        if (nums[num+1]) - nums[num] != 1:
            missing.append(num)
            print('missing')
    return missing

print('brakujące liczby to',findMissing())