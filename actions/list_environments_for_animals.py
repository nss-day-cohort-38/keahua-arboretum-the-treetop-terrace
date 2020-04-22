import os
import sys

def list_environments_for_animals(arboretum, animal):
    if animal.species == "River Dolphin":
        locations = arboretum.rivers + arboretum.coastlines
        list_environments(locations, animal)

    elif animal.species == "Nene Goose":
        locations = arboretum.grasslands
        list_environments(locations, animal)

    elif animal.species == "Hawaiian Happy Face Spider":
        locations= arboretum.swamps
        list_environments(locations, animal)

    elif animal.species == "Gold Dust Day Gecko":
        locations = arboretum.forests
        list_environments(locations, animal)

    elif animal.species == "Kikakapu":
        locations = arboretum.swamps + arboretum.rivers
        list_environments(locations, animal)

    elif animal.species == "Opeapea":
        locations = arboretum.forests + arboretum.mountains
        list_environments(locations, animal)

    elif animal.species == "Pueo":
        locations = arboretum.grasslands + arboretum.forests
        list_environments(locations, animal)

    elif animal.species == "Ulae":
        locations = arboretum.coastlines
        list_environments(locations, animal)



def list_environments (locations, animal):
    counter = 1
    # os.system('cls' if os.name == 'nt' else 'clear')
    if len(locations) == 0:
        print("****   No biomes found please try again  ****")
        
        
    else:
        for location in locations:
            print(f"{counter}. {location} ({len(location.animals)} animals)")
            counter += 1
        choice = input("Choose your environment > ")
        num = int(choice)-1
        if len(locations[num].animals) == locations[num].animal_capacity:
            print("****   That biome is not large enough   ****")
            print("****     Please choose another one      ****")
            list_environments(locations, animal)
        else:
            locations[num].animals.append(animal)
    