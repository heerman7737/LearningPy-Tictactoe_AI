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
    if (any(EMPTY in row for row in board)):
        numX = sum(row.count(X) for row in board)
        numO = sum(row.count(O) for row in board)

        if (numO == numX):
            return X
        else:
            return O
    else:
        return 
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    poss = set()
    flag = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                flag = 1
                #s = str(i)+str(j)
                poss.add((i,j))

    if (flag==0):
        return -1
    else:
        return poss
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    i, j = action
    if (newBoard[i][j] != EMPTY):
        raise Exception("Not possible")
    else:
        turn = player(newBoard)
        newBoard[i][j] = turn
        return newBoard
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if matches all rows
    for i in range(3):
        if (board[i].count(X) == 3):
            return X
        elif (board[i].count(O) == 3):
            return O
    
    # for all columns
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] == X):
            return X
        elif (board[0][i] == board[1][i] == board[2][i] == O):
            return O

    # for main diagonal 
    flagX = 0
    flagO = 0
    for i in range(3):
        if (board[i][i] == X):
            flagX += 1
        elif (board[i][i] == O):
            flagO += 1
    if (flagX == 3):
        return X
    elif (flagO == 3):
        return O
    
    #for anti diagonal
    flagO = 0
    flagX = 0
    for i in range(3):
        if (board[i][3-i-1] == X):
            flagX += 1
        elif (board[i][3-i-1] == O):
            flagO += 1
    if (flagX == 3):
        return X
    elif (flagO == 3):
        return O
    
    return None
    #raise NotImplementedError



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)!=None):
        return True
    
    fill = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] !=  EMPTY):
                fill += 1

    if (fill == 9):
        return True
    else:
        return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if (w == X):
        return 1
    elif (w == O):
        return -1
    else:
        return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board) == True):
        return None
    elif (player(board) == X):
        best = -2
        bestMove = tuple()
        moves = actions(board)
        for move in moves:
            move_val = MIN(result(board,move))
            if (move_val == 1):
                return move
            elif (move_val > best):
                best = move_val
                bestMove = move
        return bestMove
    elif (player(board) == O):
        best = 2
        bestMove = tuple()
        moves = actions(board)
        for move in moves:
            move_val = MAX(result(board,move))
            if (move_val == -1):
                return move
            elif (move_val < best):
                best = move_val
                bestMove = move
        return bestMove
    # raise NotImplementedError

def MAX(board):
    if (terminal(board) == True):
        return utility(board)
    
    m = -2
    moves = actions(board)
    for move in moves:
        m = max(m, MIN(result(board,move)))
        if (m == 1):
            return m
    return m


def MIN(board):
    if (terminal(board) == True):
        return utility(board)
    
    m = 2
    moves = actions(board)
    for move in moves:
        m = min(m, MAX(result(board,move)))
        if (m==-1):
            return m
    return m