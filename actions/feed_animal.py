from animals import RiverDolphin, GoldDustGecko, NeneGoose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider
import os 

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to feed >")

    if choice == 1:
        print("")

    if choice == 2:
        food_dolphin()

    if choice == 3:
        print("")

    if choice == 4:
        print("")

    if choice == 5:
        print("")

    if choice == 6:
        print("")

    if choice == 7:
        print("")

    if choice == 8:
        print("")

def food_dolphin(arboretum):
    print("1. Trout")
    print("2. Mackarel")
    print("3. Salmon")
    print("4. Sardine")

    choice = input("What is on the menu for the River Dolphin today?")

    if choice == 1:
        RiverDolphin.feed("Trout")