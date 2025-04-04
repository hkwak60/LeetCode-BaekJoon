import sys

N = int(sys.stdin.readline().strip())

coord = []
for _ in range(N):
    coord.append(list(map(int,sys.stdin.readline().strip().split())))

s_coord = sorted(coord, key = lambda x: (x[1],x[0]))

for c in s_coord:
    print(*c)