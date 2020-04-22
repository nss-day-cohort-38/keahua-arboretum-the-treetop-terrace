from animals import RiverDolphin
from animals import NeneGoose
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import HappyFaceSpider
from animals import GoldDustGecko
from .list_environments_for_animals import list_environments_for_animals

import os

def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Nene Goose")
    print("3. Kikakapu")
    print("4. Pueo")
    print("5. Ulae")
    print("6. Ope'ape'a")
    print("7. Happy-Face Spider")
    print("8. Gold Dust Day Gecko")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()
        list_environments_for_animals(arboretum, animal)

    if choice == "2":
        animal = NeneGoose()
        list_environments_for_animals(arboretum, animal)

    if choice == "3":
        animal = Kikakapu()
        list_environments_for_animals(arboretum, animal)

    if choice == "4":
        animal = Pueo()
        list_environments_for_animals(arboretum, animal)

    if choice == "5":
        animal = Ulae()
        list_environments_for_animals(arboretum, animal)

    if choice == "6":
        animal = Opeapea()
        list_environments_for_animals(arboretum, animal)

    if choice == "7":
        animal = HappyFaceSpider()
        list_environments_for_animals(arboretum, animal)

    if choice == "8":
        animal = GoldDustGecko()
        list_environments_for_animals(arboretum, animal)


    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)
    # arboretum.swamps[int(choice) - 2].animals.append(animal)



