from tkinter import *
import math
import time

#Globals
EMPTY = ""
X = "X"
O = "O"
TIE = "TIE"
boardWinners = [[EMPTY for i in range(3)]for i in range(3)]
getBoard = [[1,2,3],[4,5,6],[7,8,9]]
boardNumber = None

global player
player = X
# Set up main window and frame
tk = Tk()
tk.geometry("")
main_frame = Frame(tk)
main_frame.grid()

def boardWinner(winner,n,button):
    #create X shape on won board, triggered by winner()
    if winner == X:
        lastMove=EMPTY
        boardWinners[int(math.floor(n)/3)][(n) % 3] = X
        button[(n) % 3][int(math.floor(n)/3)][0][0].configure(text = X,bg = ("red"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][2][0].configure(text = X,bg = ("red"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][1][1].configure(text = X,bg = ("red"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][0][2].configure(text = X,bg = ("red"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][2][2].configure(text = X,bg = ("red"),relief = "groove")

        button[(n) % 3][int(math.floor(n)/3)][0][1].configure(text = "-", bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][1][0].configure(text = "-", bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][1][2].configure(text = "-", bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][2][1].configure(text = "-", bg = ("gray"),relief = "groove")
    #create O shape on won board
    else:
        lastMove=EMPTY
        boardWinners[int(math.floor(n)/3)][(n) % 3] = O
        button[(n) % 3][int(math.floor(n)/3)][0][0].configure(text = "-",bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][2][0].configure(text = "-",bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][1][1].configure(text = "-",bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][0][2].configure(text = "-",bg = ("gray"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][2][2].configure(text = "-",bg = ("gray"),relief = "groove")

        button[(n) % 3][int(math.floor(n)/3)][0][1].configure(text = O, bg = ("#6599FF"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][1][0].configure(text = O, bg = ("#6599FF"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][1][2].configure(text = O, bg = ("#6599FF"),relief = "groove")
        button[(n) % 3][int(math.floor(n)/3)][2][1].configure(text = O, bg = ("#6599FF"),relief = "groove")


def winner(button):
    #checks each board for a winner
    waysToWin = ((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for n in range(9):
        xCo = (n) % 3
        yCo = int(math.floor(n)/3)
        board = []
        for x in range(3):
            for y in range(3):
                board.append(button[xCo][yCo][x][y].cget("text"))
        for row in waysToWin:
            #if there is three in a row, win that board for the player
            if board[row[0]] == board[row[1]] == board[row[2]] == X:
                boardWinner(X,n,button)
            elif board[row[0]] == board[row[1]] == board[row[2]] == O:
                boardWinner(O,n,button)
def endGame(button):
    #Once a player has won the game, disable all buttons and remove all green
    for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        button[i][j][x][y]["state"] = DISABLED
                        if button[i][j][x][y].cget("text") not in (X,O,"-"):
                            button[i][j][x][y].configure(bg = "gray")

def winnerAll(player,boardWinners,button):
    #Check if there is 3 won boards in a row, using the 2D array boardWinners
    w = 0
    boardWinners2 = []
    waysToWin2 = ((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    #This meant I could copy previous code and I'm lazy
    for i in range(3):
        for j in range(3):
            boardWinners2.append(boardWinners[i][j])

    for w in range(9):
        for row in waysToWin2:
            if boardWinners2[row[0]] == boardWinners2[row[1]] == boardWinners2[row[2]] !="":
                #If there is a winner, pop-up alert to show who won
                infoWin = Toplevel(bg = "black")
                infoWin.attributes("-topmost", True)
                infoWin.title("GAME WON")
                endGame(button)
                msg = Message(infoWin, text="Player " + player + " has WON!")
                msg.configure(font = 20,fg = "green", bg = "black")
                msg.pack()

                exitB = Button(infoWin, text="Dismiss",bg = "black", fg = "green", font = 16, command=infoWin.destroy)
                exitB.pack()
                return player
    return None

def move(i,j,x,y,button):
    #This function is triggered by clicking a button and inherits the button's co-ords on the board
    global player
    if player == X:
        plaCol = "red"
    else:
        plaCol = "#6599FF"
    button[i][j][x][y].configure(text = player, relief = "sunken", bg = plaCol, state = DISABLED)
    winner(button)

    if boardWinners[x][y] != "":
        #If forced board has already been won
        boardNumber = None
    else:
        boardNumber = getBoard[x][y]
    validMoves(boardNumber, button)
    #set all valid tiles to green and all invalid tiles to grey
    global tableWinner
    tableWinner = winnerAll(player, boardWinners,button)

    #change the turn every time a move is made
    if player == X:
        player = O
    else:
        player = X
    #update the UI
    tk.update()

def generateBoard():
    #Create 3x3 of frames
    frames = [[Frame(main_frame, width="20px", height=90, borderwidth =1) for i in range(3)] for i in range(3)]
    for x in range(3):
        for y in range(3):
            frames[x][y].grid(column = x, row = y+1, pady = 3)

    button = [[[["" for i in range(3)]for i in range(3)]for i in range(3)]for i in range(3)]
    #create 4D array of buttons. [1] = BoardX, [2] = BoardY, [3] = tileX, [4] = tileY
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    button[i][j][x][y] = Button(frames[i][j], relief = "raised", font = 20,height = 2, width = 6, bg = "gray", command = lambda i=i,j=j,x=x,y=y:move(i,j,x,y,button))
                    button[i][j][x][y].grid(column = y, row = x)

    return button

def displayInfo():
    #Pop-up explaining how to play
    infoWin = Toplevel(bg = "black")
    infoWin.attributes("-topmost", True)
    infoWin.title("How to play")
    msg = Message(infoWin, text="""
Welcome to the ULTIMATE TIC TAC TOE game,

Here's how to play:
- The first player will be X. They can click any tile on any board to make their move.
- Then, The second player, O, has their move. Their move will take place on the
board corresponding to the tile the X player played in.
- All valid moves will be highlighted green, if the player is pushed to a board that has already
been won or drawn, they may choose anywhere for their next move.
- Three X's or O's in a row on a board will win that board for the player
- The game is won when a player wins three boards in a row.""")
    msg.configure(font = 20,fg = "green", bg = "black")
    msg.pack()
    #button to close info pop-up
    exitB = Button(infoWin, text="Dismiss",bg = "black", fg = "green", font = 16, command=infoWin.destroy)
    exitB.pack()



def validMoves(boardNumber,button):
    if boardNumber == None:
        #if there is no forced board all tiles not taken are valid
        for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        if  button[i][j][x][y].cget("text") not in (X,O,"-"):
                            button[i][j][x][y].configure(bg = "green")
                            button[i][j][x][y]["state"] = NORMAL

                        else:
                            button[i][j][x][y]["state"] = DISABLED
                            if button[i][j][x][y].cget("text") not in (X,O,"-"):
                                button[i][j][x][y].configure(bg = "gray")

    else:
        xCo = (boardNumber-1) % 3
        yCo = int(math.floor(boardNumber-1)/3) #These two get X and Y co-ords from the board number(1-9)
        #If there is a forced board, highlight only tiles on this board

        for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        if i != xCo or j != yCo:
                            button[i][j][x][y]["state"] = DISABLED
                            if button[i][j][x][y].cget("text") not in (X,O,"-"):
                                button[i][j][x][y].configure(bg = "gray")
        count = 0
        for x in range(3):
            for y in range(3):
                if button[xCo][yCo][x][y].cget("text") not in (X,O,"-"):
                    button[xCo][yCo][x][y].configure(bg = "green")
                    button[xCo][yCo][x][y]["state"] = NORMAL
                    count+=1
        #If there board has been drawn, there are no valid tiles so start again with no
        #board number
        if count == 0:
            validMoves(None,button)

    #I cant remember why this is here but I'm sure it's important
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    if boardWinners[j][i] != "":
                        button[i][j][x][y]["state"] = DISABLED
                        if button[i][j][x][y].cget("text") not in (X,O,"-"):
                            button[i][j][x][y].configure(bg = "gray")

def main(boardNumber):
    #Call the other functions
    button = generateBoard() #Button is the array of buttons
    tk.update() #Initiate the UI
    displayInfo() #Show the user how to play
    validMoves(boardNumber,button) #colour valid buttons. boardNumber = None here.
    tableWinner = None

    while tableWinner == None:
        #update label at the top of the board
        label = Label(main_frame, font = 8, text="Current Player: " + player)
        label.grid(column = 1, row  = 0)
        #update the UI
        tk.update()
        #Stop this Loop from running as fast as it can and tanking my computer
        time.sleep(0.1)

main(boardNumber)

