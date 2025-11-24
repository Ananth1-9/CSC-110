def differences(set1, set2):
    count = 0
    for i in set1:
        if i  not in set2:
            count += 1
    for j in set2:
        if j not in set1:
            count += 1

    return count