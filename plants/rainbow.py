from .plant import Plant
from interfaces import Identifiable
from interfaces import ILight
from interfaces import IWater

class RainbowEucalyptusTree(Plant, Identifiable, ILight, IWater):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Spring/Summer")
        Identifiable.__init__(self)
        ILight.__init__(self, True, False, False, False)
        IWater.__init__(self, False, True, False, False)
        self.seeds = 8
        self.resistance = "Low"
        self.possible_locations = ["Forest"]
    
    def __str__(self):
        return f'Rainbow Eucalyptus Tree [{self.id.hex[:8]}]'