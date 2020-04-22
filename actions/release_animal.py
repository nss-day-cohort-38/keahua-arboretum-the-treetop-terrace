from animals import RiverDolphin
from animals import NeneGoose
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import HappyFaceSpider

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

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        animal = NeneGoose()

    if choice == "3":
        animal = Kikakapu()

    if choice == "4":
        animal = Pueo()

    if choice == "5":
        animal = Ulae()

    if choice == "6":
        animal = Opeapea()

    if choice == "7":
        animal = HappyFaceSpider()


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River [{river.id.hex[:8]}]')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 2}. Swamp {swamp.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)
    # arboretum.swamps[int(choice) - 2].animals.append(animal)


