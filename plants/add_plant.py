import os
from .list_environments_for_plants import build_environment_menu
from plants import BlueJadeVine
from plants import MountainAppleTree
from plants import RainbowEucalyptusTree
from plants import SilverSword
from interfaces import RepresentsInt, raise_val_error

def add_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Blue Jade Vine")
    print("2. Mountain Apple Tree")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Silversword")


    choice = input("Choose your plant > ")
    if RepresentsInt(choice) == True:
        if int(choice) < 5:

            if choice == "1":
                bjv = BlueJadeVine()
                build_environment_menu(arboretum, bjv)

                
            if choice == "2":
                moap = MountainAppleTree()
                build_environment_menu(arboretum, moap)
            
            if choice == "3":
                ret = RainbowEucalyptusTree()
                build_environment_menu(arboretum, ret)
            
            if choice == "4":
                ss = SilverSword()
                build_environment_menu(arboretum, ss)
        else:
            if raise_val_error():
                return ""
    

