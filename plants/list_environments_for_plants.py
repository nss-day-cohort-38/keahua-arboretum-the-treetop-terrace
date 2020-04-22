import os
import sys

def list_environments_for_plants(arboretum, plant):
    if plant.species == "Blue Jade Vine":
        locations = arboretum.grasslands + arboretum.swamps
        list_environments(locations, plant)

    elif plant.species == "Rainbow Eucalyptus Tree":
        locations = arboretum.forests
        list_environments(locations, plant)

    elif plant.species == "Mountain Apple Tree":
        locations= arboretum.mountains
        list_environments(locations, plant)

    elif plant.species == "Silversword":
        locations = arboretum.grasslands
        list_environments(locations, plant)



def list_environments (locations, plant):
    counter = 1
    # os.system('cls' if os.name == 'nt' else 'clear')
    if len(locations) == 0:
        print("****   No biomes found please try again  ****")
        
    else:
        for location in locations:
            print(f"{counter}. {location} ({len(location.plants)} plants)")
            counter += 1
        choice = input("Choose your environment > ")
        num = int(choice)-1
        if len(locations[num].plants) == locations[num].plant_capacity:
            print("****   That biome is not large enough   ****")
            print("****     Please choose another one      ****")
            list_environments(locations, plant)
        else:
            locations[num].plants.append(plant)
    