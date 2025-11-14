def remove_vowel_list(lst):
    vow = 'aeiouAEIOU'
    i = 0
    while i < len(lst):
        if lst[i] in vow:
            lst.pop(i)
        i += 1

    return lst

def remove_vowels_string(stringv):
    vow = 'aeiouAEIOU'
    i = 0
    newstr = ''
    while i < len(stringv):
        if stringv[i] not in vow:
            newstr += stringv[i]
        i += 1
    return newstr
