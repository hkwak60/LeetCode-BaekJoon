import sys
import bisect

n = int(sys.stdin.readline())

if n==5:
    print(2)
    exit()
def Eratosthenes(num):
    primenumbers=[]
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            primenumbers.append(p)
    return primenumbers

prime = Eratosthenes(n)

count = 0

for i in range(1, int(n**0.5)+3):
    idx = bisect.bisect_left(prime,n//i)
    if idx-i//2<0:
        break
    if i%2!=0:
        target = sum(prime[idx-i//2:idx+i//2+1])
        if target==0:
            continue
        iter = 1
        if target>n:
            while idx-i//2-iter>=0 and target>n:
                target = sum(prime[idx-i//2-iter:idx+i//2+1-iter])
                iter+=1
        elif target<n:
            while target<n:
                target = sum(prime[idx-i//2+iter:idx+i//2+1+iter])
                iter+=1
        if target==n:
            count+=1
    else:
        target = sum(prime[idx-i//2:idx+i//2])
        if target==0:
            continue
        iter = 1
        if target>n:
            while idx-i//2-iter>=0 and target>n:
                target = sum(prime[idx-i//2-iter:idx+i//2-iter])
                iter+=1
        elif target<n:
            while target<n:
                target = sum(prime[idx-i//2+iter:idx+i//2+iter])
                iter+=1
        if target==n:
            count+=1

print(count)
