def invert_dictionary(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if value in new_dictionary:
            new_dictionary[value].append(key)
        else:
            new_dictionary[value] = [key]
    return new_dictionary

    