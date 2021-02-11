

def my_func():
    hours = int(input('Введите количество отработанных часов : '))
    hourly_rate = int(input('Введите суммы оплаты труда за 1 час : '))
    bonus = int(input('Укажите размер премии - '))
    salary = hours * hourly_rate
    return salary + bonus
print(f'Размер заработной платы составил: {my_func() }')
argv = my_func()