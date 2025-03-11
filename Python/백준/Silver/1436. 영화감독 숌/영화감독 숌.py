def title(n):
    count = 0
    while n>0:
        if n%1000==666:
            return True
        n=n//10
    return False

n = int(input())

res = []
i = 666
while len(res)<n:
    if title(i):
        res.append(i)
    i+=1

print(res[-1])