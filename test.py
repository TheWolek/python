# list1 = [x for x in range(2,11)]
# list2 = list(map(lambda x: 2 ** x, list1))
# print(list2)

def isPowerOfTwo(n):
    return n > 0 and (n & (n-1) == 0)

print(isPowerOfTwo(4))