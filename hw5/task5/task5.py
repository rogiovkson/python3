try:
    with open ('task5.txt', 'w') as my_file:
        line = input('Введите цифры через пробел \n')
        my_file.write(line)
        my_numb = line.split()
        print(sum(map(int,my_numb)))
except IOError:
        print("Ошибка в файле")
except ValueError:
        print('Необходимо ввести цифры через пробел')
finally:
    my_file.close()

