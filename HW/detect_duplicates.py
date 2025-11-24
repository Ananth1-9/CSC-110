def has_duplicate(lst):
    if len(lst) == 0:
        return None
    for i in lst:
        count = 0
        for j in range(len(lst)):
            if lst[j] == i:
                count += 1
        if count  != 1:
            return True
        else:
            return False
        