sysin = input().split()

sum = 0
for i in range(len(sysin[0])):
    num = ord(list(sysin[0])[len(sysin[0])-i-1])
    if num>=65:
        sum+=(num-55)*(int(sysin[1]))**i
    else:
        sum+=(num-48)*(int(sysin[1]))**i
print(sum)