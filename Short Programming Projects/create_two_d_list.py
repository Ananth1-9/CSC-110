import random

def create_list(w, l):
    random.seed(123)
    outlst = []
    for i in range(l):
        templst = []
        for j in range(w):
            rno = random.randint(0,100)
            templst.append(rno)
        outlst.append(templst)
    return outlst

