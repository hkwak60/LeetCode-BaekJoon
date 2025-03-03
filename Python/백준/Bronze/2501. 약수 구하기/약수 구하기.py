line = list(map(int, input().split()))

a = line[0]
b = line[1]-1

div = []

for i in range(1, a+1):
    if a/i==int(a/i):
        div.append(i)

if b<len(div):
    print(div[b])
else:
    print(0)