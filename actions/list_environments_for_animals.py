import os
import sys


def build_environment_menu(arboretum, animal):
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 1
    new_list = list()
    new_new_list = list()

    for biomes in arboretum.master:
            for biome in biomes:
                new_list.append(biome)
                
    if len(new_list) > 0:
        for biome in new_list:
            if biome.animal_capacity > len(biome.animals):
                
                if biome.test(animal):
                    new_new_list.append(biome)

            else:
                pass
              

        for biome in new_new_list:
            print(f"{counter}. {biome} ({len(biome.animals)}/{biome.animal_capacity} animals)")
            counter += 1

        if len(new_new_list) == 0:
            print(f"Annex a new habitat. No more space")
            input("\n\nPress any key to continue...")

        else:
            choice = input("In which biome would you like to add an animal?\n ")
            new_new_list[int(choice)-1].add_animal(animal)


    else:
        print("Please annex a habitat before releasing animals. \n")
        input("\n\nPress any key to continue...")



# def list_environments_for_animals(arboretum, animal):
#     locations = set()

#     if "Fish" in animal.foodType \
#         and animal.isSaltwater:
#         locations.add(arboretum.coastlines)
    
#     if "Fish" in animal.foodType and animal.isFreshWater and animal.stagnant \
#         or "Insects" in animal.foodType and animal.isFreshWater:
#         locations.add(arboretum.swamps)

#     # if "Insects" in animal.foodType and animal.isFreshWater:
#     #     locations.add(arboretum.swamps)
    
#     if "Fish" in animal.foodType and animal.isFreshWater:
#         locations.add(arboretum.rivers)
    
#     if "Rodents" in animal.foodType and animal.flight_speed:
#         locations.add(arboretum.forests)

#     if "Insects" in animal.foodType and animal.move_speed:
#         locations.add(arboretum.forests)

#     if "Insects" in animal.foodType and animal.flight_speed \
#         and animal.isNocturnal:
#         locations.add(arboretum.forests)

#     if "Rodents" in animal.foodType and animal.flight_speed \
#         and animal.maxFlightSpeed > 150:
#         locations.add(arboretum.grasslands)

#     if "Vegetation" in animal.foodType and animal.flight_speed \
#         and animal.isNocturnal == False:
#         locations.add(arboretum.grasslands)
    
#     if "Vegetation" in animal.foodType and animal.flight_speed and animal.isNocturnal:
#         locations.add(arboretum.mountains)

#     total_Locations = []

#     for location_list in locations:
#         for location in location_list:
#             total_Locations.append(location)
  
#     list_environments(total_Locations, animal)
# def list_environments (locations, animal):
#     counter = 1
#     # os.system('cls' if os.name == 'nt' else 'clear')
#     if len(locations) == 0:
#         print("****   No biomes found please try again  ****")
        
        
#     else:
#         for location in locations:
#             print(f"{counter}. {location} ({len(location.animals)} animals)")
#             counter += 1
#         choice = input("Choose your environment > ")
#         num = int(choice)-1
#         if len(locations[num].animals) == locations[num].animal_capacity:
#             print("****   That biome is not large enough   ****")
#             print("****     Please choose another one      ****")
#             list_environments(locations, animal)
#         else:
#             locations[num].animals.append(animal)
    