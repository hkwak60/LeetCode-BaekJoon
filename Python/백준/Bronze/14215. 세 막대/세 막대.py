sticks = sorted(map(int, input().split()))

print(sticks[0]+sticks[1]+min(sticks[2],(sticks[0]+sticks[1]-1)))