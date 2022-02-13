# Tic Tac Toe program 
# Author - Mantha Sai Gopal 

# function to take size of the grid as input and initialize the grid
def Initalize():                        
    global size
    size = int(input("Enter the grid size: "))

    global grid
    grid = [['-'] * size for i in range(size)]

# function to print the grid
def ShowGrid():
    for row in range(size):
        for col in range(size):
            print(grid[row][col], end = " ")
        print('\n')

def Player1Input():
    x = -1
    y = -1
    while not ValidateInput(x, y):
        inp = input("Player 1 Enter coma separated x, y values:")
        x, y = ProcessInput(inp)
    return x, y

def Player2Input():
    x = -1
    y = -1
    while not ValidateInput(x, y):
        inp = input("Player 2 Enter coma separated x, y values:")
        x, y = ProcessInput(inp)
    return x, y

def ProcessInput(inp):
    inp = inp.split(',')
    x = int(inp[0])
    y = int(inp[1])
    return x, y

def ModifyGrid(x, y, sym):
    grid[x][y] = sym

def ValidateInput(x, y):
    if x < 0 or y < 0 or x > size - 1 or y > size - 1:
        if x != -1 and y != -1:
            print("Player please enter the values in range 0 to 2")
        return False
    elif grid[x][y] != '-':
        print("Provided coordinates are filled, enter different coordinates")
        return False
    return True

def DidSomeoneWin(ch):

    for i in range(size - 2):
        if(grid[i][i] == ch and grid[i+1][i+1] == ch and grid[i+2][i+2] == ch):
            return True
        elif(grid[i][i+2] == ch and grid[i+1][i+1] == ch and grid[i+2][i] == ch):
            return True

    for i in range(size - 2):
        for j in range(size):
            if(grid[i][j] == ch and grid[i+1][j] == ch and grid[i+2][j] == ch):
                return True
            elif(grid[j][i] == ch and grid[j][i+1] == ch and grid[j][i+2] == ch):
                return True
    return False

def IsGameOver():
    if DidSomeoneWin('X'):
        print("Congratulations Player 1")
        return True
    elif DidSomeoneWin('O'):
        print("Congratulations Player 2")
        return True
    return False

def main():
    Initalize()
    move = 0

    x = -1 
    y = -1
    isPlayer1Turn = True
    while(move < size * size):
        ShowGrid()
        if isPlayer1Turn:
            x, y = Player1Input()
            ModifyGrid(x, y, 'X')
            isPlayer1Turn = False
        else:
            x, y = Player2Input()
            ModifyGrid(x, y, 'O')
            isPlayer1Turn = True
        if IsGameOver():
            return
        move += 1
    print("Game Drawn! Well played both the players")

main()