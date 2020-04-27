from .environment import Environment
from interfaces import Identifiable, IContainsAnimals, IContainsPlants, IShade, IRain, ITerrestrial, getAmountOfPlantsAndAnimals


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
        return f'Forest ({getAmountOfPlantsAndAnimals(self)}) [{self.id.hex[:8]}]'

    def add_animal(self, animal):
        try:
            if "Insects" in animal.foodType :
                try: 
                    if animal.flight_speed > -1:
                        if animal.isNocturnal:
                            self.animals.append(animal)
                except:
                    if animal.move_speed > -1:
                        if "Spider" in animal.food:
                            self.animals.append(animal)

            if "Rodents" in animal.foodType and animal.flight_speed > -1:
                self.animals.append(animal)

        except AttributeError:
            print("This animal can't go in this habitat")
        
    def add_plant(self, plant):
        try:
            if plant.low_light and plant.med_water:
                self.plants.append(plant)
        except:
            print(f"{plant.species} can't go in tihs habitat")
    
    def test(self, item):
        try:
            if "Insects" in item.foodType :
                try: 
                    if item.flight_speed > -1:
                        if item.isNocturnal:
                            return True
                except:
                    if item.move_speed > -1:
                        if "Spider" in item.food:
                            return True

            if "Rodents" in item.foodType and item.flight_speed > -1:
                return True
            

        except AttributeError:
            return False
    
    def test_plant(self, item):
        try:
            if item.low_light and item.med_water:
                return True

        except AttributeError:
            return False

        