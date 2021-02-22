class Clothes:
    def __init__(self, param):
        self.param = param
    @property
    def consumption(self):
        return f'Итого сумма затраченной ткани равна: \
    {self.param / 6.5 + 0.5 + 2 * self.param + 0.3}'
    def coat(self):
        return f'Сумма затраченной ткани равна на пальто:  \
{self.param / 6.5 + 0.5 :.2f}'
    def suit(self):
        return f'Сумма затраченной ткани равна на костюм:  \
{2 * self.param + 0.3 :.2f}'
clothes = Clothes(100)
suit = Clothes(60)
print(suit.suit())
print(clothes.coat())
print(Clothes.consumption)
 

