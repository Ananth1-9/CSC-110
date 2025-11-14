#lilian 
def sum_all(list_num):
    total = 0
    num = len(list_num)
    i = 0
    while i < num:
        total = total + list_num[i]
        i = i + 1
    return total
