import random

randomList = []
i = int(input('Введите кол-во чисел списка\n'))
for n in range(0, i):
    randomList.append(random.randrange(100, 1000,2))
print(f'Список из {i} чисел - {randomList}')

from functools import reduce
multiplying = reduce(lambda x, y: x*y, randomList)
print(multiplying)