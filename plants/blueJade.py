from .plant import Plant
from interfaces import Identifiable
from interfaces import ILight
from interfaces import IWater

class BlueJadeVine(Plant, Identifiable, ILight, IWater):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "Spring/Summer")
        Identifiable.__init__(self)
        ILight.__init__(self, False, False, False, True)
        IWater.__init__(self, False, False, False, True)
        self.seeds = 0
        self.resistance = "Medium"
        self.possible_locations = ["Grassland", "Swamp"]
    
    def __str__(self):
        return f'Blue Jade Vine [{self.id.hex[:8]}]'