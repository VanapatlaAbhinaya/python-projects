from tkinter import *

root = Tk()
canvas = Canvas(root, width = 450, height = 400)

canvas.pack()

canvas.bind("<1>", lambda x: PlacePiece(TheBoard, canvas.gettags(CURRENT)))

for i in range(1,8):
    canvas.create_rectangle(i*50, 10, i*50 + 50, 30, fill = "white", tag = "button"+str(i))
    canvas.create_text(i*50+25, 20, text = "Place", tag = "button"+str(i))   

def ResetGame():
    global TheBoard, turn
    TheBoard = {}
    turn = "R"

    canvas.bind("<1>", lambda x: PlacePiece(TheBoard, canvas.gettags(CURRENT)))

    for i in range(1,7):
        for j in range(1,8):
            key = str(j)+str(i)
            TheBoard.setdefault(key, " ")

    for i in range(1,7):
        for j in range(1,8):
            key = str(j) + str(i)

            canvas.create_rectangle(j*50, i*50, j*50 + 50, i*50 + 50, fill = "blue", outline = "blue")
            canvas.create_oval(j*50 + 3, i*50 + 3, j*50 + 47, i*50 + 47, fill = "white", tag = "piece"+key)

    canvas.create_text(225, 360, text = "It is " + turn + "'s turn", tag = "TurnText")
        
def PlacePiece(board, column):
    global turn

    try:
        column[0]

    except:
        return

    else:
        column = column[0]
    if column[:6] != "button":
        return

    col = column[-1]

    while 1:
        try:
            int(col)
            board[col + "1"]

        except:
            return

        else:
            if board[col + "1"] != " ":
                return

            else:
                break

    for i in range(1,7):
        pos = col + str(i)

        if board[pos] != " " or i == 6:
            if i == 6 and board[pos] == " ":
                board[pos] = turn

            else:
                board[col+str(i-1)] = turn
                
            break

    for j in range(1,7):
        for i in range(1,8):
            if board[str(i) + str(j)] == "R":
                canvas.itemconfig("piece" + str(i) + str(j), fill = "red")

            elif board[str(i) + str(j)] == "Y":
                canvas.itemconfig("piece" + str(i) + str(j), fill = "yellow")

    turn = ChangeTurn()
    canvas.itemconfig("TurnText", text = "It is " + turn + "'s turn")

    global top

    if " " not in TheBoard.values():
        top = Toplevel(root)

        label = Label(top, text = "It's a draw")
        resetbutton = Button(top, text = "Reset Game", command = CloseGame)
        
        label.pack()
        resetbutton.pack()


    if CheckBoard(TheBoard):
        
        top = Toplevel(root)
        
        label = Label(top, text = ChangeTurn() + " wins!")
        resetbutton = Button(top, text = "Reset Game", command = CloseGame)
        
        label.pack()
        resetbutton.pack()

        canvas.bind("<1>", CloseGame)

def CloseGame(event = None):
    canvas.delete("TurnText")
    top.destroy()
    ResetGame()

                

def CheckHorizontal(board):
    for j in range(1,7):
        for i in range(1,5):
            spot1 = board[str(i) + str(j)]

            if spot1 != " ":
                spot2 = board[str(i+1) + str(j)]
                spot3 = board[str(i+2) + str(j)]
                spot4 = board[str(i+3) + str(j)]

                if spot1 == spot2 and spot1 == spot3 and spot1 == spot4:
                    return True

def CheckVertical(board):
    for i in range(1,8):
        for j in range(1,4):
            spot1 = board[str(i) + str(j)]

            if spot1 != " ":
                spot2 = board[str(i) + str(j+1)]
                spot3 = board[str(i) + str(j+2)]
                spot4 = board[str(i) + str(j+3)]

                if spot1 == spot2 and spot1 == spot3 and spot1 == spot4:
                    return True

def CheckDiagonalUL(board):
    for i in range(1,5):
        for j in range(1,4):
            spot1 = board[str(i) + str(j)]

            if spot1 != " ":
                spot2 = board[str(i+1) + str(j+1)]
                spot3 = board[str(i+2) + str(j+2)]
                spot4 = board[str(i+3) + str(j+3)]

                if spot1 == spot2 and spot1 == spot3 and spot1 == spot4:
                    return True

def CheckDiagonalUR(board):
    for i in range(7,3,-1):
        for j in range(1,4):
            spot1 = board[str(i) + str(j)]

            if spot1 != " ":
                spot2 = board[str(i-1) + str(j+1)]
                spot3 = board[str(i-2) + str(j+2)]
                spot4 = board[str(i-3) + str(j+3)]

                if spot1 == spot2 and spot1 == spot3 and spot1 == spot4:
                    return True
    
def CheckBoard(board):
    return (CheckHorizontal(board) or CheckVertical(board) or CheckDiagonalUL(board) or CheckDiagonalUR(board))
    
def ChangeTurn():
    if turn == "R":
        return "Y"

    else:
        return "R"

ResetGame()
root.mainloop()



        