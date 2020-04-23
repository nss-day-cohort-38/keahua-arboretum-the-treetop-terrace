from animals import Animal
from interfaces import Identifiable, IWalking, IBiome

class GoldDustGecko(Animal, Identifiable, IWalking, IBiome):

    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)
        IWalking.__init__(self)
        IBiome.__init__(self, False, False, True, False, False, False)
        self.__food = ( "Mosquito", "House Fly", "Spider" )

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The gecko ate {food} for a meal')
        else:
            print(f'The gecko rejects the {food}')

    def __str__(self):
        return f'Gold Dust Day Gecko [{self.id.hex[:8]}]. Silence...'