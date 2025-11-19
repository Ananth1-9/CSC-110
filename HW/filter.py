def remove_zero_sides(numbers):
    for sublst in numbers:
        if len(sublst) > 0 and sublst[0] == 0:
            sublst.pop(0)

        if len(sublst) > 0 and sublst[-1] == 0:
            sublst.pop(-1)
            
    return numbers