def reverse_string(s):
    revstri = ''
    i = 0
    while i < len(s):
        revstri = revstri + s[len(s) - 1 - i]
        i = i + 1
    return revstri

def remove_spaces(s):
    remstri = ''
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
        else:
            remstri = remstri + s[i]
            i += 1
    return remstri

def is_palindrome(s):
    s = remove_spaces(s)
    palistri = reverse_string(s)
    if s == palistri:
        return True
    else:
        return False
    

