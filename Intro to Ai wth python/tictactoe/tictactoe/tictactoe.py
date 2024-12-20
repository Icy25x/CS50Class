"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for rows in board:
        for blocks in rows:
            if blocks == X:
                Xcount += 1 
            if blocks == O:
                Ocount += 1
    if Ocount < Xcount:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board[:][1])):
        for j in range(len(board[1][:])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions
    raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    for i, j in action:        
        new_board = copy.deepcopy(board)
        new_board[i][j] = player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check horizontal 
    for i in range(len(board[:][1])): #increment through each row at a time
        if board[i][0] == board[i][1] & board[i][0] == board[i][2] & board[i][0] != EMPTY: #check all columns in row
            return board[i][0]
        
    #check vertical
    for j in range(len(board[1][:])): #increment through each column
        if board[0][j] == board[1][j] & board[0][j] == board[2][j] & board[0][j] != EMPTY: #check each row in a column
            return board[0][j]
        
    #check diag
    if board[0][0] == board[1][1] & board[0][0] == board[2][2] & board[0][0] != EMPTY:
        return board[0][i]
    
    if board[0][2] == board[1][1] & board[2][0] == board[2][2] & board[0][2] != EMPTY:
        return board[0][i]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:   #if there is a winner, obviously the game is fucking over. 
        return True
    elif winner(board) == None:
        if not list(actions(board)): #if there is an empty set of actions, game is over
            return True
        else:               #if there are actions, game is not over. 
            return False 
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    a = winner(board)

    if terminal(board) == True:
        if a == X:
            return 1
        elif a == O:
            return -1
        else:
            return 0
    else:
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # No moves left if the game is over

    current_player = player(board)  # Determine who is playing

    if current_player == X:
        best_val = float("-inf")
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            val = minValue(new_board)
            if val > best_val:
                best_val = val
                best_action = action
        return best_action

    elif current_player == O:
        best_val = float("inf")
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            val = maxValue(new_board)
            if val < best_val:
                best_val = val
                best_action = action
        return best_action


def maxValue(board):
    """
    Helper function to find the maximum value for the maximizing player (X).
    """
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        new_board = result(board, action)
        v = max(v, minValue(new_board))
    return v


def minValue(board):
    """
    Helper function to find the minimum value for the minimizing player (O).
    """
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        new_board = result(board, action)
        v = min(v, maxValue(new_board))
    return v