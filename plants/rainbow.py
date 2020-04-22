from .plant import Plant
from interfaces import Identifiable

class RainbowEucalyptusTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Spring/Summer")
        Identifiable.__init__(self)
        self.seeds = 8
        self.light = "Shade"
        self.resistance = "Low"
        self.possible_locations = ["Forest"]
    
    def __str__(self):
        return f'Rainbow Eucalyptus Tree [{self.id.hex[:8]}]'