import os
import sys

def list_enviroments_for_plants(arboretum, plant):
    os.system('cls' if os.name == 'nt' else 'clear')
    if plant.species == "Blue Jade Vine":
        print(plant)
        # sys.exit()
        locations = arboretum.grasslands + arboretum.swamps
        list_enviroments(locations, plant)

    elif plant.species == "Rainbow Eucalyptus Tree":
        print(plant)
        # sys.exit()
        locations = arboretum.forests
        list_enviroments(locations, plant)

    elif plant.species == "Mountain Apple Tree":
        print(plant)
        # sys.exit()
        locations= arboretum.mountains
        list_enviroments(locations, plant)

    elif plant.species == "Silversword":
        print(plant)
        # sys.exit()
        locations = arboretum.grasslands
        list_enviroments(locations, plant)



def list_enviroments (locations, plant):
    counter = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(locations) == 0:
        print("****   No biomes found please try again  ****")
        # sys.exit()

    for location in locations:
        print(f"{counter}. {location} ({len(location.plants)} plants)")
        counter += 1
    choice = input("Choose your enviroment > ")
    num = choice-1
    if len(location[num].plants) == location[num].plant_capactiy:
        print("****   That biome is not large enough   ****")
        print("****     Please choose another one      ****")
        list_enviroments(locations, plant)
    else:
        location[num].plants.append(plant)
    