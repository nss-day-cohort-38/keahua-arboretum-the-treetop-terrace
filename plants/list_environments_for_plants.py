import os
import sys


def build_environment_menu(arboretum, plant):
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 1
    new_list = list()
    new_new_list = list()

    for biomes in arboretum.master:
            for biome in biomes:
                new_list.append(biome)

    if len(new_list) > 0:

        for biome in new_list:
            if biome.test_plant(plant):
                new_new_list.append(biome)

        for biome in new_new_list:
            print(f"{counter}. {biome}")
            counter += 1
        

        choice = input("In which biome would you like to add an plant?\n ")
        print(new_new_list)
        new_new_list[int(choice)-1].add_plant(plant)
    else:
        print("Please annex a habitat before planting \n")
        input("\n\nPress any key to continue...")

# def list_environments_for_plants(arboretum, plant):
   

#     if plant.low_light and plant.med_water:
#         locations = arboretum.forests
#         list_environments(locations, plant)

#     elif plant.full_light and plant.med_water:
#         locations= arboretum.mountains
#         list_environments(locations, plant)

#     elif plant.full_light and plant.low_water:
#         locations = arboretum.grasslands
#         list_environments(locations, plant)

#     elif plant.high_water and plant.partial_light:
#         locations = arboretum.rivers
#         list_environments(locations, plant)

#     elif plant.high_water and plant.low_light:
#         locations = arboretum.swamps
#         list_environments(locations, plant)

#     elif plant.high_water and plant.full_light:
#         locations = arboretum.coastlines
#         list_environments(locations, plant)
#     elif plant.all_light and plant.all_water:
#         locations = arboretum.grasslands + arboretum.swamps
#         list_environments(locations, plant)



# def list_environments (locations, plant):
#     counter = 1
#     # os.system('cls' if os.name == 'nt' else 'clear')
#     if len(locations) == 0:
#         print("****   No biomes found please try again  ****")
        
        
#     else:
#         for location in locations:
#             print(f"{counter}. {location} ({len(location.plants)} plants)")
#             counter += 1
#         choice = input("Choose your environment > ")
        
#         if RepresentsInt(choice) == True:
#             num = int(choice)-1
#             if len(locations[num].plants) == locations[num].plant_capacity:
#                 print("****   That biome is not large enough   ****")
#                 print("****     Please choose another one      ****")
#                 list_environments(locations, plant)
#             else:
#                 locations[num].plants.append(plant)
#                 print(f"The {plant.species} was added to {locations[num]}")
#                 input("\n\nPress any key to continue...")
    



def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        print ("Please enter a number...")
        input("\n\nPress any key to continue...")


        # print(type(int(choice)))
        # num = int(choice)-1
        # if len(locations[num].plants) == locations[num].plant_capacity:
        #     print("****   That biome is not large enough   ****")
        #     print("****     Please choose another one      ****")
        #     list_environments(locations, plant)
        # else:
        #     locations[num].plants.append(plant)
        #     print(f"The {plant.species} was added to {locations[num]}")
        #     input("\n\nPress any key to continue...")

