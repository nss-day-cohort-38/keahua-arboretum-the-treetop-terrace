import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.feed_animal import biome_menu
from actions.report import build_facility_report
from plants import add_plant

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("|  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print ("6. Life tip of the day")
    print("7. Wanna see a cat?")
    print("8. Exit")
    print("Choose a KILLER option.")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)
        pass

    if choice == "3":
        biome_menu(keahua)
        pass

    if choice == "4":
        add_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        
    if choice == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("________                 __        .___      .__        __     ___.   .__                       .__     ")
        print("\______ \   ____   _____/  |_    __| _/______|__| ____ |  | __ \_ |__ |  |   ____ _____    ____ |  |__  ")
        print(" |    |  \ /  _ \ /    \   __\  / __ |\_  __ \  |/    \|  |/ /  | __ \|  | _/ __ \\__  \ _/ ___\|  |  \ ")
        print(" |    `   (  <_> )   |  \  |   / /_/ | |  | \/  |   |  \    <   | \_\ \  |_\  ___/ / __ \\  \___|   Y  \ ")
        print("/_______  /\____/|___|  /__|   \____ | |__|  |__|___|  /__|_ \  |___  /____/\___  >____  /\___  >___|  /")
        print("        \/            \/            \/               \/     \/      \/          \/     \/     \/     \/ ")

        input("\n\nPress any key to continue...")

    if choice == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("   |\---/|")
        print("   | ,_, |")
        print("    \_`_/-..----.")
        print(" ___/ `   ' ,""+ \  sk")
        print("(__...'   __\    |`.___.';")
        print("  (_,...'(_,.`__)/'.....+")

        input("\n\nPress any key to continue...")

    if choice != "8":
        main_menu()
    

main_menu()

