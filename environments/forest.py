from .environment import Environment
from interfaces import Identifiable, IContainsAnimals, IContainsPlants, IShade, IRain, ITerrestrial


class Forest(Environment, Identifiable, IContainsPlants, IContainsAnimals, IShade, IRain, ITerrestrial):

    def __init__(self):
        Environment.__init__(self)
        Identifiable.__init__(self)
        IContainsPlants.__init__(self)
        IContainsAnimals.__init__(self)
        IShade.__init__(self)
        IRain.__init__(self)
        ITerrestrial.__init__(self)

        self.inhabitants = []
        self.plant_capacity = 32
        self.animal_capacity = 20

    def __str__(self):
        return f'Forest [{self.id.hex[:8]}]'