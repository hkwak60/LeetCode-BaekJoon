row, col = map(int,input().split())

chess = []
for _ in range(row):
    chess.append(list(input()))


def minimum_change(r,c,board):
    Wstart = 0
    Bstart = 0
    for i in range(r,r+8):
        for j in range(c,c+8):
            if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                if board[i][j]!='W':
                    Wstart+=1
                else:
                    Bstart+=1
            elif (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                if board[i][j]!='B':
                    Wstart+=1
                else:
                    Bstart+=1
    return min(Wstart,Bstart)

result = 64
for i in range(row-7):
    for j in range(col-7):
        result = min(result,minimum_change(i,j,chess))

print(result)