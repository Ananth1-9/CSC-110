import random

def random_list(lstnum):
    random.seed(123)
    i = 0
    while i < len(lstnum):
        temp = lstnum[i]
        temprep = random.randint(0,temp)
        lstnum[i] = temprep
        i += 1
    return lstnum

print(random_list([3,2,1,3,5]))