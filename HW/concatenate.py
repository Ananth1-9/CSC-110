def concatenate(words):
    lstconcat = ''
    i = 0
    while i < len(words):
        lstconcat += words[i]
        if i != len(words) - 1:
            lstconcat += ' '    
        i += 1
    return lstconcat 

