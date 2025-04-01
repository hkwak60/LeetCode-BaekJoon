import sys

numbers = []
for _ in range(5):
    numbers.append(int(sys.stdin.readline().strip()))


print(sum(numbers)//5)
print(sorted(numbers)[2])