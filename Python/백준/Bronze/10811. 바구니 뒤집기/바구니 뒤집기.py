line = input().split()

N = int(line[0])
M = int(line[1])

basket = []
for i in range(N):
    basket.append(i+1)

def swap(list, i, j):
    if i>=j:
        return
    else:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        swap(list, i+1, j-1)

for s in range(M):
    swaps = input().split()
    i = int(swaps[0])-1
    j = int(swaps[1])-1
    swap(basket,i,j)

print(*basket)
