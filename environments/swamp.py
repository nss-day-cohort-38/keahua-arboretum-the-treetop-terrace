import sys
sys.path.append('../')

from .environment import Environment
from interfaces import IAquatic, Identifiable, IContainsAnimals, IContainsPlants, IFreshwater, IStagnant, ITerrestrial

# from animals.


class Swamp(Environment, IStagnant, IAquatic, Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial):

    def __init__(self):
        Environment.__init__(self)
        IStagnant.__init__(self)
        IAquatic.__init__(self)
        Identifiable.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        ITerrestrial.__init__(self)
        self.inhabitants = []
        self.plant_capacity = 12
        self.animal_capacity = 8
        

    def animal_count(self):
        return f"This place has {len(self.inhabitants)} of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        else:
            self.inhabitants.append(item)

    def __str__(self):
        return f'Swamp [{self.id}]'
