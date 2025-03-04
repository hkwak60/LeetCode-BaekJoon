finger = int(input())
count = int(input())

if finger==1:
    print(count*8)
elif finger==2:
    res = 1 +int(count/2)*8
    if count%2!=0:
        res+=6
    print(res)
elif finger==3:
    print(count*4+2)
elif finger==4:
    res = 3+int(count/2)*8
    if count%2!=0:
        res+=2
    print(res)
else:
    print(4+count*8)