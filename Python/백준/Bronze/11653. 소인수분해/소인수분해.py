def sieve(limit):
    primes = [True] *(limit +1)
    primes[0] = primes[1]=False

    for i in range(2, int(limit**0.5)+1):
        if primes[i]:
            for m in range(i*i, limit+1, i):
                primes[m] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]

a = int(input())

prime = sieve(a)
res = ''

while a>1:
    breakable = False
    for p in prime:
        if a/p == int(a/p):
            breakable = True
            res+=str(p)+'\n'
            a/=p
            break
    if not breakable:
        res+=str(int(a))+'\n'
        a/=a

print(res,end='')