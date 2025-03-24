import sys

N = int(sys.stdin.readline().strip())

meetings = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
meetings.sort(key = lambda x: (x[1],x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
    if start >=  last_end_time:
        count += 1
        last_end_time = end

print(count)