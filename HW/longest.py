def longest_string(lst):
    longeststring = ''
    for subdict in lst:
        temp = subdict.values()
        for i in temp:
            if len(i) > len(longeststring):
                longeststring = i
    if longeststring == '':
        return None
    return longeststring