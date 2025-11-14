def count_vowels(string):
    capvow = 'AEIOUaeiou'
    vowcount = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0
                ,'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in range(len(string)):
        if string[i] in capvow:
            vowcount[string[i]] = vowcount[string[i]]+1
        
    return vowcount
    
print(count_vowels('banana'))

