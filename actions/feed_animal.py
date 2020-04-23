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

    if choice == "1":
        gecko = GoldDustGecko()
        feed_menu(gecko)

    if choice == "2":
        dolphin = RiverDolphin()
        feed_menu(dolphin)

    if choice == "3":
        nene = NeneGoose()
        feed_menu(nene)

    if choice == "4":
        kikakapu = Kikakapu()
        feed_menu(kikakapu)

    if choice == "5":
        pueo = Pueo()
        feed_menu(pueo)

    if choice == "6":
        ulae = Ulae()
        feed_menu(ulae)

    if choice == "7":
        opeapea = Opeapea()
        feed_menu(opeapea)

    if choice == "8":
        spider = HappyFaceSpider()
        feed_menu(spider)

def feed_menu(animal):
    os.system('cls' if os.name == 'nt' else 'clear')

    counter = 1
    for food in animal.food:
        print(f"{counter}. {food}")
        counter += 1

    choice = input(f"What is on the menu for the {animal.species} today?")

    number = int(choice) -1
    
    animal.feed(animal.food[number])

    input("\n\nPress any key to continue...")
