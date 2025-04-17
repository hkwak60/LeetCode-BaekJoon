import sys

N = int(sys.stdin.readline().strip())

def make_one(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 1
    if n%3==2:
        from_three = 3+make_one((n-2)//3)
    elif n%3==1:
        from_three = 2+make_one((n-1)//3)
    else:
        from_three = 1+make_one(n//3)
    if n%2==1:
        from_two = 2+make_one((n-1)//2)
    else:
        from_two = 1+make_one(n//2)
    return min(from_three,from_two)

print(make_one(N))