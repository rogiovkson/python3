my_list = [1, 5, 10, 2, 3, 100, 50]
print(f'Исходный список - {my_list}')
new_list = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el-1]]
print(f' Новый список - {new_list}')
