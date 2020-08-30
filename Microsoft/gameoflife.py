def gameoflife(board):
    if not board or not board[0]:
        return None
    m = len(board)
    n = len(board[0])
    for i, row in enumerate(board):
        for j, ele in enumerate(row):
            count = 0
            for a in range(max(0,i-1),min(i+2,m)):
                for b in range(max(0,j-1),min(j+2,n)):
                    if (a,b)!=(i,j) and 1<=board[a][b]<=2:
                        count +=1
            if board[i][j]==0:
                if count==3:
                    board[i][j]=3
            else:
                if count<2 or count>3:
                    board[i][j]=2
    for i in range(m):
        for j in range(n):
            if board[i][j]==2:
                board[i][j]=0
            if board[i][j]==3:
                board[i][j]=1
    return board
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(gameoflife(board))