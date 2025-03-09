cnt = int(input())

set = []
price = 0
for _ in range(cnt):
    set.append(int(input()))
prices = sorted(set)

for _ in range(cnt%3):
    price+=prices.pop(0)
for i in range(cnt-cnt%3):
    if i%3!=0:
        price+=prices[i]

print(price)