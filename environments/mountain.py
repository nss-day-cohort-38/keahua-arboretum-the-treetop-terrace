from .environment import Environment
from interfaces import Identifiable, IContainsAnimals, IContainsPlants, IShade, IRain, ITerrestrial, IElevation, getAmountOfPlantsAndAnimals


class Mountain(Environment, Identifiable, IContainsPlants, IContainsAnimals, ITerrestrial, IElevation):

    def __init__(self):
        Environment.__init__(self)
        Identifiable.__init__(self)
        IContainsPlants.__init__(self)
        IContainsAnimals.__init__(self)
        ITerrestrial.__init__(self)
        IElevation.__init__(self)
        self.name = "Mountain"
        self.inhabitants = []
        self.plant_capacity = 4
        self.animal_capacity = 6

    def __str__(self):
        if len(self.animals + self.plants) == 0:
            return f'Mountain [{self.id.hex[:8]}]'
        else :
            return f'Mountain ({getAmountOfPlantsAndAnimals(self)})[{self.id.hex[:8]}]'

    def add_animal(self, animal):
        try:
            if "Vegetation" in animal.foodType and animal.flight_speed > -1 and animal.isNocturnal:
                self.animals.append(animal)
        except AttributeError:
            print("This animal can't be added to this environment")

    def add_plant(self, plant):
        try:
            if plant.full_light and plant.med_water:
                self.plants.append(plant)
        except:
            print(f"{plant.species} can't go in this habitat")
    
    def test (self, item):
        try:
            if "Vegetation" in item.foodType and item.flight_speed > -1 and item.isNocturnal:
                return True
            

        except AttributeError:
            return False
        
    def test_plant(self, item):
        try:
            if item.full_light and item.med_water:
                return True
                
        except AttributeError:
            return False