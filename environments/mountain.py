from .environment import Environment
from interfaces import Identifiable, IContainsAnimals, IContainsPlants, IShade, IRain, ITerrestrial, IElevation


class Mountain(Environment, Identifiable, IContainsPlants, IContainsAnimals, ITerrestrial, IElevation):

    def __init__(self):
        Environment.__init__(self)
        Identifiable.__init__(self)
        IContainsPlants.__init__(self)
        IContainsAnimals.__init__(self)
        ITerrestrial.__init__(self)
        IElevation.__init__(self)

        self.inhabitants = []
        self.plant_capacity = 4
        self.animal_capacity = 6

    def __str__(self):
        return f'Mountain [{self.id}]'