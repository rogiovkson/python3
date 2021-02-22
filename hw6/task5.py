class Stationery:
    def __init__(self, tittle):
        self.tittle = tittle
    def draw(self):
        return ('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        return(f'Зарисовка {self.tittle}')
class Pencil(Stationery):
    def draw(self):
        return(f'Подрисовка {self.tittle}')
class Handle(Stationery):
    def draw(self):
        return(f'Дорисовка {self.tittle}')
a_1 = Stationery(())
print(a_1.draw())
a_2 = Pen('карандашом')
print(a_2.draw())
a_3 = Pencil('ручкой')
print(a_3.draw())
a_4 = Handle('маркером')
print(a_4.draw())


