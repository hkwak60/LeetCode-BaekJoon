case = int(input())

for _ in range(case):
    clothes = int(input())
    closet = {}
    for _ in range(clothes):
        type = input().split()[1]
        closet[type] = closet.get(type,0)+1

    possible = 1
    for count in closet.values():
        possible*=(count+1)
    print(possible-1)
