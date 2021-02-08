name = input('Введите имя\n')
surname = input('Введите фамилию\n')
birthday = int(input('Введите год рождения\n'))
city = input('Введите город проживания\n')
email = input('Введите e-mail\n')
phone = int(input('Введите номер а\n'))


def args(arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
    print(f'Имя - {arg_1}, Фамилия - {arg_2}, Год рождения - {arg_3}, Город проживания - {arg_4}, E-mail - {arg_5}, Номер телефона - {arg_6}')

args(arg_1 = name, arg_2 = surname, arg_3 = birthday, arg_4 = city, arg_5 = email, arg_6 = phone)