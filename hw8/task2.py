dividend = int(input('Введите делимое \n'))
quotient = int(input('Введите делитель \n'))
try:
    res = dividend / quotient
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("Программа завершена")