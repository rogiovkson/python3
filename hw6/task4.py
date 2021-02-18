class Car:
    def __init__(self, speed, color, name, is_police = None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return (f'машина марки {self.name} тронулась.')
    def stop(self):
        return(f'{self.name} остановилась.')
    def turn(self,direction):
        return(f'{self.name} повернула {direction}.')
    def show_speed(self):
        return (f'Скорость машины - {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return (f'Превышение скорости, ваша скорость - \
{self.speed} км/ч.')
        return(f'скорость допустимых пределах - {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Превышение скорости, ваша скорость - \
{self.speed} км/ч.')
        return (f'скорость допустимых пределах - {self.speed} км/ч')
class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return (f'Ваша скорость - {self.speed} км/ч. С мигалками можно')
        return (f'скорость допустимых пределах - {self.speed} км/ч')
class SportCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return (f'Скоростть {self.name} {self.speed} км/ч. \
С такой скоростью лучше ездить по гоночному треку')
        return (f'Скорость в допустимых пределах - {self.speed} км/ч')
    pass


town = TownCar(70, 'Синяя', 'BMW', False)
print(town.color, town.go(), town.stop(), town.turn('налево'), town.turn('направо'), town.show_speed())
work = WorkCar(30, 'Зеленая', 'UAZ', False)
print(work.color, work.go(), work.stop(), work.turn('налево'), work.turn('направо'), work.show_speed())
police = PoliceCar(110, 'Белая', 'Ford', True)
print(police.color, police.go(), police.stop(), police.turn('налево'), police.turn('направо'), police.show_speed())
sport = SportCar(210, 'Желтая', 'Lamborgini', False)
print(sport.color, sport.go(), sport.stop(), sport.turn('налево'), sport.turn('направо'), sport.show_speed())