def switcher(index):
    switch = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four'
    }
    return switch.get(index, "null")


select = int(input('Podaj liczbę: '))
print(switcher(select))
