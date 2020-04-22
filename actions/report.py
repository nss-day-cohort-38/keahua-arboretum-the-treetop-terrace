from arboretum import Arboretum

def build_facility_report(Arboretum):
    for environments in Arboretum.master:
        for environment in environments:
            print(environment)
            print('''
            ----- ANIMALS -----
            ''')
            for animal in environment.animals:
                print(animal)
            print('''
            ----- PLANTS ------
             ''')
            for plant in environment.plants:
                print(plant)

    input("\n\nPress any key to continue...")