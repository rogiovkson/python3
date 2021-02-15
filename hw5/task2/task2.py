my_file = open('task2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('task2.txt', 'r')
content = my_file.read().split('\n')
sub = ' '
for i in range(len(content)):
    print(f'Количество слов в {i+1}-й строке = {content.count(sub)+1}')
my_file.close()