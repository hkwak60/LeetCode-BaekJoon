import sys

N = int(sys.stdin.readline().strip())

nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

for n in sorted(nums):
    print(n)