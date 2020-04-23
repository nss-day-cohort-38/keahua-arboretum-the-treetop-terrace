from .plant import Plant
from interfaces import Identifiable
from interfaces import ILight
from interfaces import IWater

class MountainAppleTree(Plant, Identifiable, ILight, IWater):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Spring/Summer")
        Identifiable.__init__(self)
        ILight.__init__(self, False, False, True, False)
        IWater.__init__(self, False, True, False, False)
        self.seeds = 17
        self.resistance = "High"
        self.possible_locations = ["Mountain"]
    
    def __str__(self):
        return f'Mountain Apple Tree [{self.id.hex[:8]}]'