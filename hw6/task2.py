class Road: #определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25 #кг
        self.height = 5 #см
    def asphalt(self):
        asphalt = self._length * self._width * self.weight * self.height / 1000
        print(int(asphalt))

r = Road(5000, 20)
r.asphalt()
#Например: 20 м*5000 м*25 кг*5 см = 12500 т.
