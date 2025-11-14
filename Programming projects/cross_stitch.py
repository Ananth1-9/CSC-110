
'''
Ananth Mugundhan
CSC 110
Project -7
A cross stitch program that uses 2d list
manipulation
'''
import random

SYMBOLS = [" ◎ ", " △ ", " ▞ ", " ● ", " ▣ ", 
           " ▤ ", " ▲ ", " ▼ ", " * ", " < ",
           " > ", " = ", " ≡ ", " ☼ ", " ♦ ",
           " ◭ ", " ► ", " ◘ ", " ◓ ", " ▌ "]

def print_pattern(pattern):
    """
    Prints the 2D list (pattern) as a grid.
    This function was provided in the starter code.
    """
    if not pattern:
        print("Pattern is empty.")
        return
    
    width = len(pattern[0])  - 1
    top_line = "┌" + "───┬" * width + "───┐"
    print(top_line)
    for i in range(len(pattern)):
        new_row = "│"
        for j in range(len(pattern[i])):
            new_row += pattern[i][j] + "│"
        print(new_row)
        if i != len(pattern) - 1:
            print("├" + "───┼" * width + "───┤")
    bottom_line = "└" + "───┴" * width + "───┘"
    print(bottom_line)

def create_background(width, length, num_symbols):
    """
    Creates a new pattern as a 2D list with the specified dimensions,
    filled with random symbols from the first 'num_symbols' in the 
    SYMBOLS list.
    
    Args:
        width (int): The number of columns in the pattern.
        length (int): The number of rows in the pattern.
        num_symbols (int): The number of unique symbols to use from SYMBOLS.
    
    Returns:
        list: A 2D list representing the random background pattern.
    """
    random.seed(123)
    
    pattern = []
    for x in range(length):
        row = []
        for y in range(width):
            rand_index = random.randint(0, num_symbols - 1)
            row.append(SYMBOLS[rand_index])
        pattern.append(row)
    return pattern

def add_v_stripe(pattern, y_start, width, symbol_index):
    """
    Adds a vertical stripe to the pattern spanning all rows.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        y_start (int): The starting column index for the stripe.
        width (int): The width (in columns) of the stripe.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern 
    
    num_cols = len(pattern[0])
    
    for x in range(num_rows): 
        for y in range(y_start, y_start + width):
            if y < num_cols: 
                pattern[x][y] = symbol
    return pattern

def add_h_stripe(pattern, x_start, height, symbol_index):
    """
    Adds a horizontal stripe to the pattern spanning all columns.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The starting row index for the stripe.
        height (int): The height (in rows) of the stripe.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern 
    
    num_cols = len(pattern[0])
    
    for x in range(x_start, x_start + height): 
        if x < num_rows: 
            for y in range(num_cols): 
                pattern[x][y] = symbol
    return pattern

def add_square(pattern, x_start, y_start, size, symbol_index):
    """
    Adds a square to the pattern.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The top row index of the square.
        y_start (int): The left column index of the square.
        size (int): The width and height of the square.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    return add_rectangle(pattern, x_start, y_start, size, size, symbol_index)

def add_rectangle(pattern, x_start, y_start, width, height, symbol_index):
    """
    Adds a rectangle to the pattern.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The top row index of the rectangle.
        y_start (int): The left column index of the rectangle.
        width (int): The width (in columns) of the rectangle.
        height (int): The height (in rows) of the rectangle.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern
        
    num_cols = len(pattern[0])

    for x in range(x_start, x_start + height): 
        for y in range(y_start, y_start + width):
            if x < num_rows and y < num_cols: 
                pattern[x][y] = symbol
    return pattern

def add_triangle_a(pattern, x_start, y_start, size, symbol_index):
    """
    Adds a lower-left triangle (type A) to the pattern.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The top row index of the triangle's bounding box.
        y_start (int): The left column index of the triangle's bounding box.
        size (int): The size of the triangle's bounding box.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern
    num_cols = len(pattern[0])

    for rel_x in range(size):
        for rel_y in range(size): 
            
            if rel_y <= rel_x:
                x = x_start + rel_x
                y = y_start + rel_y
                
                if x < num_rows and y < num_cols:
                    pattern[x][y] = symbol
    return pattern

def add_triangle_b(pattern, x_start, y_start, size, symbol_index):
    """
    Adds a lower-right triangle (type B) to the pattern.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The top row index of the triangle's bounding box.
        y_start (int): The left column index of the triangle's bounding box.
        size (int): The size of the triangle's bounding box.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern
    num_cols = len(pattern[0])

    for rel_x in range(size):
        for rel_y in range(size):
            
            if rel_y >= (size - 1) - rel_x:
                x = x_start + rel_x
                y = y_start + rel_y
                
                if x < num_rows and y < num_cols:
                    pattern[x][y] = symbol
    return pattern

def add_triangle_c(pattern, x_start, y_start, size, symbol_index):
    """
    Adds an upper-left triangle (type C) to the pattern.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The top row index of the triangle's bounding box.
        y_start (int): The left column index of the triangle's bounding box.
        size (int): The size of the triangle's bounding box.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern
    num_cols = len(pattern[0])

    for rel_x in range(size):
        for rel_y in range(size):
            
            if rel_y + rel_x < size:
                x = x_start + rel_x
                y = y_start + rel_y
                
                if x < num_rows and y < num_cols:
                    pattern[x][y] = symbol
    return pattern

def add_triangle_d(pattern, x_start, y_start, size, symbol_index):
    """
    Adds an upper-right triangle (type D) to the pattern.
    
    Args:
        pattern (list): The 2D pattern list to modify.
        x_start (int): The top row index of the triangle's bounding box.
        y_start (int): The left column index of the triangle's bounding box.
        size (int): The size of the triangle's bounding box.
        symbol_index (int): The index of the symbol in SYMBOLS to use.
        
    Returns:
        list: The modified 2D pattern list.
    """
    symbol = SYMBOLS[symbol_index]
    num_rows = len(pattern)
    if num_rows == 0:
        return pattern
    num_cols = len(pattern[0])

    for rel_x in range(size):
        for rel_y in range(size):
            
            if rel_y >= rel_x:
                x = x_start + rel_x
                y = y_start + rel_y
                
                if x < num_rows and y < num_cols:
                    pattern[x][y] = symbol
    return pattern


if __name__ == "__main__":
    pattern = create_background(15, 10, 2)
    pattern = add_h_stripe(pattern, 6, 4, 6)
    pattern = add_square(pattern, 6, 4, 4, 3)
    add_triangle_a(pattern, 8, 0, 4, 17)
    add_triangle_b(pattern, 4, 0, 4, 17)
    
    print("--- Your Custom Pattern ---")
    print_pattern(pattern)
    
    