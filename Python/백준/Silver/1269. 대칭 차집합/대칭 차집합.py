import sys

A,B = map(int,sys.stdin.readline().strip().split())

setA = set(map(int,sys.stdin.readline().strip().split()))
setB = set(map(int,sys.stdin.readline().strip().split()))

dup = 0
for a in setA:
    if a in setB:
        dup+=1

print(A+B-(2*dup))