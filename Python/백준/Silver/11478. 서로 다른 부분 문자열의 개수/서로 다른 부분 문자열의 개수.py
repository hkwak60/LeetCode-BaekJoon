import sys

S = sys.stdin.readline().strip()
subset = set()

n = len(S)
for i in range(n):
    for j in range(i + 1, n + 1):
        subset.add(S[i:j])

print(len(subset))