import sys

curr = list(map(int, sys.stdin.readline().strip().split()))
dday = list(map(int, sys.stdin.readline().strip().split()))

if dday[0] - curr[0] > 1000 or (dday[0] - curr[0] == 1000 and 
    (dday[1] > curr[1] or (dday[1] == curr[1] and dday[2] >= curr[2]))):
    print('gg')
    exit()

days = 0

def leapyear(yy):
    return yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0)

def remaining_days(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapyear(year):
        days_in_month[1] = 29
    return sum(days_in_month[month:]) - day

def elapsed_days(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapyear(year):
        days_in_month[1] = 29
    return sum(days_in_month[:month-1]) + day

if curr[0]!=dday[0]:
    for year in range(curr[0] + 1, dday[0]):
        days += 366 if leapyear(year) else 365
    days += remaining_days(curr[0],curr[1] - 1, curr[2])
    days += elapsed_days(dday[0],dday[1], dday[2])
else: 
    days = elapsed_days(dday[0], dday[1], dday[2]) - elapsed_days(curr[0], curr[1], curr[2])

print(f'D-{days}')