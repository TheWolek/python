# Napisz funkcje, która policzy wystąpienia każzdej z liter w podanym łańcuchu

def count_chars(str):
    dict = {}
    for letter in str:
        keys = dict.keys()
        if letter in keys:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

print(count_chars('test'))