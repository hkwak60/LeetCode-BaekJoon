def create(M):
    N = M
    while M>0:
        N+=M%10
        M//=10
    return N

M = int(input())
if M>100:
    for i in range(M-100,M):
        if create(i)==M:
            print(i)
            exit()
else:
    for i in range(1,M):
        if create(i)==M:
            print(i)
            exit()

print(0)