from animals import RiverDolphin, GoldDustGecko, NeneGoose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider
import os 

def biome_menu(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 1
    new_list = list()
    for biomes in arboretum.master:
            for biome in biomes:
                new_list.append(biome)
    if len(new_list) > 0:
        
        for biome in new_list:
            print(f"{counter}. {biome}")
            counter += 1
        

        choice = input("In which biome would you like to feed the animals?\n ")
    
        animal_list(new_list[int(choice)-1])
    else:
        print("Please annex a habitat and release animals before feeding \n")
        input("\n\nPress any key to continue...")

def animal_list(biome):
    os.system('cls' if os.name == 'nt' else 'clear')
    counter = 1
    if len(biome.animals) > 0:
        for animal in biome.animals:
            print(f"{counter}. {animal}")
            counter += 1

        choice = input("Please select an animal to feed. \n")
        feed_menu(biome.animals[int(choice)-1])
    else:
        print("Please release animals to habitat before feeding\n")
        input("\n\nPress any key to continue...")


def feed_menu(animal):
    os.system('cls' if os.name == 'nt' else 'clear')

    counter = 1
    for food in animal.food:
        print(f"{counter}. {food}")
        counter += 1

    choice = input(f"What is on the menu for the {animal.species} today? \n")

    number = int(choice) -1
    
    animal.feed(animal.food[number])

    input("\n\nPress any key to continue...")
