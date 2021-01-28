import random

rows, cols = (8, 8)
chessboard = [["_" for x in range(rows)] for y in range(cols)]
start = random.randint(0, 7)
placed = []
legal2 = []

def show_chessboard():
    for i in range(8):
        for j in range(8):
            print(chessboard[i][j], end=" ")

        print("\n", end="")



def attack(r, c):
    for i in range(1, 8):
        if r + i < 8 and c + i < 8 and chessboard[r + i][c + i] != "Q":
            chessboard[r + i][c + i] = "x"
        if r - i > -1 and c - i > -1 and chessboard[r - i][c - i] != "Q":
            chessboard[r - i][c - i] = "x"
        if r + i < 8 and c - i > -1 and chessboard[r + i][c - i] != "Q":
            chessboard[r + i][c - i] = "x"
        if r - i > -1 and c + i < 8 and chessboard[r - i][c + i] != "Q":
            chessboard[r - i][c + i] = "x"
        if r + i < 8 and chessboard[r + i][c] != "Q":
            chessboard[r + i][c] = "x"
    if r + 1 < 8:
        legal = []
        for i in range(8):
            if chessboard[r + 1][i] == "_":
                legal.append(i)
    show_chessboard()
    print(legal)
    return legal




def move(pmoves, row):
    if row<7:
        try:
            mymove = random.choice(pmoves)
            chessboard[row][mymove] = "Q"
            placed.append(mymove)
            pmoves = attack(row, mymove)
            row+=1
            move(pmoves,row)
        except:
            for i in range(8):
                for j in  range(8):
                    chessboard[i][j]="_"
            placed.clear()

            start=random.randint(0,7)
            chessboard[0][start]="Q"
            placed.append(start)
            legal2=attack(0,start)
            move(legal2,1)

    else:
        chessboard[7][random.choice(pmoves)]="Q"
        for i in range(8):
            for j in range(8):
              if chessboard[i][j]=="x":
                  chessboard[i][j]="_"

        show_chessboard()
        print("finish")
        return 0


chessboard[0][start] = "Q"
placed.append(start)
legal2 = attack(0, start)
move(legal2,1)



