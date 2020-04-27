def count_inhabitants(environment):
    list_of_inhabitants = environment.animals + environment.plants
    list_of_species = list()

    for inhabitant in list_of_inhabitants:
        list_of_species.append(inhabitant.species)

    dict_of_inhabitants = {element : list_of_species.count(element) for element in list_of_species}

    return str(dict_of_inhabitants)