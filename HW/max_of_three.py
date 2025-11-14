def max_of_three(x,y,z):
    """Returns the maximum of three numbers."""
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
