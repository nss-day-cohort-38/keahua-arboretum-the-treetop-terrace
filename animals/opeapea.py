from animals import Animal
from interfaces import Identifiable, IFlying

class Opeapea(Animal, Identifiable, IFlying):

    def __init__(self):
        Animal.__init__(self, "Opeapea")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        self.__food = { "Mosquito", "Beetle", "Berry" }

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The bat ate {food} for a meal')
        else:
            print(f'The bat rejects the {food}')

    def __str__(self):
        return f'Opeapea (Hawaiian Hoary Bat) [{self.id.hex[:8]}]. Screeeee!'

