import os
from .list_environments_for_plants import list_environments_for_plants
from plants import BlueJadeVine
from plants import MountainAppleTree
from plants import RainbowEucalyptusTree
from plants import SilverSword

def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Silversword")

    choice = input("Choose your plant > ")

    if choice == "1":
        bjv = BlueJadeVine()
        list_environments_for_plants(arboretum, bjv)

        
    if choice == "2":
        moap = MountainAppleTree()
        list_environments_for_plants(arboretum, moap)
    
    if choice == "3":
        ret = RainbowEucalyptusTree()
        list_environments_for_plants(arboretum, ret)
    
    if choice == "4":
        ss = SilverSword()
        list_environments_for_plants(arboretum, ss)

