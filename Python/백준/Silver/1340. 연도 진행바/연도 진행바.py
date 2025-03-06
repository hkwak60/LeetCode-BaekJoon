def days_of_year(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return 366
            else:
                return 365
        else:
            return 366
    return 365

line = input().split()
Month= line[0]
Day = int(line[1].split(",")[0])-1
Year = int(line[2])
Hour = int(line[3].split(":")[0])
Min = int(line[3].split(":")[1])

total_days = days_of_year(Year)
days_of_month = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
if total_days==366:
    days_of_month['February'] = 29

passed_days = 0

for months, days in days_of_month.items():
    if Month==months:
        break
    passed_days+=days

passed_days+=Day
total_minutes = total_days*24*60
passed_minutes = passed_days*24*60+Hour*60+Min
print(passed_minutes/total_minutes*100)