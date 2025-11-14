def hypotenuse(a,b):
    """Returns the length of the hypotenuse of a right triangle
    with legs of length a and b.
    """
    c = (a**2 + b**2)**0.5
    return round(c,2)

print(round(hypotenuse(3,4),2))
print(round(hypotenuse(10,10),2))