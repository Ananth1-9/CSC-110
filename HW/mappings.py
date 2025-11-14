def all_mappings(dict):
    resultlst = []
    for key, value_list in dict.items():
        for number in value_list:
            resultlst.append((key,number))

    return resultlst