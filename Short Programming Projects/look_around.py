def make_grid(w, h):
    arr = []
    for i in range(h):
        temparr = []
        for i in range(w):
            temparr.append('o')
        arr.append(temparr)
    return arr

def print_grid(grd):
    for i in grd:
        print(i)

def within_limits(grd, xc, yc):
    rows = len(grd)
    cols = len(grd[0]) if rows > 0 else 0
    if 0 <= xc < rows and 0 <= yc < cols:
        return True
    else:
        return False

def mark_around(grd, xc, yc):
    rows = len(grd)
    cols = len(grd[0])

    for i in range(xc - 1, xc + 2):
        for j in range(yc - 1, yc + 2):
            
            if within_limits(grd, i, j):
                grd[i][j] = 'x'
    return grd

