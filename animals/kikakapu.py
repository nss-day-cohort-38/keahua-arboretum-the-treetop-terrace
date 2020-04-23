from animals import Animal
from interfaces import IFreshwater, Identifiable, ISwimming

class Kikakapu(Animal, IFreshwater, Identifiable, ISwimming):

    def __init__(self):
        Animal.__init__(self, "Kikakapu")
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        ISwimming.__init__(self)
        self.__food = ( "Blue Coral" , "Green Coral" )

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The Kikakapu ate {food} for a meal')
        else:
            print(f'The Kikakapu does not seem interested...')


    def __str__(self):
        return f'Kikakapu (Ornate Butterflyfish) [{self.id.hex[:8]}]. Sound does not travel well under water.'


