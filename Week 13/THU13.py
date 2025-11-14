def nested_loop(nstlst):
    max = 0
    for i in range(len(nstlst)):
        for j in range(len(nstlst[i])):
            if nstlst[i][j] >= max:
                max = nstlst[i][j]
    return max


