from .plant import Plant
from interfaces import Identifiable

class SilverSword(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Silversword", "Spring/Summer")
        Identifiable.__init__(self)
        self.seeds = 22
        self.light = "Full"
        self.resistance = "High"
        self.possible_locations = ["Grassland"]
    
    def __str__(self):
        return f'Silversword [{self.id}]'