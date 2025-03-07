a = input().split()
b = input().split()
c = input().split()

res = ''
if a[0]==b[0]:
    res+=c[0]
elif a[0]==c[0]:
    res+=b[0]
else:
    res+=a[0]

res+=' '
if a[1]==b[1]:
    res+=c[1]
elif a[1]==c[1]:
    res+=b[1]
else:
    res+=a[1]
print(res)