"""
Tic Tac Toe Player
"""

import math
import copy

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

    num_x=0
    num_o=0

    for i in range(3):
        for j in range(3):
            if board[i][j] == O:
                num_o +=1
            if board[i][j] == X:
                num_x +=1

    if num_o == num_x:
        return X
    if num_x > num_o:
        return O
    else:
        pass


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.add((i,j))
    return possible



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a1 , a2 = action
    move = player(board)
    copy_board= copy.deepcopy(board)
    possible_actions=actions(board)

    if action not in possible_actions:
        raise ValueError('Impossible action!')

    copy_board[a1][a2] = move

    return copy_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    control_variable=board[0][0]

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    val = winner(board)
    if winner(board) is not None:
        return True
    if not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) is True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_val(board):
        if terminal(board):
            return utility(board)
        val = -float('inf')
        for action in actions(board):
            further_score = min_val(result(board,action))
            val = max(val,further_score)
        return val

    def min_val(board):
        if terminal(board):
            return utility(board)
        val = float('inf')
        for action in actions(board):
            further_score = max_val(result(board,action))
            val=min(val,further_score)
        return val

    if terminal(board): #game is over here
        return None
    current_player = player(board)
    optimal = None
    if current_player == X:
        score = -float('inf')
        for action in actions(board):
            further_score = min_val(result(board,action))
            if further_score > score:
                score = further_score
                optimal = action

    else:
        score = float('inf')
        for action in actions(board):
            further_score = max_val(result(board,action))
            if further_score < score:
                score = further_score
                optimal = action

    return optimal
