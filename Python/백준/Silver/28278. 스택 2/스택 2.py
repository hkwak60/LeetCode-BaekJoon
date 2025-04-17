import sys

N = int(sys.stdin.readline().strip())

res = []
for _ in range(N):
    input = sys.stdin.readline().strip()
    if len(input.split())==1:
        number = int(input)
    else:
        number = int(input.split()[0])
        put_int = int(input.split()[1])

    if number==1:
        res.append(put_int)
    elif number==2:
        if len(res)!=0:
            print(res.pop())
        else:
            print(-1)
    elif number==3:
        print(len(res))
    elif number==4:
        if len(res)==0:
            print(1)
        else:
            print(0)
    elif number==5:
        if len(res)!=0:
            print(res[-1])
        else:
            print(-1)