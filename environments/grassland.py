import sys
sys.path.append('../')

from .environment import Environment
from interfaces import Identifiable, IContainsAnimals, IContainsPlants, ITerrestrial, IRain, IShade, getAmountOfPlantsAndAnimals

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
    def add_animal(self, animal):
        try:
            if "Rodents" in animal.foodType and animal.flight_speed > -1 \
                and animal.maxFlightSpeed > 150:
                self.animals.append(animal)

            if "Vegetation" in animal.foodType and animal.flight_speed > -1 \
                and animal.isNocturnal == False:
                self.animals.append(animal)
        except AttributeError:
            print("This animal can't be added here.")
    
    def add_plant(self, plant):
        try:
            if plant.full_light and plant.low_water or plant.all_light and plant.all_water:
                self.plants.append(plant)
        except:
            print(f"{plant.species} can't go in this habitat")
    
    def test(self, item):
        try:
            if "Rodents" in item.foodType and item.flight_speed > -1 \
                and item.maxFlightSpeed > 150:
                    return True

            if "Vegetation" in item.foodType and item.flight_speed > -1 \
                and item.isNocturnal == False:
                    return True
            
        except AttributeError:
            return False

    def test_plant(self, item):
        try:
            if item.full_light and item.low_water or item.all_light and item.all_water:
                return True
                
        except AttributeError:
            return False

    def __str__(self):
        if len(self.animals + self.plants) == 0:
            return f'Grassland [{self.id.hex[:8]}]'
        else :
            return f'Grassland ({getAmountOfPlantsAndAnimals(self)})[{self.id.hex[:8]}]'