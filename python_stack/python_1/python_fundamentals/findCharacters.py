def findCharacters(word_list, char):
    new_list = []
    letter = set('a')
    for word in word_list:
        if letter & set(word):
            new_list.append(word)
    print new_list

findCharacters(['hello', 'world', 'my', 'name', 'is', 'Anna'], 'o')