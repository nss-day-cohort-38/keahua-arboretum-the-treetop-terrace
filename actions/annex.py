import os
from environments import River
# from index import build_menu



def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
<<<<<<< HEAD
        
=======
        print('river added')
        # build_menu()
>>>>>>> 2f7d2fabf80462446bfe2f45679a11bf80b5c0c4
    if choice == "2":
        pass