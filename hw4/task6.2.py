from itertools import cycle
my_list = [True, 'XYZ', 556, None]
count = 0
n = int(input('Укажите длину генератора\n'))
for el in cycle(my_list):
    count += 1
    if count >= n:
        print('Генерация списка завершена')
        break
    else:
        print(el)