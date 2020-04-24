from animals import Animal
from interfaces import IAquatic, Identifiable, ISwimming, ISaltwater, IFoodType

class Ulae(Animal, Identifiable, ISwimming, ISaltwater, IFoodType):
    
    def __init__(self):
        Animal.__init__(self, "Ulae")
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        IFoodType.__init__(self, "Fish")
        self.__food = ( "Squid", "Bait Fish")

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The ulae ate {food} for a meal')
        else:
            print(f'The ulae does not seem interested...')


    def __str__(self):
        return f'Ulae (Red Lizardfish) [{self.id.hex[:8]}]. Sound does not travel well under water.'