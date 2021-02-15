dictionary = {}
with open('task6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
#         subject, lection, practice, lab = line.split() - не присваивает
        line = line.split()
        num_list = [int(num) for num in filter(lambda num: num.isnumeric(), line)]

        print(sum(num_list))