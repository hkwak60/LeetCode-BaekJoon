while True:
    sides = sorted(map(int,input().split()))

    if sides == [0,0,0]:
        break

    a,b,c = sides
    if a+b<=c:
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')