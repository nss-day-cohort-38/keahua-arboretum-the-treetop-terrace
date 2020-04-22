from .plant import Plant
from interfaces import Identifiable

class MountainAppleTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Spring/Summer")
        Identifiable.__init__(self)
        self.seeds = 17
        self.light = "Partial"
        self.resistance = "High"
        self.possible_locations = ["Mountain"]
    
    def __str__(self):
        return f'Mountain Apple Tree [{self.id}]'