'''
Ananth Mugundhan
CSC110
Project - 11
This program creates a simple version of the
popular gamr minesweeper.
'''
def read_file(filename):
    '''
    Reads the minefield configuration 
    from a file and returns the grid.
    Args:
        filename : The name of the file.
    Returns:
        The minefield grid.
    '''
    grid = []
    
    # Open the file manually
    f = open(filename, 'r')
    all_lines = f.readlines()
    
    for line in all_lines[2:]:
        clean_line = line.strip()
        if len(clean_line) > 0:
            parts = clean_line.split(',')
            new_row = []
            for item in parts:
                char = item.strip()
                if char == '1':
                    new_row.append('X')
                else:
                    new_row.append('0')
            
            grid.append(new_row)
    f.close()
    return grid

def make_empty_grid(grid):
    '''
    Creates a new grid filled with
    spaces that has the same size as the input grid.
    Args:
        grid : The minefield grid.
    Returns:
        An empty grid of the same size.
    '''
    empty_grid = []
    rows = len(grid)
    
    if rows == 0:
        return empty_grid
    
    cols = len(grid[0])
    
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(' ')
        empty_grid.append(new_row)
        
    return empty_grid

def update_grid(grid):
    '''
    Modifies the grid to show the number 
    of adjacent mines for each safe square.
    Args:
        grid : The minefield grid.
    Returns:
        None
    '''
    rows = len(grid)
    if rows == 0:
        return
    cols = len(grid[0])
    
    # Update each cell with the count of adjacent mines
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                continue
            
            mine_count = 0
            
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i >= 0 and i < rows and j >= 0 and j < cols:
                        if grid[i][j] == 'X':
                            mine_count += 1
            
            grid[r][c] = str(mine_count)

def dig(grid, coord, user_view):
    '''
    Reveals the square at the given
    coordinate and updates the user view.
    Args:
        grid : The minefield grid.
        coordinate : The coordinate to dig.
        user_view : The user's current view
        of the grid.
    Returns:
        None
    '''
    col_char = coord[0]
    row_num_str = coord[1:]
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    col = 0
    for i in range(len(alphabet)):
        if alphabet[i] == col_char:
            col = i
            break
            
    row_lbl = int(row_num_str)
    rows = len(grid)
    row = rows - 1 - row_lbl
    
    cols = len(grid[0])
    
    # Reveal the square and its neighbors if safe
    if row >= 0 and row < rows and col >= 0 and col < cols:
        
        user_view[row][col] = grid[row][col]
        
        if grid[row][col] != 'X':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i >= 0 and i < rows and j >= 0 and j < cols:
                        if grid[i][j] != 'X':
                            user_view[i][j] = grid[i][j]
    
    print_grid(user_view)

def count_total_moves(grid, user_view):
    '''
    Return the unrevealed safe squares left.
    Args:
        grid : The minefield grid.
        user_view : The user's current view of the grid.
    Returns:
        int: The count of unrevealed safe squares.
    '''
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # Count unrevealed safe squares
    for r in range(rows):
        for c in range(cols):
            if user_view[r][c] == ' ' and grid[r][c] != 'X':
                count += 1
    return count

def print_grid(grid):
    '''
    Prints the grid to the console with row and column labels.
    Args:
        grid : The grid to print.
    Returns:
        None
    '''
    rows = len(grid)
    if rows == 0:
        return
    cols = len(grid[0])

    max_lbl = rows - 1
    lbl_width = len(str(max_lbl))
    
    if lbl_width < 2:
        lbl_width = 2
    
    # Print each row with labels
    for r in range(rows):
        lbl_val = rows - 1 - r
        lbl_str = str(lbl_val)
        
        line = ""
        
        spaces_needed = lbl_width - len(lbl_str)
        for k in range(spaces_needed):
            line += " "
            
        line += lbl_str
        
        for c in range(cols):
            line += "[" + grid[r][c] + "]"
        
        print(line)
    
    bottom_line = ""
    for k in range(lbl_width):
        bottom_line += " "
        
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for c in range(cols):
        letter = alphabet[c]
        bottom_line += " " + letter + " "
        
    bottom_line += " "
    
    print(bottom_line)

def determine_game_status(grid, user_view):
    '''
    Checks if the game should continue or not.
    Args:
        grid : The minefield grid.
        user_view : The user's current 
        view of the grid.
    Returns:
        True if the game 
        should continue, False otherwise.
    '''
    rows = len(grid)
    cols = len(grid[0])

    # Check for revealed mines
    for r in range(rows):
        for c in range(cols):
            if user_view[r][c] == 'X':
                return False
    
    moves_left = count_total_moves(grid, user_view)
    if moves_left == 0:
        return False
        
    return True

