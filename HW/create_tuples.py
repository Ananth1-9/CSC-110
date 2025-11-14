def zip_lists(list_1, list_2, list_3):
    outputlst = []
    for i in range(len(list_1)):
        templist = []
        templist.append(list_1[i])
        templist.append(list_2[i])
        templist.append(list_3[i])
        outputlst.append(tuple(templist))
    return outputlst

