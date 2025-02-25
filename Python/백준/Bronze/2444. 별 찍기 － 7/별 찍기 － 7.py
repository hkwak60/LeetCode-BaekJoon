pattern = int(input())

for i in range(1,pattern):
    print(" "*(pattern-i)+"*"*(2*i-1))
for i in range(pattern,0, -1):
    print(" "*(pattern-i)+"*"*(2*i-1))