def maxlist(list_max):
    i = 0
    max_val = list_max[0]
    while i < len(list_max):
        if list_max[i] > max_val:
            max_val = list_max[i]
        i += 1
    return max_val  

def double(dbl_list):
    i = 0
    while i < len(dbl_list):
        dbl_list[i] = dbl_list[i] * 2
        i += 1
    return dbl_list
