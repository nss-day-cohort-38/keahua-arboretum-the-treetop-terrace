from arboretum import Arboretum

def build_facility_report(Arboretum):
    for environments in Arboretum.master:
        for environment in environments:
            print(environment)
            print('''
                    ----- ANIMALS -----
            ''')
            for animal in environment.animals:
                print(f'        {animal}')
            print('''
                    ----- PLANTS ------
             ''')
            for plant in environment.plants:
                print(f'        {plant}')
            
    print('''
                ------  END REPORT  -------
        ''')

    input("\n\nPress any key to continue...")