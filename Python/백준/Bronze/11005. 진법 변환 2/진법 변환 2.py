sysin = list(map(int,input().split()))

digits = 0
while(sysin[0]>=sysin[1]**digits):
    digits+=1

res = ''

for i in range(digits):
    num = int(sysin[0]/sysin[1]**(digits-i-1))
    sysin[0]-= num*sysin[1]**(digits-i-1)
    if num>=10:
        res+=chr(num+55)
    else:
        res+=str(num)

if res=='':
    print(0)
else:
    print(res)