def count_vowels(s):
    i = 0
    count = 0
    while i < len(s):
        if s[i] in 'aeiouAEIOU':
            count += 1
        i += 1
    return count
