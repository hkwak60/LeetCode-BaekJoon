import sys

N = int(sys.stdin.readline().strip())

initial = set(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
search = list(map(int,sys.stdin.readline().strip().split()))

result = []
for s in search:
    if s in initial:
        result.append(1)
    else:
        result.append(0)

print(*result)