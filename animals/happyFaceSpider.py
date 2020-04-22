from animals import Animal
from interfaces import IWalking, Identifiable

class HappyFaceSpider(Animal, IWalking, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy Face Spider")
        IWalking.__init__(self)
        Identifiable.__init__(self)
        self.__food = { "Mosquito", "House Fly", "Beetle"}

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food in self.__food:
            print(f'The spider ate {food} for a meal')
        else:
            print(f'The spider rejects the {food}')

    def __str__(self):
        return f'Hawaiian Happy Faced Spider {self.id}. Silence... '