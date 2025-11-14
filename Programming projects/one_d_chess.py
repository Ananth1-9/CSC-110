
'''
Ananth Mugundhan
CSC110
Project - 6
This program creates a game of 1D chess.
'''

def create_board():
    '''
    This function creates the initial game board.
    
    Args:
        None
    
    Returns:
        list: The initial game board.
    '''
    #Defining the initial board components.
    initial_board = ["WKi","WKn","WKn",\
                    "EMPTY","EMPTY","EMPTY",\
                    "BKn","BKn","BKi"]
    return initial_board

def printable_board(board):
    '''
    This function prints the game board.
    
    Args:
        board (list): The current game board.

    Returns:
        str: The visual representation of the game board.
    '''
    #Making the spaces which are empty return blank spaces.
    i = 0
    while i < len(board):
        if board[i] == "EMPTY":
            board[i] = "   "
        i += 1
    
    #Returning the formatted version of the board components.
    return "+-----------------------------------------------------+\n"+\
            "| "+board[0]+" | "+board[1]+" | "+board[2]+\
            " | "+board[3]+" | "+board[4]+" | "+board[5]+\
            " | "+board[6]+" | "+board[7]+" | "+board[8]+" |\n"+\
            "+-----------------------------------------------------+"

def is_valid_move(board,position,colour):
    '''
    This function checks if a move is valid.
    
    Args:
        board (list): The current game board.
        position (int): The position to move from.
        colour (str): The colour of the piece to move.

    Returns:
        bool: True if the move is valid and False if invalid.
    '''
    #Checking if the index provided is in range.
    if position >= 0 and position < len(board):
        #Checking for the colour white.
        if colour == "WHITE":
            if board[position] == "WKi" or board[position] == "WKn":
                return True
            else:
                return False
        #Checking for the colour black.
        if colour == "BLACK":
            if board[position] == "BKi" or board[position] == "BKn":
                return True
            else:
                return False
    else:
        return False

def move_king(board,position,direction):
    '''
    This function moves the king.
    
    Args:
        board (list): The current game board.
        position (int): The position to move from.
        direction (str): The direction to move.

    Returns:
        list: The game board after the move is made.
    '''
    # Do nothing if the move is impossible from the edge.
    if (position == 0 and direction == "LEFT") or \
       (position == len(board) - 1 and direction == "RIGHT"):
        return board

    king_piece = board[position]
    board[position] = "EMPTY" 

    if direction == "LEFT":
        # Find the destination by moving left
        dest = position - 1
        while dest > 0 and board[dest] == "EMPTY":
            dest -= 1
        board[dest] = king_piece

    if direction == "RIGHT":
        # Find the destination by moving right
        dest = position + 1
        while dest < len(board) - 1 and board[dest] == "EMPTY":
            dest += 1
        board[dest] = king_piece
    
    return board

def move_knight(board,position,direction):
    '''
    This function moves the knight.
    
    Args:
        board (list): The current game board.
        position (int): The position to move from.
        direction (str): The direction to move.

    Returns:
        list: The game board after the move is made.
    '''
    #Changing the values for moving the piece to the left.
    if direction == "LEFT" and position > 1:
        board[position - 2] = board[position]
        board[position] = "EMPTY"
    #Changing the values for moving the piece to the right.
    if direction == "RIGHT" and position < len(board) - 2:
        board[position + 2] = board[position]
        board[position] = "EMPTY"
    return board

def move(board,position,direction):
    '''
    This function makes a move.
    
    Args:
        board (list): The current game board.
        position (int): The position to move from.
        direction (str): The direction to move.

    Returns:
        list: The game board after the move is made.
    '''
    #Checking if the piece at the position is a king.
    #Moving the piece using the move_king function.
    if board[position] == "WKi" or board[position] == "BKi":
        return move_king(board,position,direction)
    #Checking if the piece at the position is a knight.
    #Moving the piece using the move_knight function.
    if board[position] == "WKn" or board[position] == "BKn":
        return move_knight(board,position,direction)

def is_game_over(board):
    '''
    This function checks if the game is over.
    
    Args:
        board (list): The current game board.

    Returns:
        bool: True if the game is over and False if it isn't.
    '''
    WKi_present = "WKi" in board
    BKi_present = "BKi" in board
    
    #Checking if white wins (White King is present, Black King is not).
    if WKi_present and not BKi_present:
        print("White wins!" , end = "")
        return True
    #Checking if black wins (Black King is present, White King is not).
    if BKi_present and not WKi_present:
        print("Black wins!" , end = "")
        return True
    # If both kings are present, the game is not over.
    if WKi_present and BKi_present:
        return False
    
    return True 