'''
Ananth Mugundhan
CSC110
Project - 12
This program implements a word search solver.
It finds words horizontally and vertically (forward and backward)
and prints their starting coordinates.
'''

def get_word_bank(filename):
    '''
    Reads the list of words to find from a file.
    Args:
    filename: the name of the file to read.
    Returns:
    A list of strings representing the words to search for.
    '''
    words = []
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    #remove whitespace and empty lines
    for line in lines:
        cleaned = line.strip()
        if len(cleaned) > 0:
            words.append(cleaned)
    return words
def get_grid(filename):
    '''
    Reads the puzzle grid from a file.
    Args:
    filename: the name of the file to read.
    Returns:
    A 2D list representing the grid of letters.
    '''
    grid = []
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    #remove whitespace and empty lines
    for line in lines:
        cleaned_line = line.strip()
        if len(cleaned_line) > 0:
            row = cleaned_line.split()
            grid.append(row)
            
    return grid

def reverse_string(s):
    '''
    Reverses a string 
    Args:
    s: the string to reverse.
    Returns:
    The reversed string.
    '''
    rev = ""
    length = len(s)
    #reverse the string
    for i in range(length):
        index = length - 1 - i
        rev += s[index]
    return rev

def get_rows_as_strings(grid):
    '''
    Converts the 2D grid list into a list of row strings.
    Args:
    grid: the 2D list of characters.
    Returns:
    A list of strings, where each string is a row.
    '''
    row_strings = []
    #convert each row to a string
    for r in grid:
        s = ""
        for char in r:
            s += char
        row_strings.append(s)
    return row_strings

def get_cols_as_strings(grid):
    '''
    Converts the 2D grid list into a list of column strings.
    Args:
    grid: the 2D list of characters.
    Returns:
    A list of strings, where each string is a column.
    '''
    col_strings = []
    rows = len(grid)
    #handle empty grid
    if rows == 0:
        return col_strings
    cols = len(grid[0])
    #convert each column to a string
    for c in range(cols):
        s = ""
        for r in range(rows):
            s += grid[r][c]
        col_strings.append(s)
        
    return col_strings

def find_word_in_list(lines, word, is_vertical):
    '''
    Searches for a word in a list of strings.
    Args:
    lines: list of strings.
    word: the word to search for.
    is_vertical: boolean, True if searching columns.
    Returns:
    A list [row, col] if found, or None if not found.
    '''
    #search forward
    for i in range(len(lines)):
        line = lines[i]
        index = line.lower().find(word)
        if index != -1:
            if is_vertical:
                return [index + 1, i + 1]
            else:
                return [i + 1, index + 1]
    rev_word = reverse_string(word)
    #search backward
    for i in range(len(lines)):
        line = lines[i]
        index = line.lower().find(rev_word)
        if index != -1:
            real_start = index + len(word) - 1
            if is_vertical:
                return [real_start + 1, i + 1]
            else:
                return [i + 1, real_start + 1]
                
    return None

def main():
    '''
    Main function to run the word search program.
    Args:
    None
    Returns:
    None
    '''
    word_filename = input("Name of the word bank file: ")
    grid_filename = input("Name of the grid file: ")
    words = get_word_bank(word_filename)
    grid = get_grid(grid_filename)
    rows = get_rows_as_strings(grid)
    cols = get_cols_as_strings(grid)
    results = {}
    for word in words:
        location = find_word_in_list(rows, word, False)
        
        if location:
            results[word] = location
        else:
            location = find_word_in_list(cols, word, True)
            if location:
                results[word] = location
    
    print(results)