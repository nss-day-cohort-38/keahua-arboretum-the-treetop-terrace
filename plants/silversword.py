from .plant import Plant
from interfaces import Identifiable
from interfaces import ILight
from interfaces import IWater

class SilverSword(Plant, Identifiable, ILight, IWater):

    def __init__(self):
        Plant.__init__(self, "Silversword", "Spring/Summer")
        Identifiable.__init__(self)
        ILight.__init__(self, False, False, True, False)
        IWater.__init__(self, True, False, False, False)
        self.seeds = 22
        self.resistance = "High"
        self.possible_locations = ["Grassland"]
    
    def __str__(self):
        return f'Silversword [{self.id.hex[:8]}]'