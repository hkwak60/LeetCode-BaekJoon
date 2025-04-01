import sys

N, Cut = map(int,sys.stdin.readline().strip().split())

numbers = list(map(int,sys.stdin.readline().strip().split()))

print(sorted(numbers)[-Cut])
