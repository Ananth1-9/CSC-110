def rectangle_area(base, height):
    area = base * height
    return area

def triangle_area(a,b,c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def trapezoid_area(base_1, base_2, height):
    area = (1/2)*(base_1 + base_2) * height
    return area

def circle_area(radius):
    area = 3.1415 * radius**2
    area = round(area, 2)
    return area

def calculate_area(shape, arg1, arg2, arg3):
    if shape == 'rectangle':
        a = rectangle_area(arg1, arg2)
        return 'The are of the rectangle is {}'.format(a)
    elif shape == 'triangle':
        a = triangle_area(arg1, arg2, arg3)
        return 'The area of the triangle is {}'.format(a)
    elif shape == 'trapezoid':
        a = trapezoid_area(arg1, arg2, arg3)
        return 'The area of the trapezoid is {}'.format(a)
    elif shape == 'circle':
        a = circle_area(arg1)
        return 'The area of the circle is {}'.format(a)
    else:
        print('Error')

def main():
    print( rectangle_area(4, 4.5) ) 
    print( triangle_area(3, 4, 5) ) 
    print( trapezoid_area(4, 20, 10) ) 
    assert circle_area(20) == 1256.6

    message = calculate_area("trapezoid", 11, 25, 5)
    print(message) 
    
    message = calculate_area("circle", 4, 0, 0)
    print(message) 
  
main()