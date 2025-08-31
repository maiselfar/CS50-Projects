"""
Tic Tac Toe Player
"""

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
    count = 0

    for row in board:
        for cell in row:
            count += 1 if cell is not EMPTY else 0

    if count == 0 or (count %2 == 0):
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                set_of_actions.add((i,j))
    return set_of_actions
            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    updated_board = [row[:] for row in board]

    updated_board[action[0]][action[1]] = player(board)

    return updated_board
    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    for i, row in enumerate(board):
        if row[0] is not EMPTY and row[0] == row[1] == row[2]:
            winner = row[0]
            return winner
        for j, cell in enumerate(row):
            if board[0][j] is not EMPTY and board[0][j] == board[1][j] == board [2][j]:
                winner = board[0][j]
                return winner
            elif board[1][1] is not EMPTY and (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
                winner = board[1][1]
                return winner
            
    return winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_game_over = False
    if winner(board) is not None or actions (board) == set():
        is_game_over = True

    return is_game_over

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility_value = 0

    if terminal(board):
        if winner(board) == X:
            utility_value = 1
        elif winner(board) == O:
            utility_value = -1
    return utility_value


def maximum_value(board):

    if terminal(board):
        return utility(board)
    
    value = -math.inf
    for action in actions(board):
        value = max(value, minimum_value(result(board,action)))
    return value

def minimum_value(board):

    if terminal(board):
        return utility(board)
    
    value = math.inf
    for action in actions(board):
        value = min(value, maximum_value(result(board,action)))
    return value

def minimax (board):
    
    "retun the best move"

    if terminal(board):
        return None
    
    if player(board) == X:
        max_value = -math.inf
        best_action = None
        for action in actions(board):
            value = minimum_value(result(board,action))
            if value > max_value:
                max_value = value
                best_action = action
        return best_action

    if player(board) == O:
        v = math.inf
        best_action = None

        for action in actions (board):
            min_value = maximum_value(result(board, action))
            if min_value<v:
                v = min_value
                best_action = action
        return best_action




