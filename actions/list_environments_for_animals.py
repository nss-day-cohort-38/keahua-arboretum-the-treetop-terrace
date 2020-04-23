import os
import sys

def list_environments_for_animals(arboretum, animal):
    
    if animal.canMountain and animal.canForest:
        return list_environments(arboretum.forests + arboretum.mountains, animal)

    elif animal.canMountain and animal.canGrassland:
        return list_environments(arboretum.grasslands + arboretum.mountains, animal)

    elif animal.canMountain and animal.canRiver:
        return list_environments(arboretum.rivers + arboretum.mountains, animal)

    elif animal.canMountain and animal.canSwamp:
        return list_environments(arboretum.swamps + arboretum.mountains, animal)

    elif animal.canMountain and animal.canCoastline:
        return list_environments(arboretum.coastlines + arboretum.mountains, animal)

    elif animal.canGrassland and animal.canForest:
        return list_environments(arboretum.forests + arboretum.grasslands, animal)

    elif animal.canGrassland and animal.canRiver:
        return list_environments(arboretum.rivers + arboretum.grasslands, animal)

    elif animal.canGrassland and animal.canSwamp:
        return list_environments(arboretum.swamps + arboretum.grasslands, animal)

    elif animal.canGrassland and animal.canCoastline:
        return list_environments(arboretum.coastlines + arboretum.grasslands, animal)

    elif animal.canForest and animal.canRiver:
        return list_environments(arboretum.rivers + arboretum.forests, animal)

    elif animal.canForest and animal.canSwamp:
        return list_environments(arboretum.swamps + arboretum.forests, animal)

    elif animal.canForest and animal.canCoastline:
        return list_environments(arboretum.coastlines + arboretum.forests, animal)

    elif animal.canRiver and animal.canSwamp:
        return list_environments(arboretum.swamps + arboretum.rivers, animal)

    elif animal.canRiver and animal.canCoastline:
        return list_environments(arboretum.coastlines + arboretum.rivers, animal)

    elif animal.canCoastline and animal.canSwamp:
        return list_environments(arboretum.swamps + arboretum.coastlines, animal)

    elif animal.canGrassland:
        return list_environments(arboretum.grasslands, animal)

    elif animal.canMountain:
        return list_environments(arboretum.mountains, animal)

    elif animal.canForest:
        return list_environments(arboretum.forests, animal)

    elif animal.canRiver:
        return list_environments(arboretum.rivers, animal)

    elif animal.canSwamp:
        return list_environments(arboretum.swamps, animal)

    elif animal.canCoastline:
        return list_environments(arboretum.coastlines, animal)


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
    