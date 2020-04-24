from interfaces.habitat.aquatic import IAquatic

class ISaltwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type2 = "hypotonic"
        self.isSaltwater = True
