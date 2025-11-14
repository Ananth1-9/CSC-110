'''
Ananth Mugundhan
CSC110
Project -2
Computer restaurant that serves burgers
'''

def top_bun():
    '''
    This is an ingredient
    Args:
        None
    Returns:
        prints ingredient
    '''
    topbun = '''   __________________________
  /     <>            <>     \\
 /  <>       <>   <>      <>  \\
 \\____________________________/'''
    print(topbun)

def bottom_bun():
    '''
    This is an ingredient
    Args:
        None
    Returns:
        prints ingredient
    '''   
    bottombun = '''  ____________________________
 /                            \\
 \\____________________________/'''
    print(bottombun)

def patty():
    '''
    This is an ingredient
    Args:
        None
    Returns:
        prints ingredient
    '''
    patty = '''   __________________________
  |                          |
  |__________________________|'''
    print(patty)

def lettuce():
    '''
    This is an ingredient
    Args:
        None
    Returns:
        prints ingredient
    '''
    lettuce = '''  \\/^\\/^\\/^\\/^\\/^\\/^\\/^\\/^\\/^\\
  \\/^\\/^\\/^\\/^\\/^\\/^\\/^\\/^\\/^\\'''
    print(lettuce)

def tomato():
    tomato = '''  ()()()()()()()()()()()()()()
  |                          |
  ()()()()()()()()()()()()()()'''
    print(tomato)

def bacon():
    '''
    This is an ingredient
    Args:
        None
    Returns:
        prints ingredient
    '''
    bacon = '''  ~~~~~~/\\~~~~~~/\\~~~~~~/\\~~~
  ~~~~~~/\\~~~~~~/\\~~~~~~/\\~~~'''
    print(bacon)

def mushroom():
    '''
    This is an ingredient
    Args:
        None
    Returns:
        prints ingredient
    '''
    mushroom = '''  |  (o)   (o)   (o)   (o)   |'''
    print(mushroom)

def onion():
    onion = '''  |  @@@   @@@   @@@   @@@   |'''
    print(onion)

def serve(order):
    '''
    This returns the final burger based on the order
    Args:
        Order: string taken from next function
    Returns:
        prints the final burger
    '''
    #checks the order and calls the respective ingredients
    if order == 'plain':
        top_bun()
        patty()
        bottom_bun()
    elif order == 'blt':
        top_bun()
        bacon()
        lettuce()
        tomato()
        bottom_bun()
    elif order == 'lettuce wrap':
        lettuce()
        bacon()
        patty()
        tomato()
        lettuce()
    elif order == 'double':
        top_bun()
        patty()
        patty()
        bottom_bun()
    elif order == 'plain add mushroom':
        top_bun()
        mushroom()
        patty()
        bottom_bun()
    elif order == 'double add onion':
        top_bun()
        patty()
        onion()
        patty()
        bottom_bun()
    else:
        print('Sorry, we do not have that option', end = '')

def main():
    '''
    This takes order from user and calls the serve function
    Args:
        None
    Returns:
        prints end result
    '''
    print('''Menu:
    plain
    blt
    lettuce wrap
    double
    plain add mushroom
    double add onion.''')
    order = input('''Enter your choice of burger(please be precise) - ''')
    serve(order)

#checks if the program is still being run
if __name__ == '__main__':
    main()