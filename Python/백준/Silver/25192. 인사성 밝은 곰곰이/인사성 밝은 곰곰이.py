res = 0
lst = set()
for i in range(int(input())):
    nickname = input()
    if nickname=='ENTER':
        lst.clear()
        continue
    if nickname not in lst:
        lst.add(nickname) 
        res+=1
print(res)