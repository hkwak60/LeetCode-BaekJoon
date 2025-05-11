from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())

maze = []
for _ in range(N):
    maze.append(list(sys.stdin.readline().strip()))

dist = []
for r in range(N):
    dist.append([])
    for c in range(M):
        if maze[r][c]=='1':
            dist[r].append(float('inf'))
        else:
            dist[r].append('-')

dist[N-1][M-1]=1

q = deque()
directions = [[0,1],[0,-1],[1,0],[-1,0]]

q.append((N-1,M-1))
while q:
    r, c = q.popleft()
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<M and dist[nr][nc]!='-' and dist[nr][nc] > dist[r][c]+1:
            dist[nr][nc] = dist[r][c]+1
            q.append((nr,nc))

print(dist[0][0])