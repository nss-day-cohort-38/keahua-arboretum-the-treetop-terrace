import sys
sys.path.append('../')

from .environment import Environment
from interfaces import IAquatic, Identifiable, IContainsAnimals, IContainsPlants, IFreshwater, IStagnant, ITerrestrial, getAmountOfPlantsAndAnimals

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
            self.animals.append(item)
    
    def add_animal(self, animal):
        try:

            if "Fish" in animal.foodType and animal.isFreshWater and animal.stagnant \
                or "Insects" in animal.foodType and animal.isFreshWater:
                self.animals.append(animal)
        except AttributeError:
            print("This animal can't be added to this environment.")

    def add_plant(self, plant):
        try:
            if plant.high_water and plant.low_light or plant.all_light and plant.all_water:
                self.plants.append(plant)
        except:
            print(f"{plant.species} can't go in this habitat")
    
    def __str__(self):
        return f'Swamp [{self.id.hex[:8]}]'

    def test(self, item):
        try:
            if "Fish" in item.foodType and item.isFreshWater and item.stagnant \
                or "Insects" in item.foodType and item.isFreshWater:
                return True
            

        except AttributeError:
            return False
    
    def test_plant(self, item):
        try:
            if item.high_water and item.low_light or item.all_light and item.all_water:
                return True
                
        except AttributeError:
            return False