class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
class Printer(Warehouse):
    def to_print(self):
        return f'Принтер {self.name} печатает {self.numb} документов. Таких устройств {self.quantity}'


class Scanner(Warehouse):
    def to_scan(self):
        return f'Сканнер {self.name} сканирует {self.numb} документов. Таких устройств {self.quantity}'


class Xerox(Warehouse):
    def to_copier(self):
        return f'Ксерокс {self.name} копирует {self.numb} документов. Таких устройств {self.quantity}'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Xerox('Xerox', 1500, 1, 15)
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
