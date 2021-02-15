my_list = [2,3,3,4,5,9,23,54,54,87,10,9]
print(f'Исходный список - {my_list}')
new_list = [el for el in my_list if my_list.count(el) < 2  ]
print(f'Новый список - {new_list}')