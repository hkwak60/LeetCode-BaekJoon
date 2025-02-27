line = input().split(" ")
N = int(line[0])
M = int(line[1])

A1 = []
res = []
for a in range(2):
    if a ==0:
        for i in range(N):
            line = input().split(" ")
            A1.append(line)
    else:
        for i in range(N):
            line = input().split(" ")
            res.append([])
            for j in range(M):
                res[i].append(int(A1[i][j])+int(line[j]))

for ar in res:
    print(*ar)