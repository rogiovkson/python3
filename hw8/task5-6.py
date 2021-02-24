class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        print(f'Для выхода - Q, продолжение - Enter')
        while True:
            try:
                unit = input(f'Введите наименование ')
                unit_p = int(input(f'Введите цену за ед '))
                unit_q = int(input(f'Введите количество '))
                unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Текущий список -\n {self.my_store}')
            except:
                return f'Ошибка ввода данных'

            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q == 'Q' or q == 'q':
                self.my_store_full.append(self.my_store)
                print(f'Весь склад -\n {self.my_store_full}')
                return f'Выход'
            else:
                return Warehouse.reception(self)


class Printer(Warehouse):
    def to_print(self):
        return f'Печать {self.numb} документов'


class Scanner(Warehouse):
    def to_scan(self):
        return f'Сканирование {self.numb} документов'


class Copier(Warehouse):
    def to_copier(self):
        return f'Копия  {self.numb} документов'



