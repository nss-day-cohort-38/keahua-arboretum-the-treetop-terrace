from interfaces.habitat.aquatic import IAquatic

class IFreshwater(IAquatic):

    def __init__(self):
        IAquatic.__init__(self)
        self.cell_type1 = "hypertonic"
        self.isFreshWater = True