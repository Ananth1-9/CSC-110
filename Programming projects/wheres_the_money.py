'''Ananth Mugundhan
CSC 110
Project -4
A program that shows where your money goes based on your salary
'''

def yearly_sal(args):
    '''This function returns the yearly salary
    Args:
        args (int): yearly salary
    Returns:
         returns the yearly salary'''
    return args

def rent(argr):
    '''This function returns the yearly rent based on monthly rent
    Args:
        argr (int): monthly rent
    Returns:
         returns the yearly rent'''
    yrent = argr * 12
    return yrent

def bills(argb):
    '''This function returns the yearly bills based on monthly bills
    Args:
        argb (int): monthly bills
    Returns:
         returns the yearly bills'''
    ybills = argb * 12
    return ybills

def food(argf):
    '''This function returns the yearly food based on weekly food
    Args:
        argf (int): weekly food
    Returns:
         returns the yearly food'''
    yfood = argf * 52
    return yfood

def travel(argt):
    '''This function returns the yearly travel
    Args:
        argt (int): yearly travel
    Returns:
        returns the yearly travel'''
    return argt

def calculate_tax(yearly_salary):
    '''This function returns the tax based on yearly salary 
    and calculating your tax bracket
    Args:
        yearly_salary (int): yearly salary
    Returns:
        returns the tax'''
    #checking tax brackets and calculating tax
    if 0 <= yearly_salary <= 15000:
        tax = yearly_salary *0.10
    elif 15000 < yearly_salary <= 75000:
        tax = yearly_salary *0.20
    elif 75000 < yearly_salary <= 200000:
        tax = yearly_salary *0.25
    elif yearly_salary > 200000:
        tax = yearly_salary *0.30
    if tax > 75000:
        tax = 75000
    return tax

def max(a,b,c,d,e,f):
    '''This function returns the maximum value among the six inputs
    Args:
        a (float): first value
        b (float): second value
        c (float): third value
        d (float): fourth value
        e (float): fifth value
        f (float): sixth value
    Returns:
        returns the maximum value'''
    max_val = a
    # Check each value and update max_val if a larger value is found
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    if d > max_val:
        max_val = d
    if e > max_val:
        max_val = e
    if f > max_val:
        max_val = f
    return max_val

def wheres_the_money(yearly_salary, yrent,
                      ybills, yfood, ytravel):
    '''This function prints a financial breakdown based on the inputs
    Args:
        yearly_salary (int): yearly salary
        yrent (int): yearly rent
        ybills (int): yearly bills
        yfood (int): yearly food
        ytravel (int): yearly travel
    Returns:
        a table showing the financial breakdown'''
    #getting the yearly values
    yrent = rent(yrent)
    ybills = bills(ybills)
    yfood = food(yfood)
    ytravel = travel(ytravel)   
    ytax = calculate_tax(yearly_salary)

    # Caculating percentages of yearly salary each expense takes up
    yrentp = (yrent / yearly_salary) * 100
    ybillsp = (ybills / yearly_salary) * 100
    yfoodp = (yfood / yearly_salary) * 100
    ytaxp = (ytax / yearly_salary) * 100
    ytravelp = (ytravel / yearly_salary) * 100

    # Finding extra money left over after expenses and its percentage
    extra = yearly_salary - (yrent + ybills + 
                             yfood + ytax + ytravel)
    extrap = (extra / yearly_salary) * 100

    # Finding the maximum percentage for formatting the table
    maxhash = int(max(yrentp, ybillsp, yfoodp,
                       ytaxp, extrap, ytravelp))
    
    # Printing the financial breakdown table
    print('-'*(42+maxhash))
    print('See the financial breakdown below, based on a salary of ${}'
          .format(yearly_salary))
    print('-'*(42+maxhash))
    print('| mortgage/rent | ${:>11,.2f} | {:>5}% | {}'
          .format(yrent, round(yrentp, 1), '#' * int(yrentp)))
    print('|         bills | ${:>11,.2f} | {:>5}% | {}'
          .format(ybills, round(ybillsp, 1), '#' * int(ybillsp)))
    print('|          food | ${:>11,.2f} | {:>5}% | {}'
          .format(yfood, round(yfoodp, 1), '#' * int(yfoodp)))
    print('|        travel | ${:>11,.2f} | {:>5}% | {}'
          .format(ytravel, round(ytravelp, 1), '#' * int(ytravelp)))
    print('|           tax | ${:>11,.2f} | {:>5}% | {}'
          .format(ytax, round(ytaxp, 1), '#' * int(ytaxp)))
    print('|         extra | ${:>11,.2f} | {:>5}% | {}'
          .format(extra, round(extrap, 1), '#' * int(extrap)))
    print('-'*(42+maxhash))   

    
    # Printing warnings based on financial situation
    if extra < 0:
        print('>>> WARNING: DEFICIT <<<')
    if ytax == 75000:
        print('>>> TAX LIMIT REACHED <<<')

wheres_the_money(40000, 2000, 300, 150, 4000)