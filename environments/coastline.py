from .environment import Environment
from interfaces import IAquatic, Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial, ISaltwater, getAmountOfPlantsAndAnimals

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


    def add_animal(self, animal):
        try:
            if "Fish" in animal.foodType and animal.isSaltwater:
                self.animals.append(animal)
        except AttributeError:
            print("This animal can't be added to this environment.")

    def add_plant(self, plant):
        try:
            if plant.high_water and plant.full_light:
                self.plants.append(plant)
        except:
            print(f"{plant.species} can't go in this habitat")

    def test(self, item):
        try:
            if "Fish" in item.foodType and item.isSaltwater:
                return True
            
        except AttributeError:
            return False
    def test_plant(self, item):
        try:
            if item.high_water and item.full_light:
                return True
        except AttributeError:
            return False
        
    def __str__(self):
        
        return f'Coastline ({getAmountOfPlantsAndAnimals(self)})[{self.id.hex[:8]}]'
        