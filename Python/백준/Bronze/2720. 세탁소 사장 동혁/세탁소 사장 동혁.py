case = int(input())


res = ''
for i in range(case):
    change = int(input())
    num = 0
    if change>=25:
        while(change>=25*(num+1)):
            num+=1
        change-=num*25
    res+=str(num)+' '
    num = 0
    if change>=10:
        while(change>=10*(num+1)):
            num+=1
        change-=num*10
    res+=str(num)+' '
    num = 0
    if change>=5:
        while(change>=5*(num+1)):
            num+=1
        change-=num*5
    res+=str(num)+' '
    res+=str(change)+'\n'

print(res, end='')