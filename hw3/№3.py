def my_func(arg1, arg2, arg3):
    if (arg1 and arg2) > arg3:
        return arg1 + arg2
    elif(arg2 and arg3) > arg1:
        return arg2 + arg3
    else:
        return arg3 + arg1
print(f'Сумма наибольших двух аргументов - {my_func((int(input("Введите первый аргумент "))), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')



