def total_mean(lst2d):
    for sublst in lst2d:
        tup = []
        max = 0
        for i in sublst:
            max += i
        tup.append(max)
        tup.append(max/len(sublst))
        lst2d.pop(0)
        lst2d.append(tuple(tup))
    return lst2d
print(total_mean([[1,2,3], [1,2,3,4]]))