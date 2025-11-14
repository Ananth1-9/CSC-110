def build_car(width):
    '''
    A simple program to print a model T car of variable width.
    '''
    line_1 = '.'+ '-'*(11+width)+'.'
    line_2 = '| ### ||  '+'#'*(3+width)+'\\'
    line_3 = '| ### ||  '+'#'*(4+width)+'\\.'
    line_4 = 'D     ||'+ ' '*(2+width)+'<>    |------+' 
    line_5 = '|  ______'+' '*(5+width)+' /______ |'
    line_6 = ' \\/ /..\\ \\_'+'_'*(4+width)+'/ /..\\ \\|'
    line_7 = '    \\__/'+' '*(9+width)+'\\__/'
    return line_1+'\n'+line_2+'\n'+line_3+'\n'+line_4+'\n'+line_5+'\n'+line_6+'\n'+line_7


width = 0
car = build_car(width)
print(car, end = "")

width = 5
car = build_car(width)
print(car, end="")

width = 12
car = build_car(width)
print(car, end="")

width = 20
car = build_car(width)
print(car, end="")