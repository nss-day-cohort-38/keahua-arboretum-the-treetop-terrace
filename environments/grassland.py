import sys
sys.path.append('../')

from .environment import Environment
from interfaces import Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial, IRain, IShade

# from animals.


class Grassland(Environment, Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial, IRain, IShade):

    def __init__(self):
        Environment.__init__(self)
        Identifiable.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        ITerrestrial.__init__(self)
        IRain.__init__(self)
        IShade.__init__(self)
        self.inhabitants = []
        self.plant_capacity = 15
        self.animal_capacity = 22
        self.rain = False
        self.shade = False
        

    def animal_count(self):
        return f"This place has {len(self.inhabitants)} of animals in it"

    # def addInhabitant(self, item):
    #     if not isinstance(item, IStagnant):
    #         raise TypeError(f"{item} is not of type IStagnant")
    #     else:
    #         self.inhabitants.append(item)

    def __str__(self):
        return f'Grassland [{self.id}]'
