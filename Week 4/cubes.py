def get_fit(cube_len, side):
    side1 = int(input('Enter length of the {} - '.format(side)))
    cube_num = side1//cube_len
    return cube_num

def main():
    cube_len = int(input("Cube length? "))
    fit_w = get_fit(cube_len, 'width')
    fit_h = get_fit(cube_len, 'height')
    fit_l = get_fit(cube_len, 'length')
    result = fit_w * fit_h * fit_l
    print(str(result) + " Rubik's cubes will fit in that container.")
