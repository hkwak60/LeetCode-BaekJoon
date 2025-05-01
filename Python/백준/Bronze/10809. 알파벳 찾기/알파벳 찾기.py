import sys

chars = list(sys.stdin.readline().strip())
res = [-1 for i in range(26)]
for i in range(len(chars)):
    if res[ord(chars[i])-97]==-1:
        res[ord(chars[i])-97] = i
print(*res)