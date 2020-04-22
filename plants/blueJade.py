from .plant import Plant
from interfaces import Identifiable

class BlueJadeVine(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Spring/Summer")
        Identifiable.__init__(self)
        self.seeds = 0
        self.light = "Partial"
        self.resistance = "Medium"
        self.possible_locations = ["Grassland", "Swamp"]
    
    def __str__(self):
        return f'Blue Jade Vine [{self.id.hex[:8]}]'