line = input().split()

N = line[0]
M = line[1]

basket = []
for i in range(1,int(N)+1):
    basket.append(i)

for i in range (int(M)):
    swap = input().split()
    temp = basket[int(swap[0])-1]
    basket[int(swap[0])-1] = basket[int(swap[1])-1]
    basket[int(swap[1])-1] = temp

print(*basket)