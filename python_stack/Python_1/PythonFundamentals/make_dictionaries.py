#Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

#Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dictcopy(list1, list2):
    animal_names = zip(name, favorite_animal)
    animal_names_dict = dict(animal_names)
    return animal_names_dict

print make_dictcopy(name, favorite_animal)

#animal_names = zip(name, favorite_animal)
#animal_names_dict = dict(animal_names)
#print animal_names_dict