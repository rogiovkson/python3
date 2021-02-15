from itertools import count, cycle

first = (int(input('Введите первое число списка\n')))
last = (int(input('Введите последнее число списка\n')))
for i in count(first):
    if i > last:
        break
    else:
        print(i)



