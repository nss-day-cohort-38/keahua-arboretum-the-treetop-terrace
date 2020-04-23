class ILight:
    def __init__(self, low_level, med_level, high_level, all_level ):
        self.low_light = low_level
        self.partial_light = med_level
        self.full_light = high_level
        self.all_light = all_level
