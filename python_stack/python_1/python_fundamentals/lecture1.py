kamini = {
    "name": "Tom",
    "gender": "male",
    "city": "Seattle"
}

for key in kamini:
    print key, kamini[key]

def printDictionary(dictionaryToPrint):
    for key in dictionaryToPrint:
        print key, dictionaryToPrint[key]

printDictionary(kamini)