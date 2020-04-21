from arboretum import Arboretum

def build_facility_report(Arboretum):
    for river in Arboretum.rivers:
        print(f'River [{river.id}]')

    input("\n\nPress any key to continue...")