class ILight:
    def __init__(self, low_level = False, med_level = False, high_level = False, all_level = False ):
        self.low_light = low_level
        self.partial_light = med_level
        self.full_light = high_level
        self.all_light = all_level
