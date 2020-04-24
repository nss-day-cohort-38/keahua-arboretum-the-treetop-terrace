
def getDuplicatesWithCount(listOfElems):
    ''' Get frequency count of duplicate elements in the given list '''
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    # Filter key-value pairs in dictionary
    # dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    # Returns a dict of duplicate elements and thier frequency count
    return dictOfElems


def getAmountOfPlantsAndAnimals(biome):
        aNpList = biome.animals + biome.plants
        nameList = []
        for item in aNpList:
            nameList.append(item.species)
        if len(nameList) == 0:
            return ""
        else:
            freqDict = getDuplicatesWithCount(nameList)
            aNpString = ""
            counter = 1
            dictLen = len(freqDict.keys())
            for key,value in freqDict.items():
                if counter == dictLen:
                    aNpString += f'{key} {value}'
                    counter +=1
                else:
                    aNpString += f'{key} {value},'
                    counter +=1
            return aNpString