sum = 0
exit = False
while exit == False:
    my_list = input('Введите числа через пробел или "f" для выхода\n').split()
    current_sum = 0
    for el in range(len(my_list)):
        if my_list[el] == 'f':
            exit = True
            break
        else:
            current_sum = current_sum + int(my_list[el])
    sum = sum + current_sum
    print(f' Промежуточная cумма введенных чисел = {sum}')
print(f' Сумма введенных чисел = {sum}')
