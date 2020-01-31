# Napisz funkcje przyjmującą dwa argumenty ("abc","xyz") 
# tworzącą jeden łańcuch "xyc abz"
def concat(str1,str2):
    Newstr1 = str2[0:2] + str1[-1]
    Newstr2 = str1[0:2] + str2[-1]

    return Newstr1 + ' ' + Newstr2

print(concat('abc','xyz'))