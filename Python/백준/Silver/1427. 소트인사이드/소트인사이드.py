import sys

line = list(map(int,sys.stdin.readline().strip()))

sline = sorted(line)
for i in range(len(line)-1,-1, -1):
    print(sline[i], end='')

print()