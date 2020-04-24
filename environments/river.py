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
            if "Fish" in animal.foodType and animal.isFreshWater:
                self.animals.append(animal)

        except AttributeError:
            print("Cannot add non-aquatic, or saltwater animals to a river")
    
        

    def add_plant(self, plant):
        try:
            if plant.high_water and plant.partial_light:
                self.plants.append(plant)
        except:
            print(f"{plant.species} can't go in this habitat")

    def __str__(self):
        return f'River [{self.id.hex[:8]}]'

    def test (self, item):
        try:
            if "Fish" in item.foodType and item.isFreshWater:
                return True
            

        except AttributeError:
            return False
    
    def test_plant(self, item):
        try:
            if item.high_water and item.partial_light:
                return True
                
        except AttributeError:
            return False
