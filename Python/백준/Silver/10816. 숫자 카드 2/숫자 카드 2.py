import bisect

input()
arr = sorted(map(int,input().split()))
input()
searching = list(map(int,input().split()))


res=[]
for s in searching:
    res.append(bisect.bisect(arr,s)-bisect.bisect_left(arr,s))
print(*res)