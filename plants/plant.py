class Plant:

    def __init__(self, species, season):
      self.species = species
      self.peak_season = season
    
    def add_plant(self, habitat):
      habitat.plants.append(self)
