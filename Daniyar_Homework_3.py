data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
Numbers = []
Letters = []

for i in data_tuple:
    if type(i) == str:
        Letters.append(i)
    elif type(i) == int or type(i) == float:
        Numbers.append(i)
    elif type(i) == bool:
        Letters.append(i)
Letters.append(Letters.pop(Letters.index(True)))
Letters.reverse()
Letters[1] = 'G'
Letters[-2] = 'c'
Numbers.remove(6.13)
Numbers.insert(1, 2)
Numbers.sort()
Letters1 = tuple(Letters)
Numbers1 = tuple(Numbers)
print(Letters)
print(Numbers)
