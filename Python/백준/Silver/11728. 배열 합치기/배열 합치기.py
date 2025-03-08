x, y = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = []
i, j = 0, 0

while i < x and j < y:
    if A[i] < B[j]:
        res.append(A[i])
        i += 1
    else:
        res.append(B[j])
        j += 1

res.extend(A[i:])
res.extend(B[j:])

print(*res)