class digit(ValueError):
    pass
my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise digit(value)
        my_list.append(value)
    except ValueError:
        print('Не число!')
print(f'ваш список - {my_list}')

