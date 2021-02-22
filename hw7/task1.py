# import random
# class Matrix:
#     def __init__(self, row, col):
#         self.matrix = [[random.randrange(-50, 50) for a in range(col)] for b in range(row)]
#     #
#     # def __str__(self):
#     #     matrix = self.matrix
#     #     for im in range(len(matrix)):
#     #         return print((matrix[im]))
#     # def print(self):
#     #     matrix = self.matrix
#     #     for im in range(len(matrix)):
#     #         print(matrix[im])
# Matrix(3,3).print()
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:5}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)
m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))