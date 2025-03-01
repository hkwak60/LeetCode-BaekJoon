papers = int(input())

plane = []
for i in range(100):
    plane.append([False]*100)

for _ in range(papers):
    coord = list(map(int, input().split()))
    for i in range(coord[0],coord[0]+10):
        for j in range(coord[1], coord[1]+10):
            if not plane[i][j]:
                plane[i][j] = True

area = 0
for i in range(100):
    for j in range(100):
        if plane[i][j]:
            area+=1
print(area)
