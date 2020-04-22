from animals import Animal
from interfaces import Identifiable, IFlying

class Pueo(Animal, Identifiable, IFlying):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        self.__food = {"Mouse", "Rat"}

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The owl ate {food} for a meal')
        else:
            print(f'The owl rejects the {food}')

    def __str__(self):
        return f'Pueo owl [{self.id.hex[:8]}]. Hoo HOO! Hoo HOO!'
