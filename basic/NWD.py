# Napisz funkcje, która poda NWD dwóch podanych liczb

def NWD(x,y):
    nwd = 1
    if x%y == 0:
        return y

    for k in range(int(y/2),0,-1):
        if (x%k==0 and y%k==0):
            nwd = k
            break

    return nwd

print(NWD(282,78))