import sys

N = int(sys.stdin.readline().strip())

req = list(map(int,sys.stdin.readline().strip().split()))

budget = int(sys.stdin.readline().strip())
req = sorted(req)

limit = budget/N
while len(req)>1 and req[0]<=limit:
    minimum = req[0]
    del req[0]
    budget-=minimum
    N-=1
    limit = budget/N

print(min(req[0],int(limit)))