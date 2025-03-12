test = int(input())

for _ in range(test):
    input()
    r, c = map(int,input().split())
    board = []
    for _ in range(r):
        board.append(list(input()))
    
    candies = 0
    for i in range(r):
        for j in range(c):
            if board[i][j]=='o':
                if j>0 and j<c-1:
                    if board[i][j-1]=='>' and board[i][j+1]=='<':
                        candies+=1
                if i>0 and i<r-1: 
                    if board[i-1][j]=='v' and board[i+1][j]=='^':
                        candies+=1
    print(candies)