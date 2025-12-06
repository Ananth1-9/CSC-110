def sum_nums(lst, num):
    sum = 0
    for sublst in lst:
        for i in range(len(sublst)):
            if sublst[i] < num:
                sum += sublst[i]

    return sum
