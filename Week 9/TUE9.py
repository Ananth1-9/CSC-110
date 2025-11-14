def count_chars(string):
    chardic = {}
    for i in range(len(string)):
        if string[i] not in chardic:
            chardic[string[i]] = 1
        else:
            chardic[string[i]] += 1