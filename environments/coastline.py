from .environment import Environment
from interfaces import IAquatic, Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial, ISaltwater

# from animals.


class Coastline(Environment, Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial, ISaltwater):

    def __init__(self):
        Environment.__init__(self)
        Identifiable.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        ITerrestrial.__init__(self)
        ISaltwater.__init__(self)
        self.inhabitants = []
        self.plant_capacity = 3
        self.animal_capacity = 15

    def __str__(self):
        return f'Coastline [{self.id}]'
        