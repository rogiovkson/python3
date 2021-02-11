x = int(input("Введите действительное положительное число х "))
y = int(input("Введите целое отрицательное число y "))
def my_func(x,y):
    return x ** y
if x > 0 and y < 0:
    result = my_func(x,y)
    print(f'X в степени Y равен {result}')
else:
    print('ошибка')
#var 2
def my_func(x, y):
    a = 1
    for i in range(abs(y)):
        a = x * a
    if y >= 0:
        return a
    else:
        return 1 / a
print(my_func(float(input("Первое значение - ")), int(input("Второе значение - "))))
