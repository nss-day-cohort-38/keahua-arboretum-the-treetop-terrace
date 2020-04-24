class IWater:
    def __init__(self, low_level = False, med_level = False, high_level = False, all_level = False ):
        self.low_water = low_level
        self.med_water = med_level
        self.high_water = high_level
        self.all_water = all_level