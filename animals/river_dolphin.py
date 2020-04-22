from animals import Animal
from interfaces import IFreshwater, Identifiable, ISwimming

class RiverDolphin(Animal, IFreshwater, Identifiable, ISwimming):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        self.__food = ( "Trout", "Mackarel", "Salmon", "Sardine" )

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The dolphin ate {food} for a meal')
        else:
            print(f'The dolphin rejects the {food}')


    def __str__(self):
        return f'River Dolphin [{self.id.hex[:8]}]. Eeee EeeEEeeeeEE!'
