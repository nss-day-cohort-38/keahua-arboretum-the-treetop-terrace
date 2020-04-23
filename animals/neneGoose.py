from animals import Animal
from interfaces import Identifiable, IFlying, IWalking

class NeneGoose(Animal, Identifiable, IFlying, IWalking):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Identifiable.__init__(self)
        IFlying.__init__(self)
        IWalking.__init__(self)
        self.__food = ("Grass", "Weeds", "Ohelo Berries" )

    @property
    def food(self):
        return self.__food

    def feed(self, food):
        if food == "Ohelo Berries":
            print('The goose loves ohelo berries!')
        elif food in self.__food:
            print(f'The goose ate {food} for a meal')
        else:
            print(f'The goose rejects the {food}')

    def __str__(self):
        return f'Nene Goose [{self.id.hex[:8]}]. HONK!!'