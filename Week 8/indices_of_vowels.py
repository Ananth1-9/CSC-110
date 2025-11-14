def indices_of_vowels(strv):
    vow = 'aeiouAEIOU'
    lstvowi = []
    for i in range(len(strv)):
        if strv[i] in vow:
            lstvowi.append(i)
        
    return lstvowi

