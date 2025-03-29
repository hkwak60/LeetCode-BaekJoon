import sys

N = int(sys.stdin.readline().strip())
switches = list(map(int, sys.stdin.readline().strip().split()))

S = int(sys.stdin.readline().strip())

def girl(switch, left, right):
    if left<0 or right>=len(switch) or switch[left]!=switch[right]:
        return
    else:
        if left==right:
            switch[left]= 1-switch[left]
        else:
            switch[left]= 1-switch[left]
            switch[right]= 1-switch[right]
        return girl(switch, left-1, right+1)

def boy(switch, number):
    for i in range(number - 1, len(switch), number):
        switch[i] = 1 - switch[i]
    return

for s in range(S):
    line = list(map(int, sys.stdin.readline().strip().split()))
    if line[0]==2:
        girl(switches, line[1]-1,line[1]-1)
    else:
        boy(switches, line[1])

for i in range(0, len(switches), 20):
    print(" ".join(map(str, switches[i : i + 20])))