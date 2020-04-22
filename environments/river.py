from interfaces import Identifiable, IContainsAnimals, IContainsPlants, IFreshwater
from animals import RiverDolphin

class River(IContainsAnimals, IContainsPlants, Identifiable, IFreshwater):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        IFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.inhabitants = []
        self.plant_capacity = 6
        self.animal_capacity = 12
      

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")

    def __str__(self):
        return f'River [{self.id.hex[:8]}]'
