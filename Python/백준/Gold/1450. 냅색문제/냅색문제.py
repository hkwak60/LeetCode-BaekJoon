import sys
from bisect import bisect_right

N, C = map(int, sys.stdin.readline().strip().split())
objects = list(map(int,sys.stdin.readline().strip().split()))
if N==1:
    if objects[0]<=C:
        print(2)
    else:
        print(1)
    exit()

left = objects[:len(objects)//2]
right = objects[len(objects)//2:]

def get_subset_sum(arr):
    subset_sum = []

    def dfs(index, curr_sum):
        if index==len(arr):
            subset_sum.append(curr_sum)
            return
        dfs(index+1, curr_sum+arr[index])
        dfs(index+1, curr_sum)
    
    dfs(0,0)
    return sorted(subset_sum)

left_subset_sum = get_subset_sum(left)
right_subset_sum = get_subset_sum(right)

res = 0

for l in left_subset_sum:
    count = bisect_right(right_subset_sum, C - l)
    res += count


print(res)