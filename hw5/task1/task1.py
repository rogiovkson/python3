my_f = open('task1.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line + '\n')
    line = input('Введите текст \n')
    if not line:
        break
my_f.close()
 
