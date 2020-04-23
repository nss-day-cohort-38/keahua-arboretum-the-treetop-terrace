from animals import Animal
from interfaces import Identifiable, IFlying, IBiome

class Pueo(Animal, Identifiable, IFlying, IBiome):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IBiome.__init__(self, False, True, True, False, False, False)
        self.__food = ("Mouse", "Rat")

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
