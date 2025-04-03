import sys

N = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))
nums_dict = {}
for n in nums:
    nums_dict[n] = 1

s_nums_dict = dict(sorted(nums_dict.items(), key=lambda x: x[0]))

added_val = 0
new_sums_dict = {}
for n in s_nums_dict:
    new_sums_dict[n] = added_val
    added_val+=s_nums_dict[n]

result = []
for n in nums:
    result.append(new_sums_dict[n])

print(*result)