import random

def displayBoard(b):
    print('     |     |')
    print('  ' + ('0' if b[0] == ' ' else b[0])  + '  |  ' + ('1' if b[1] == ' ' else b[1]) + '  |  ' + ('2' if b[2] == ' ' else b[2]))
    print('     |     |')
    print('--------------------')
    print('     |     |')
    print('  ' + ('3' if b[3] == ' ' else b[3]) + '  |  ' + ('4' if b[4] == ' ' else b[4]) + '  |  ' + ('5' if b[5] == ' ' else b[5]))
    print('     |     |')
    print('--------------------')
    print('     |     |')
    print('  ' + ('6' if b[6] == ' ' else b[6]) + '  |  ' + ('7' if b[7] == ' ' else b[7]) + '  |  ' + ('8' if b[8] == ' ' else b[8]))
    print('     |     |')
    print('-------------------------------------------')

def checkWin(b, m):
    ''' Here we do a check for all the possible winning positions '''
    return ((b[0] == m and b[1] == m and b[2] == m) or  # Row 0-1-2
            (b[3] == m and b[4] == m and b[5] == m) or  # Row 3-4-5
            (b[6] == m and b[7] == m and b[8] == m) or  # Row 6-7-8
            (b[0] == m and b[3] == m and b[6] == m) or  # Column 0-3-6
            (b[1] == m and b[4] == m and b[7] == m) or  # Column 1-4-7
            (b[2] == m and b[5] == m and b[8] == m) or  # Column 2-5-8
            (b[0] == m and b[4] == m and b[8] == m) or  # Diagonal 0-4-8
            (b[2] == m and b[4] == m and b[6] == m))    # Diagonal 2-4-6

def checkDraw(b):
    ''' Here we check if there are no possible ways for either the User or PC 
        to win the game '''
    return ' ' not in b

def getBoardCopy(b):
    ''' We need to make a duplicate of the board so that we can test winning 
        moves without changing the actual board '''
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def testWinMove(b, mark, i):
    ''' b = the board
        mark = O or X
        i = the square to check if makes a win ''' 
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)

def testForkMove(b, mark, i):
    ''' To check if a move opens up a fork '''
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2

firstComputerMove = True

def getComputerMoveEasy(b,firstComputerMove):
    
    if firstComputerMove == True:
        i = random.randint(0,8)
        while(b[i] != ' '):
            i = random.randint(0,8)
        b[i] = 'X'
        firstComputerMove = False
        return i
    
    ''' Check for winning moves for the computer '''
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    ''' Check for winning moves for the User '''
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'O', i):
            return i
    ''' If a corner postition is played '''
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    ''' If the center postition is played '''
    if b[4] == ' ':
        return 4
    ''' If a side postition is played '''
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i
        
def getComputerMoveMedium(b,firstComputerMove):
    
    ''' Check fork opportunities for the User '''
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'O', i):
            return i
    ''' Check for winning moves for the User '''
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'O', i):
            return i
    ''' Check fork opportunities for the computer '''
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'X', i):
            return i
    ''' Check for winning moves for the computer '''
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    ''' If a corner postition is played '''
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    ''' If the center postition is played '''
    if b[4] == ' ':
        return 4
    ''' If a side postition is played '''
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i
        
def getComputerMoveHard(b, firstComputerMove):
    
    ''' Check fork opportunities for the User '''
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'O', i):
            return i    
    ''' Check fork opportunities for User, including two forks '''
    playerForks = 0
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'O', i):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j
    ''' Check for winning moves for the User '''
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'O', i):
            return i    
    ''' Check fork opportunities for the computer '''
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'X', i):
            return i
    ''' Check for winning moves for the computer '''
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    ''' If a corner postition is played '''
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    ''' If the center postition is played '''
    if b[4] == ' ':
        return 4
    ''' If a side postition is played '''
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i 

Playing = True
while Playing:
    print('Welcome to the game of TIC-TAC-TOE')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('The markers for the game are: ')
    print('User - O')
    print('Computer - X')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('At what difficulty level would you like to play?')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    _in1 = input()
    if (_in1 != '1' and _in1 != '2' and _in1 != '3'):
        print('Enter valid number')
        continue
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    firstComputerMove = True
    InGame = True
    board =  [' '] * 9
    print('Would you like to go first or second? (1/2)')
    _in2 = input()
    if _in2 == '1':
        playerMarker = 'O'
    elif _in2 == '2':
        playerMarker = 'X'
    else:
        print('Enter either 1 or 2 only')
        continue
    displayBoard(board)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    while InGame:
        if playerMarker == 'O':
            print('Selct a spot: (0-8)')
            move = int(input())
            if board[move] != ' ':
                print('Invalid move!')
                continue
        else:
            if _in1 == '1':
                move = getComputerMoveEasy(board,firstComputerMove)
            elif _in1 == '2':
                move = getComputerMoveMedium(board,firstComputerMove)
            elif _in1 == '3':
                move = getComputerMoveHard(board,firstComputerMove)
        board[move] = playerMarker
        if checkWin(board, playerMarker): 
            InGame = False
            displayBoard(board)
            if playerMarker == 'O':
                print('~~~~ User Wins ~~~~')
            else:
                print('~~~~ Computer Wins ~~~~~')
            continue
        if checkDraw(board):
            InGame = False
            displayBoard(board)
            print('It was a draw!')
            continue
        displayBoard(board)
        if playerMarker == 'O':
            playerMarker = 'X'
        else:
            playerMarker = 'O'

    print('Do you wish to play another game (Y-Yes/N-No)??')
    inp = input()
    if inp != 'y' and inp != 'Y':
        Playing = False