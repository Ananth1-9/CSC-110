def remove_records(dict):
    key = set(dict)
    for item in key:
        if item[0].lower == item[-1].lower:
            dict.pop(item)
    return dict


tempdict = {'anna': 1, 'Ananth': 2, 'jojo':3}

print(remove_records(tempdict))


def test_dictionary(dict1):
    key = set(dict1)
    for item in key:
        lst = []
        for i in range(len(dict1[item])):
            lst.append(item)
        dict1[item] = lst
    return dict1
print(test_dictionary(tempdict))

