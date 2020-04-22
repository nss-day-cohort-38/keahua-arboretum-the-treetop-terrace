# import os
# from environments import River
# # from index import build_menu

# def annex_habitat(arboretum):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("1. River")
#     print("2. Swamp")
#     print("3. Coastline")
#     print("4. Grassland")

#     choice = input("Choose your habitat > ")

#     if choice == "1":
#         river = River()
#         arboretum.rivers.append(river)
#         print('river added')
#         # build_menu()
#     if choice == "2":
#         pass

import os
from environments import River, Swamp, Coastline, Grassland

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
    if choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    if choice == "3":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)