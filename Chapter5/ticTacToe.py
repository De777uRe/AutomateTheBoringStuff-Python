TOP_L = 'top-L'
TOP_M = 'top-M'
TOP_R = 'top-R'

MID_L = 'mid-L'
MID_M = 'mid-M'
MID_R = 'mid-R'

LOW_L = 'low-L'
LOW_M = 'low-M'
LOW_R = 'low-R'

theBoard = {TOP_L: ' ', TOP_M: ' ', TOP_R: ' ',
            MID_L: ' ', MID_M: ' ', MID_R: ' ',
            LOW_L: ' ', LOW_M: ' ', LOW_R: ' '}


def printBoard(board):
    print(board[TOP_L] + '|' + board[TOP_M] + '|' + board[TOP_R])
    print('-+-+-')
    print(board[MID_L] + '|' + board[MID_M] + '|' + board[MID_R])
    print('-+-+-')
    print(board[LOW_L] + '|' + board[LOW_M] + '|' + board[LOW_R])


def checkHorizTop(board):
    isWin = False
    if board[TOP_L] == board[TOP_M] and board[TOP_M] == board[TOP_R]:
        isWin = True
    return isWin


def checkHorizMid(board):
    isWin = False
    if board[MID_L] == board[MID_M] and board[MID_M] == board[MID_R]:
        isWin = True
    return isWin


def checkHorizLow(board):
    isWin = False
    if board[LOW_L] == board[LOW_M] and board[LOW_M] == board[LOW_R]:
        isWin = True
    return isWin


def checkVertLeft(board):
    isWin = False
    if board[TOP_L] == board[MID_L] and board[MID_L] == board[LOW_L]:
        isWin = True
    return isWin


def checkVertMid(board):
    isWin = False
    if board[TOP_M] == board[MID_M] and board[MID_M] == board[LOW_M]:
        isWin = True
    return isWin


def checkVertRight(board):
    isWin = False
    if board[TOP_R] == board[MID_R] and board[MID_R] == board[LOW_R]:
        isWin = True
    return isWin


def checkDiagBackward(board):
    isWin = False
    if board[TOP_L] == board[MID_M] and board[MID_M] == board[LOW_R]:
        isWin = True
    return isWin


def checkDiagForward(board):
    isWin = False
    if board[LOW_L] == board[MID_M] and board[MID_M] == board[TOP_R]:
        isWin = True
    return isWin


def checkWin(board):
    isWin = False
    if checkHorizTop(board) or checkHorizMid(board) or checkHorizLow(board) or \
            checkVertLeft(board) or checkVertMid(board) or checkVertRight(board) or \
            checkDiagBackward(board) or checkDiagForward(board):
        isWin = True
    return isWin


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
checkWin(theBoard)
